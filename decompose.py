import os
import pandas as pd
import json
import re
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
    model_path = "decapoda-research/llama-30b-hf"
    tokenizer = LlamaTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, device_map=args.device_map, load_in_8bit=True
    )
if args.model == "text-davinci" or args.model == "gpt-3.5-turbo":
    openai.api_key = OPENAI_KEY


def query_single(claim):
    full_prompt = prompt % (claim)

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
        response = output.split(claim, 1)[1]
    if args.model == "text-davinci":
        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=full_prompt,
            max_tokens=args.max_token,
            temperature=args.temperature,
        )
        response = completion.choices[0].text
    return response


def query_multiple(id_list, claim_list, label_list):
    out = []
    for uid, claim, label in tqdm(
        zip(id_list, claim_list, label_list), total=len(claim_list)
    ):
        full_prompt = prompt % (claim)

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
            # response = re.findall(r'>>>>>>(?s:.*?)------', output)[3]
            response = output.split(claim, 1)[1]
            print(claim)
            print(response)
        if args.model == "text-davinci":
            completion = openai.Completion.create(
                model="text-davinci-003",
                prompt=full_prompt,
                max_tokens=args.max_token,
                temperature=args.temperature,
            )
            response = completion.choices[0].text
            print(claim)
            print(response)
        if args.model == "gpt-3.5-turbo":
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": full_prompt}],
                max_tokens=args.max_token,
                temperature=args.temperature,
            )
            response = completion["choices"][0]["message"]["content"]
            # print(claim)
            print(response)
        out.append({"id": uid, "label": label, "claim": claim, "response": response})
    return out


if __name__ == "__main__":
    if args.dataset == "hover":
        if not os.path.exists(f"./HoVerDev/out/decompose"):
            os.makedirs(f"./HoVerDev/out/decompose")

        """Set Prompt"""
        if args.prompt_strategy == "cot":
            prompt = cot_decompose
        if args.prompt_strategy == "self-ask":
            prompt = cot_decompose
        if args.prompt_strategy == "logic":
            prompt = logic_decompose

        """ Single """
        # claim = ""
        # out = query_single(claim)
        # print(out)

        """ Multiple """
        df = pd.read_pickle(f"./HoVerDev/processed/{args.hover_num_hop}_hop_df_new.pkl")
        id_list = df["uid"]
        claim_list = df["claim"]
        label_list = df["label"]

        out = query_multiple(id_list, claim_list, label_list)
        with open(
            f"./HoVerDev/out/decompose/{args.model}_decompose_{args.prompt_strategy}_{args.hover_num_hop}_{args.version}.json",
            "w",
        ) as f:
            json.dump(out, f)

    if args.dataset == "feverous":
        if not os.path.exists(f"./FeverousDev/out/decompose"):
            os.makedirs(f"./FeverousDev/out/decompose")

        """Set Prompt"""
        if args.prompt_strategy == "cot":
            prompt = cot_decompose
        if args.prompt_strategy == "self-ask":
            prompt = cot_decompose
        if args.prompt_strategy == "logic":
            prompt = logic_decompose

        """ Single """
        # claim = ""
        # out = query_single(claim)
        # print(out)

        """ Multiple """
        df = pd.read_pickle(f"./FeverousDev/processed/{args.feverous_challenge}_df.pkl")
        id_list = df["uid"]
        claim_list = df["claim"]
        label_list = df["label"]

        out = query_multiple(id_list, claim_list, label_list)
        with open(
            f"./FeverousDev/out/decompose/{args.model}_decompose_{args.prompt_strategy}_{args.feverous_challenge}_{args.version}.json",
            "w",
        ) as f:
            json.dump(out, f)

    if args.dataset == "scifact":
        if not os.path.exists(f"./SciFact-Open/out/decompose"):
            os.makedirs(f"./SciFact-Open/out/decompose")

        """Set Prompt"""
        if args.prompt_strategy == "cot":
            prompt = cot_decompose
        if args.prompt_strategy == "self-ask":
            prompt = cot_decompose
        if args.prompt_strategy == "logic":
            prompt = logic_decompose

        """ Single """
        # claim = ""
        # out = query_single(claim)
        # print(out)

        """ Multiple """
        df = pd.read_pickle(f"./SciFact-Open/processed/df_new.pkl")
        id_list = df["uid"]
        claim_list = df["claim"]
        label_list = df["label"]

        out = query_multiple(id_list, claim_list, label_list)
        with open(
            f"./SciFact-Open/out/decompose/{args.model}_decompose_{args.prompt_strategy}_{args.version}.json",
            "w",
        ) as f:
            json.dump(out, f)

    print("Finished decompose using LLM!")
