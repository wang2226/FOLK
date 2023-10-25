import pandas as pd
import re
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix


def extract_prediction(response):
    try:
        prediction = re.search("\[(.*?)\]", response).group(1)
        return prediction
    except:
        pass


def run_hover(df):
    """Get Prediction"""
    prediction_list = []
    for response in df["response"]:
        prediction = extract_prediction(response)
        prediction_list.append(prediction)

    gold_list = df["label"].to_list()
    final_pred, final_gold = [], []

    for i in range(len(prediction_list)):
        if prediction_list[i] == "SUPPORTED" or prediction_list[i] == "NOT_SUPPORTED":
            final_pred.append(prediction_list[i])
            final_gold.append(gold_list[i])

    target_names = ["NOT_SUPPORTED", "SUPPORTED"]
    label_map = {"NOT_SUPPORTED": 0, "SUPPORTED": 1}
    labels = [label_map[e] for e in final_gold]
    predictions = [label_map[e] for e in final_pred]
    print("Classification Report")
    print("=" * 60)
    print(
        classification_report(labels, predictions, target_names=target_names, digits=4)
    )
    print(confusion_matrix(labels, predictions))


def run_feverous(df):
    remap = dict = {"SUPPORTS": "SUPPORTED", "REFUTES": "NOT_SUPPORTED"}
    df = df.replace({"label": remap})

    """ Get Prediction """
    prediction_list = []
    for response in df["response"]:
        prediction = extract_prediction(response)
        prediction_list.append(prediction)

    gold_list = df["label"].to_list()
    final_pred, final_gold = [], []

    for i in range(len(prediction_list)):
        if prediction_list[i] == "SUPPORTED" or prediction_list[i] == "NOT_SUPPORTED":
            final_pred.append(prediction_list[i])
            final_gold.append(gold_list[i])

    target_names = ["NOT_SUPPORTED", "SUPPORTED"]
    label_map = {"NOT_SUPPORTED": 0, "SUPPORTED": 1}
    labels = [label_map[e] for e in final_gold]
    predictions = [label_map[e] for e in final_pred]
    print("Classification Report")
    print("=" * 60)
    print(
        classification_report(labels, predictions, target_names=target_names, digits=4)
    )
    print(confusion_matrix(labels, predictions))


def run_scifact(df):
    remap = dict = {"SUPPORT": "SUPPORTED", "CONTRADICT": "NOT_SUPPORTED"}
    df = df.replace({"label": remap})

    """ Get Prediction """
    prediction_list = []
    for response in df["response"]:
        prediction = extract_prediction(response)
        prediction_list.append(prediction)

    gold_list = df["label"].to_list()
    final_pred, final_gold = [], []

    for i in range(len(prediction_list)):
        if prediction_list[i] == "SUPPORTED" or prediction_list[i] == "NOT_SUPPORTED":
            final_pred.append(prediction_list[i])
            final_gold.append(gold_list[i])

    target_names = ["NOT_SUPPORTED", "SUPPORTED"]
    label_map = {"NOT_SUPPORTED": 0, "SUPPORTED": 1}
    labels = [label_map[e] for e in final_gold]
    predictions = [label_map[e] for e in final_pred]
    print("Classification Report")
    print("=" * 60)
    print(
        classification_report(labels, predictions, target_names=target_names, digits=4)
    )
    print(confusion_matrix(labels, predictions))


if __name__ == "__main__":
    print("\033[92m{}\033[00m".format("CoT HOVER Two Hop"))
    with open(f"./CoT/text-davinci_aggregate_cot_two_final.json") as f:
        two = pd.read_json(f)
    run_hover(two)

    print("\033[92m{}\033[00m".format("CoT HOVER Three Hop"))
    with open(f"./CoT/text-davinci_aggregate_cot_three_final.json") as f:
        three = pd.read_json(f)
    run_hover(three)

    print("\033[92m{}\033[00m".format("CoT HOVER Four Hop"))
    with open(f"./CoT/text-davinci_aggregate_cot_four_final.json") as f:
        four = pd.read_json(f)
    run_hover(four)

    print("\033[93m{}\033[00m".format("CoT FEVEROUS Numerical"))
    with open(f"./CoT/text-davinci_aggregate_cot_numerical_final.json") as f:
        numerical = pd.read_json(f)
    run_feverous(numerical)

    print("\033[93m{}\033[00m".format("CoT FEVEROUS Multi-Hop"))
    with open(f"./CoT/text-davinci_aggregate_cot_reasoning_final.json") as f:
        reasoning = pd.read_json(f)
    run_feverous(reasoning)

    print("\033[93m{}\033[00m".format("CoT FEVEROUS Text and Table"))
    with open(f"./CoT/text-davinci_aggregate_cot_table_final.json") as f:
        table = pd.read_json(f)
    run_feverous(table)

    print("\033[95m{}\033[00m".format("CoT SciFact"))
    with open(f"./CoT/text-davinci_aggregate_cot_scifact.json") as f:
        scifact = pd.read_json(f)
    run_scifact(scifact)
