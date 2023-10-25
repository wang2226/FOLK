import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--dataset",
    type=str,
    default="hover",
    help="specify dataset [hover, feverous, scifact]",
)

parser.add_argument(
    "--hover_num_hop",
    type=str,
    default="two",
    help="number of hops [two, three, four]",
)
parser.add_argument(
    "--feverous_challenge",
    type=str,
    default="reasoning",
    help="type of challenge [reasoning, numerical, table]",
)

parser.add_argument(
    "--prompt_strategy",
    type=str,
    default="logic",
    help="prompt strategy [cot, self-ask, logic]",
)
parser.add_argument("--version", type=str, default="V1.0", help="specify version")

parser.add_argument(
    "--model",
    type=str,
    default="text-davinci",
    help="specify llama model [llama-7b, llama-13b, llama-30b, text-davinci, gpt-3.5-turbo]",
)
parser.add_argument(
    "--device_map",
    type=str,
    default="auto",
    help="specify device map [auto, balanced, balanced_low_0, sequential]",
)
parser.add_argument(
    "--temperature", type=float, default=0.7, help="temperature for GPT-3.5"
)
parser.add_argument(
    "--max_token", type=int, default=1000, help="specify number of max new token"
)
args = parser.parse_args()

print(args)
