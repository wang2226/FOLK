import argparse
import os
import json
import pandas as pd
from tqdm import tqdm

from prompts import Prompt_Loader
from utils import OpenAIModel


class Reasoning_Program_Generator:
    def __init__(self, args):
        self.args = args
        self.dataset_name = args.dataset_name
        self.model_name = args.model_name
        self.save_path = args.save_path
        self.num_programs_per_example = args.num_programs_per_example

        self.openai_api = OpenAIModel(
            args.api_key, args.model_name, args.stop_words, args.max_new_tokens
        )
        self.prompt_loader = Prompt_Loader()

    def update_results(self, sample, generated_text):
        program_list = [operation.strip() for operation in generated_text.split("\n")]
        # programs = [program_list]
        self.result_dict[sample["uid"]]["predicted_programs"].append(program_list)

    def batch_generate_programs(self, batch_size=10):
        # create output_dir
        self.result_dict = []
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

        # load dataset
        if args.my_data == "two":
            with open("../my_data/two_hop_df_new.json", "r") as f:
                raw_dataset = json.load(f)
            print(raw_dataset)
        if args.my_data == "three":
            with open("../my_data/three_hop_df_new.json", "r") as f:
                raw_dataset = json.load(f)
            print(raw_dataset)
        if args.my_data == "four":
            with open("../my_data/four_hop_df_new.json", "r") as f:
                raw_dataset = json.load(f)
            print(raw_dataset)
        if args.my_data == "numerical":
            with open("../my_data/numerical_df.json", "r") as f:
                raw_dataset = json.load(f)
            print(raw_dataset)
        if args.my_data == "reasoning":
            with open("../my_data/reasoning_df.json", "r") as f:
                raw_dataset = json.load(f)
            print(raw_dataset)
        if args.my_data == "table":
            with open("../my_data/table_df.json", "r") as f:
                raw_dataset = json.load(f)
            print(raw_dataset)

        raw_dataset = (
            raw_dataset
            if self.args.num_eval_samples < 0
            else raw_dataset[: self.args.num_eval_samples]
        )
        print(f"Loaded {len(raw_dataset)} examples from {self.dataset_name} dev set.")

        # generate programs
        temperature = 0.0 if self.num_programs_per_example == 1 else 0.7
        outputs = []
        # split dataset into chunks
        dataset_chunks = [
            raw_dataset[i : i + batch_size]
            for i in range(0, len(raw_dataset), batch_size)
        ]

        # initialize empty results
        result_dict = {}
        for idx, sample in enumerate(raw_dataset):
            result = {
                "idx": idx,
                "id": sample["uid"],
                "claim": sample["claim"],
                "gold": sample["label"],
                "predicted_programs": [],
            }
            result_dict[sample["uid"]] = result
        self.result_dict = result_dict

        # for each iteration
        for iteration in range(self.num_programs_per_example):
            print(f"Generating programs for iteration {iteration + 1}...")
            # for each chunk
            for chunk in tqdm(dataset_chunks):
                # create prompt
                full_prompts = [
                    self.prompt_loader.prompt_construction(
                        example["claim"], self.dataset_name
                    )
                    for example in chunk
                ]
                # print(full_prompts)
                try:
                    batch_outputs = self.openai_api.batch_generate(
                        full_prompts, temperature
                    )
                    # create output
                    for sample, output in zip(chunk, batch_outputs):
                        self.update_results(sample, output)
                except:
                    # generate one by one if batch generation fails
                    for sample, full_prompt in zip(chunk, full_prompts):
                        try:
                            output = self.openai_api.generate(full_prompt, temperature)
                            print(output)
                            self.update_results(sample, output)
                        except:
                            print(
                                "Error in generating reasoning programs for example: ",
                                sample["uid"],
                            )

        print(f"Generated {len(result_dict)} examples.")
        # create outputs
        for key in result_dict:
            outputs.append(result_dict[key])
        sorted_outputs = sorted(outputs, key=lambda x: x["idx"])

        # save outputs
        with open(
            os.path.join(
                self.save_path,
                f"{self.dataset_name}_N={self.num_programs_per_example}_{self.model_name}_{args.my_data}_programs.json",
            ),
            "w",
        ) as f:
            json.dump(sorted_outputs, f, indent=2, ensure_ascii=False)


def parse_args():
    parser = argparse.ArgumentParser()
    # dataset args
    parser.add_argument(
        "--dataset_name", default="HOVER", type=str, help=["HOVER", "FEVEROUS"]
    )
    parser.add_argument("--num_eval_samples", default=-1, type=int)
    parser.add_argument("--num_programs_per_example", default=1, type=int)
    parser.add_argument("--save_path", default="./results/programs", type=str)
    parser.add_argument(
        "--api_key",
        type=str,
        default="OPENAI KEY",
    )
    parser.add_argument("--model_name", type=str, default="text-davinci-003")
    parser.add_argument("--stop_words", type=str, default="# The claim is")
    parser.add_argument("--max_new_tokens", type=int, default=1024)
    parser.add_argument(
        "--my_data",
        type=str,
        default="two",
        help="[two, three, four, numerical, reasoning, table]",
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    generator = Reasoning_Program_Generator(args)
    generator.batch_generate_programs()
