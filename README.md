# FOLK: First-Order-Logic (FOL) Guided Knowledge-Grounded Reasoning for Claim Verification

[Paper](https://arxiv.org/abs/2310.05253) | [Installation](#installation) | [To Run](#to-run) | [Results](#results)

FOLK is a claim verification model that can verify complex claims and generate explanations without the need for annotated evidence using Large Language Models (LLMs).

If our code or data helps you in your research, please kindly cite us:

```bibtex
@article{wang2023explainable,
  title={Explainable Claim Verification via Knowledge-Grounded Reasoning with Large Language Models},
  author={Wang, Haoran and Shu, Kai},
  journal={arXiv preprint arXiv:2310.05253},
  year={2023}
}
```

## Installation

Install conda environment from `environment.yml` file.

```sh
conda env create -n folk --file environment.yml
conda activate folk
```

Please add your OpenAI and [SerpApi](https://serpapi.com/) key in ```keys.py``` file.

## To Run

To decompose claims:

```sh
python decompose.py \
    --dataset ["hover", "feverous", "scifact"] \
    --hover_num_hop ["two", "three", "four"] \
    --feverous_challenge ["numerical", "reasoning", "table"] \
    --prompt_strategy ["direct", "cot", "self-ask", "logic"] \
    --model ["llama-7b", "llama-13b", "llama-30b", "text-davinci"] \
    --version "DEFINE YOUR VERSION" \
    --max_token 1024 \
    --temperature 0.7
```

To ground answers:

```sh
python groudning.py \
    --dataset ["hover", "feverous", "scifact"] \
    --hover_num_hop ["two", "three", "four"] \
    --feverous_challenge ["numerical", "reasoning", "table"] \
    --prompt_strategy ["direct", "cot", "self-ask", "logic"] \
    --model text-davinci \
    --model ["llama-7b", "llama-13b", "llama-30b", "text-davinci"] \
    --version "DEFINE YOUR VERSION" \
```

To make predictions:

```sh
python aggregate.py \
    --dataset ["hover", "feverous", "scifact"] \
    --hover_num_hop ["two", "three", "four"] \
    --feverous_challenge ["numerical", "reasoning", "table"] \
    --prompt_strategy ["direct", "cot", "self-ask", "logic"] \
    --model ["llama-7b", "llama-13b", "llama-30b", "text-davinci"] \
    --version "DEFINE YOUR VERSION" \
    --max_token 1024 \
    --temperature 0.7
```

To evaluate:

```sh
python evaluation.py \
    --dataset hover \
    --hover_num_hop three \
    --prompt_strategy logic \
    --model text-davinci \
    --version "V1.0"
```

## Results

The experiment results reported in Table 2 from the paper are listed in ```Final_Results``` folder. To evaluate the results, please execute the following script:

```sh
./results.sh
```

The ProgramFC baseline is contained in ```ProgramFC``` folder. The code is modified from the original repo to process dataset used in the paper.
