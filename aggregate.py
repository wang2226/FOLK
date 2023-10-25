import os
import pandas as pd
import json
import pickle
from tqdm import tqdm

import torch
from transformers import AutoModelForCausalLM, LlamaTokenizer, BitsAndBytesConfig
import openai
from args import *
from prompt_library import *
from keys import *


if args.model == "llama-7b":
    model_path = "decapoda-research/llama-7b-hf"
    tokenizer = LlamaTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.float16, device_map=args.device_map
    )
if args.model == "llama-13b":
    model_path = "decapoda-research/llama-13b-hf"
    tokenizer = LlamaTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.float16, device_map=args.device_map
    )
if args.model == "llama-30b":
    model_path = "/data/haoran/llama-30b-hf"
    tokenizer = LlamaTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, device_map=args.device_map, load_in_8bit=True
    )
if args.model == "text-davinci" or args.model == "gpt-3.5-turbo":
    openai.api_key = OPENAI_KEY


def assemble_prompt_no_predicate(claim, question_list, grounded_answer_list):
    context = ""
    for question, answer in zip(question_list, grounded_answer_list):
        if question is None or answer is None:
            continue
        context = context + "\n" + answer
    # print(context)
    full_prompt = prompt % (claim, context)
    return context, full_prompt


def assemble_prompt(claim, predicates, question_list, grounded_answer_list):
    context = predicates + "\n"

    for question, answer in zip(question_list, grounded_answer_list):
        if question is None or answer is None:
            continue
        context = context + "\n" + question + "\n" + answer
    # print(context)
    full_prompt = prompt % (claim, context)
    return context, full_prompt


def query_single(context, full_prompt):
    if (
        args.model == "llama-7b"
        or args.model == "llama-13b"
        or args.model == "llama-30b"
    ):
        input_ids = tokenizer(full_prompt, return_tensors="pt").input_ids
        generation_output = model.generate(
            input_ids=input_ids, max_new_tokens=args.max_token
        )
        output = tokenizer.decode(generation_output[0])
        response = output.split(context, 1)[1]
    if args.model == "text-davinci":
        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=full_prompt,
            max_tokens=args.max_token,
            temperature=args.temperature,
        )
        response = completion.choices[0].text
    return response


def query_multiple(id_list, claim_list, label_list, context_list, full_prompt_list):
    out = []
    for uid, claim, label, context, full_prompt in tqdm(
        zip(id_list, claim_list, label_list, context_list, full_prompt_list),
        total=len(full_prompt_list),
    ):
        if (
            args.model == "llama-7b"
            or args.model == "llama-13b"
            or args.model == "llama-30b"
        ):
            input_ids = tokenizer(full_prompt, return_tensors="pt").input_ids
            generation_output = model.generate(
                input_ids=input_ids, max_new_tokens=args.max_token
            )
            output = tokenizer.decode(generation_output[0])
            response = output.split(context, 1)[1]
            print(response)
        if args.model == "text-davinci":
            try:
                completion = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=full_prompt,
                    max_tokens=args.max_token,
                    temperature=args.temperature,
                )
                response = completion.choices[0].text
            except:
                continue
            print(label)
            print(response)
        if args.model == "gpt-3.5-turbo":
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": full_prompt}],
                    max_tokens=args.max_token,
                    temperature=args.temperature,
                )
                response = completion["choices"][0]["message"]["content"]
            except:
                continue
            print(label)
            print(response)
        out.append(
            {
                "id": uid,
                "label": label,
                "claim": claim,
                "prompt": full_prompt,
                "response": response,
            }
        )
    return out


if __name__ == "__main__":
    if args.dataset == "hover":
        if not os.path.exists(f"./HoVerDev/out/aggregate"):
            os.makedirs(f"./HoVerDev/out/aggregate")

        """Set Prompt"""
        if args.prompt_strategy == "direct":
            prompt = direct_aggregate
        if args.prompt_strategy == "cot":
            prompt = cot_aggregate
        if args.prompt_strategy == "self-ask":
            prompt = self_ask_aggregate
        if args.prompt_strategy == "logic":
            prompt = logic_aggregate

        """ Single """
        # df = pd.read_pickle(
        #     f"./HoVerDev/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.hover_num_hop}_{args.version}.pkl")
        # index = 68
        # context, full_prompt = assemble_prompt(
        #     df["claim"][index], df["predicates"][index], df["questions"][index], df["grounded_answers"][index])
        # out = query_single(context, full_prompt)
        # print(df["label"][index])
        # print(out)

        """ Multiple """
        # df = pd.read_pickle(
        #     f"./HoVerDev/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.hover_num_hop}_{args.version}.pkl")
        df = pd.read_pickle(
            f"./HoVerDev/out/grounding/{args.model}_grounded_logic_{args.hover_num_hop}_{args.version}.pkl"
        )
        id_list = df["id"]
        claim_list = df["claim"]
        label_list = df["label"]
        context_list = []
        full_prompt_list = []

        if args.prompt_strategy == "direct":
            for c, q, ga in zip(df["claim"], df["questions"], df["grounded_answers"]):
                context_list.append("")
                full_prompt = prompt % (c)
                full_prompt_list.append(full_prompt)

        if args.prompt_strategy == "cot" or args.prompt_strategy == "self-ask":
            for c, q, ga in zip(df["claim"], df["questions"], df["grounded_answers"]):
                context, full_prompt = assemble_prompt_no_predicate(c, q, ga)
                context_list.append(context)
                full_prompt_list.append(full_prompt)

        if args.prompt_strategy == "logic":
            for c, p, q, ga in zip(
                df["claim"], df["predicates"], df["questions"], df["grounded_answers"]
            ):
                context, full_prompt = assemble_prompt(c, p, q, ga)
                context_list.append(context)
                full_prompt_list.append(full_prompt)

        out = query_multiple(
            id_list, claim_list, label_list, context_list, full_prompt_list
        )
        with open(
            f"./HoVerDev/out/aggregate/{args.model}_aggregate_{args.prompt_strategy}_{args.hover_num_hop}_{args.version}.json",
            "w",
        ) as f:
            json.dump(out, f)

    if args.dataset == "feverous":
        if not os.path.exists(f"./FeverousDev/out/aggregate"):
            os.makedirs(f"./FeverousDev/out/aggregate")

        """Set Prompt"""
        if args.prompt_strategy == "direct":
            prompt = direct_aggregate
        if args.prompt_strategy == "cot":
            prompt = cot_aggregate
        if args.prompt_strategy == "self-ask":
            prompt = self_ask_aggregate
        if args.prompt_strategy == "logic":
            prompt = logic_aggregate

        """ Single """
        # df = pd.read_pickle(
        #     f"./FeverousDev/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.feverous_challenge}_{args.version}.pkl")
        # index = 70
        # context, full_prompt = assemble_prompt(
        #     df["claim"][index], df["predicates"][index], df["questions"][index], df["grounded_answers"][index])
        # out = query_single(context, full_prompt)
        # print(full_prompt)
        # print(out)

        """ Multiple """
        df = pd.read_pickle(
            f"./FeverousDev/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.feverous_challenge}_{args.version}.pkl"
        )
        id_list = df["id"]
        claim_list = df["claim"]
        label_list = df["label"]
        context_list = []
        full_prompt_list = []

        if args.prompt_strategy == "direct":
            for c, q, ga in zip(df["claim"], df["questions"], df["grounded_answers"]):
                context_list.append("")
                full_prompt = prompt % (c)
                full_prompt_list.append(full_prompt)

        if args.prompt_strategy == "cot" or args.prompt_strategy == "self-ask":
            for c, q, ga in zip(df["claim"], df["questions"], df["grounded_answers"]):
                context, full_prompt = assemble_prompt_no_predicate(c, q, ga)
                context_list.append(context)
                full_prompt_list.append(full_prompt)

        if args.prompt_strategy == "logic":
            for c, p, q, ga in zip(
                df["claim"], df["predicates"], df["questions"], df["grounded_answers"]
            ):
                context, full_prompt = assemble_prompt(c, p, q, ga)
                context_list.append(context)
                full_prompt_list.append(full_prompt)

        out = query_multiple(
            id_list, claim_list, label_list, context_list, full_prompt_list
        )

        with open(
            f"./FeverousDev/out/aggregate/{args.model}_aggregate_{args.prompt_strategy}_{args.feverous_challenge}_{args.version}.json",
            "w",
        ) as f:
            json.dump(out, f)

    if args.dataset == "scifact":
        if not os.path.exists(f"./SciFact-Open/out/aggregate"):
            os.makedirs(f"./SciFact-Open/out/aggregate")

        """ Set Prompt """
        if args.prompt_strategy == "direct":
            prompt = direct_aggregate
        if args.prompt_strategy == "cot":
            prompt = cot_aggregate
        if args.prompt_strategy == "self-ask":
            prompt = self_ask_aggregate
        if args.prompt_strategy == "logic":
            prompt = logic_aggregate

        """ Multiple """
        df = pd.read_pickle(
            f"./SciFact-Open/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.version}.pkl"
        )
        id_list = df["id"]
        claim_list = df["claim"]
        label_list = df["label"]
        context_list = []
        full_prompt_list = []

        if args.prompt_strategy == "direct":
            for c, q, ga in zip(df["claim"], df["questions"], df["grounded_answers"]):
                context_list.append("")
                full_prompt = prompt % (c)
                full_prompt_list.append(full_prompt)

        if args.prompt_strategy == "cot" or args.prompt_strategy == "self-ask":
            for c, q, ga in zip(df["claim"], df["questions"], df["grounded_answers"]):
                context, full_prompt = assemble_prompt_no_predicate(c, q, ga)
                context_list.append(context)
                full_prompt_list.append(full_prompt)

        if args.prompt_strategy == "logic":
            for c, p, q, ga in zip(
                df["claim"], df["predicates"], df["questions"], df["grounded_answers"]
            ):
                context, full_prompt = assemble_prompt(c, p, q, ga)
                context_list.append(context)
                full_prompt_list.append(full_prompt)

        out = query_multiple(
            id_list, claim_list, label_list, context_list, full_prompt_list
        )

        with open(
            f"./SciFact-Open/out/aggregate/{args.model}_aggregate_{args.prompt_strategy}_{args.version}.json",
            "w",
        ) as f:
            json.dump(out, f)

    print("Finished aggregate using LLM!")
