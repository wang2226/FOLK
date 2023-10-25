import os
import pandas as pd
import re
from tqdm import tqdm

from serpapi import GoogleSearch
from args import *
from keys import *


def trim(response):
    new_response = []
    for r in response:
        stripped = r.split("------", 1)[0]
        new_response.append(stripped)
    return new_response


def split_on_empty_lines(s):
    # greedily match 2 or more new-lines
    blank_line_regex = r"(?:\r?\n){2,}"
    return re.split(blank_line_regex, s.strip())


def extract_response(response):
    questions = []
    answers = []

    if args.prompt_strategy == "cot" or args.prompt_strategy == "self-ask":
        for r in response:
            # stripped = r.split(">>>>>>", 1)[1]
            stripped = r
            try:
                qa = split_on_empty_lines(stripped)[0]
                q = re.findall(r"Followup Question:\s*(.*)", qa)
                a = re.findall(r"Answer:\s*(.*)", qa)
            except:
                q = " "
                a = " "
            questions.append(q)
            answers.append(a)
        return questions, answers

    if args.prompt_strategy != "cot":
        predicates = []
        questions = []
        answers = []
        for r in response:
            stripped = r.split("Predicates:", 1)[1]
            p = split_on_empty_lines(stripped)[0]
            predicates.append(p)
            try:
                qa = split_on_empty_lines(stripped)[1]
                q = re.findall(r"Followup Question:\s*(.*)", qa)
                a = re.findall(r"Answer:\s*(.*)", qa)
            except:
                q = " "
                a = " "
            questions.append(q)
            answers.append(a)
        return predicates, questions, answers


def google_old(question):
    params = {
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "q": question,
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en",
    }

    search = GoogleSearch(params)
    result = search.get_dict()
    answer = ""

    if "answer_box" in result.keys() and "answer" in result["answer_box"].keys():
        answer = result["answer_box"]["answer"]
    elif "answer_box" in result.keys() and "snippet" in result["answer_box"].keys():
        answer = result["answer_box"]["snippet"]
    elif (
        "answer_box" in result.keys()
        and "snippet_highlighted_words" in result["answer_box"].keys()
    ):
        answer = (
            answer
            + result["answer_box"]["snippet_highlighted_words"][0]
            + " "
            + result["answer_box"]["snippet_highlighted_words"][1]
        )
    elif "snippet" in result["organic_results"][0].keys():
        answer = (
            answer
            + result["organic_results"][0]["snippet"]
            + " "
            + result["organic_results"][1]["snippet"]
        )
    else:
        answer = None

    return answer


def google(question):
    params = {
        "api_key": SERPAPI_KEY,
        "engine": "google",
        "q": question,
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en",
    }

    search = GoogleSearch(params)
    result = search.get_dict()

    if "answer_box" in result.keys() and "answer" in result["answer_box"].keys():
        answer = result["answer_box"]["answer"]
    elif "answer_box" in result.keys() and "snippet" in result["answer_box"].keys():
        answer = result["answer_box"]["snippet"]
    elif (
        "answer_box" in result.keys()
        and "snippet_highlighted_words" in result["answer_box"].keys()
    ):
        answer = result["answer_box"]["snippet_highlighted_words"][0]
    elif "snippet" in result["organic_results"][0].keys():
        answer = result["organic_results"][0]["snippet"]
    else:
        answer = None

    return answer


def grounding(question_list):
    grounded_answers = []
    for questions in tqdm(question_list, total=len(question_list)):
        temp = []
        for q in questions:
            try:
                print(q)
                ga = google(q)
                # ga = google(f"en.wikipedia.org {q}")
                # print(ga)
                temp.append(ga)
                # print(temp)
            except:
                ga = None
                temp.append(ga)
                continue
        grounded_answers.append(temp)
        # print(grounded_answers)
    return grounded_answers


def sanity_check(df, index):
    print(df.iloc[index]["claim"])
    print("=" * 20)
    print(df.iloc[index]["label"])
    print("=" * 20)
    print(df.iloc[index]["predicates"])
    print("=" * 20)
    for i in df.iloc[index]["questions"]:
        print(i)
    print("=" * 20)
    for i in df.iloc[index]["answers"]:
        print(i)
    print("=" * 20)
    for i in df.iloc[index]["grounded_answers"]:
        print(i)


if __name__ == "__main__":
    if args.dataset == "hover":
        if not os.path.exists(f"./HoVerDev/out/grounding"):
            os.makedirs(f"./HoVerDev/out/grounding")

        with open(
            f"./HoVerDev/out/decompose/{args.model}_decompose_{args.prompt_strategy}_{args.hover_num_hop}_{args.version}.json"
        ) as f1:
            df = pd.read_json(f1)
        # print(df)

        """ Trim """
        new_response = trim(df["response"])
        df["new_response"] = new_response

        """ Extract """
        if args.prompt_strategy == "cot":
            questions, answers = extract_response(df["new_response"])
            df["questions"] = questions
            df["answers"] = answers

        if args.prompt_strategy != "cot":
            predicates, questions, answers = extract_response(df["new_response"])
            df["predicates"] = predicates
            df["questions"] = questions
            df["answers"] = answers

        """ Grounding """
        grounded_answers = grounding(df["questions"])
        df["grounded_answers"] = grounded_answers
        print(df["grounded_answers"])
        print("Finish Getting Knowledge-grounded answers!")
        df.to_pickle(
            f"./HoVerDev/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.hover_num_hop}_{args.version}.pkl"
        )

        """ Sanity Check """
        df = pd.read_pickle(
            f"./HoVerDev/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.hover_num_hop}_{args.version}.pkl"
        )
        # sanity_check(df, 69)

    if args.dataset == "feverous":
        if not os.path.exists(f"./FeverousDev/out/grounding"):
            os.makedirs(f"./FeverousDev/out/grounding")

        with open(
            f"./FeverousDev/out/decompose/{args.model}_decompose_{args.prompt_strategy}_{args.feverous_challenge}_{args.version}.json"
        ) as f1:
            df = pd.read_json(f1)
        # print(df)

        """ Trim """
        new_response = trim(df["response"])
        df["new_response"] = new_response

        """ Extract """
        if args.prompt_strategy == "cot":
            questions, answers = extract_response(df["new_response"])
            df["questions"] = questions
            df["answers"] = answers

        if args.prompt_strategy != "cot":
            predicates, questions, answers = extract_response(df["new_response"])
            df["predicates"] = predicates
            df["questions"] = questions
            df["answers"] = answers

        """ Grounding """
        grounded_answers = grounding(df["questions"])
        df["grounded_answers"] = grounded_answers
        print(df["grounded_answers"])
        print("Finish Getting Knowledge-grounded answers!")
        df.to_pickle(
            f"./FeverousDev/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.feverous_challenge}_{args.version}.pkl"
        )

        """ Sanity Check """
        df = pd.read_pickle(
            f"./FeverousDev/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.feverous_challenge}_{args.version}.pkl"
        )
        # sanity_check(df, 69)

    if args.dataset == "scifact":
        if not os.path.exists(f"./SciFact-Open/out/grounding"):
            os.makedirs(f"./SciFact-Open/out/grounding")

        with open(
            f"./SciFact-Open/out/decompose/{args.model}_decompose_{args.prompt_strategy}_{args.version}.json"
        ) as f1:
            df = pd.read_json(f1)
        # print(df)

        """ Trim """
        new_response = trim(df["response"])
        df["new_response"] = new_response

        """ Extract """
        if args.prompt_strategy == "cot":
            questions, answers = extract_response(df["new_response"])
            df["questions"] = questions
            df["answers"] = answers

        if args.prompt_strategy != "cot":
            predicates, questions, answers = extract_response(df["new_response"])
            df["predicates"] = predicates
            df["questions"] = questions
            df["answers"] = answers

        """ Grounding """
        grounded_answers = grounding(df["questions"])
        df["grounded_answers"] = grounded_answers
        print(df["grounded_answers"])
        print("Finish Getting Knowledge-grounded answers!")
        df.to_pickle(
            f"./SciFact-Open/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.version}.pkl"
        )

        """ Sanity Check """
        df = pd.read_pickle(
            f"./SciFact-Open/out/grounding/{args.model}_grounded_{args.prompt_strategy}_{args.version}.pkl"
        )
        # sanity_check(df, 69)

        print("Finish grounding!")
