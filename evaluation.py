import pandas as pd
import re
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from args import *


def extract_prediction(response):
    try:
        prediction = re.search("\[(.*?)\]", response).group(1)
        return prediction
    except:
        # print(response)
        # print("#" * 20)
        pass


def compute_accuracy(prediction_list, gold_list):
    correct = 0
    for prediction, gold in zip(prediction_list, gold_list):
        if prediction == gold:
            correct = correct + 1
    accuracy = correct / len(gold_list)
    return accuracy


if __name__ == "__main__":
    if args.dataset == "hover":
        with open(f"./HoVerDev/out/aggregate/{args.model}_aggregate_{args.prompt_strategy}_{args.hover_num_hop}_{args.version}.json") as f1:
            df = pd.read_json(f1)

        """ Print Label Distribution """
        # num_support = len(df[df.label == "SUPPORTED"])
        # num_not_support = len(df[df.label == "NOT_SUPPORTED"])
        # print(f"# SUPPORTED: {num_support}")
        # print(f"# NOT_SUPPORTED: {num_not_support}")

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

        print(f"Total # of predictions: {len(final_pred)}")

        acc = compute_accuracy(final_pred, final_gold)
        print(f"Accuracy: {acc: .2f}")

        target_names = ["NOT_SUPPORTED", "SUPPORTED"]
        label_map = {"NOT_SUPPORTED": 0, "SUPPORTED": 1}
        labels = [label_map[e] for e in final_gold]
        predictions = [label_map[e] for e in final_pred]
        print("Classification Report")
        print("=" * 60)
        print(classification_report(labels, predictions,
                                    target_names=target_names, digits=4))
        print(confusion_matrix(labels, predictions))

        """ Lookup Wrong """
        wrong = []
        for i in range(len(predictions)):
            if predictions[i] + labels[i] == 1:
                wrong.append(i)
        print("Got Wrong:")
        print(wrong)

    if args.dataset == "feverous":
        with open(f"./FeverousDev/out/aggregate/{args.model}_aggregate_{args.prompt_strategy}_{args.feverous_challenge}_{args.version}.json") as f1:
            df = pd.read_json(f1)

        remap = dict = {"SUPPORTS": "SUPPORTED", "REFUTES": "NOT_SUPPORTED"}
        df = df.replace({"label": remap})
        print(df)

        """ Print Label Distribution """
        num_support = len(df[df.label == "SUPPORTED"])
        num_not_support = len(df[df.label == "NOT_SUPPORTED"])
        print(f"# SUPPORTED: {num_support}")
        print(f"# NOT_SUPPORTED: {num_not_support}")

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

        print(f"Total # of predictions: {len(final_pred)}")

        acc = compute_accuracy(final_pred, final_gold)
        print(f"Accuracy: {acc: .2f}")

        target_names = ["NOT_SUPPORTED", "SUPPORTED"]
        label_map = {"NOT_SUPPORTED": 0, "SUPPORTED": 1}
        labels = [label_map[e] for e in final_gold]
        predictions = [label_map[e] for e in final_pred]
        print("Classification Report")
        print("=" * 60)
        print(classification_report(labels, predictions,
                                    target_names=target_names, digits=4))
        print(confusion_matrix(labels, predictions))

        """ Lookup Wrong """
        wrong = []
        for i in range(len(predictions)):
            if predictions[i] + labels[i] == 1:
                wrong.append(i)
        print("Got Wrong:")
        print(wrong)

    if args.dataset == "scifact":
        with open(f"./SciFact-Open/out/aggregate/{args.model}_aggregate_{args.prompt_strategy}_{args.version}.json") as f1:
            df = pd.read_json(f1)

        remap = dict = {"SUPPORT": "SUPPORTED", "CONTRADICT": "NOT_SUPPORTED"}
        df = df.replace({"label": remap})
        print(df)

        """ Print Label Distribution """
        num_support = len(df[df.label == "SUPPORTED"])
        num_not_support = len(df[df.label == "NOT_SUPPORTED"])
        print(f"# SUPPORTED: {num_support}")
        print(f"# NOT_SUPPORTED: {num_not_support}")

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

        print(f"Total # of predictions: {len(final_pred)}")

        acc = compute_accuracy(final_pred, final_gold)
        print(f"Accuracy: {acc: .2f}")

        target_names = ["NOT_SUPPORTED", "SUPPORTED"]
        label_map = {"NOT_SUPPORTED": 0, "SUPPORTED": 1}
        labels = [label_map[e] for e in final_gold]
        predictions = [label_map[e] for e in final_pred]
        print("Classification Report")
        print("=" * 60)
        print(classification_report(labels, predictions,
                                    target_names=target_names, digits=4))
        print(confusion_matrix(labels, predictions))

        """ Lookup Wrong """
        wrong = []
        for i in range(len(predictions)):
            if predictions[i] + labels[i] == 1:
                wrong.append(i)
        print("Got Wrong:")
        print(wrong)
