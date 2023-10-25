from sklearn.metrics import classification_report, confusion_matrix
import json
import argparse
import os


def print_evaluation_results(predictions, gt_labels, num_of_classes=3):
    if num_of_classes == 3:
        target_names = ["refutes", "supports", "not enough info"]
        label_map = {"refutes": 0, "supports": 1, "not enough info": 2}
        labels = [label_map[e] for e in gt_labels]
        predictions = [label_map[e] for e in predictions]
        print(
            classification_report(
                labels, predictions, target_names=target_names, digits=4
            )
        )
        print(confusion_matrix(labels, predictions))
        print()
    elif num_of_classes == 2:
        # TODO
        # target_names = ['NOT_SUPPORTED', 'SUPPORTED']
        # label_map = {'NOT_SUPPORTED': 0, 'SUPPORTED': 1}

        target_names = ["REFUTES", "SUPPORTS"]
        label_map = {"REFUTES": 0, "SUPPORTS": 1}

        labels = [label_map[e] for e in gt_labels]
        predictions = [label_map[e] for e in predictions]
        print(
            classification_report(
                labels, predictions, target_names=target_names, digits=4
            )
        )
        print(confusion_matrix(labels, predictions))
        print()


def evaluate_feverous(result_file):
    with open(result_file, "r") as f:
        results = json.load(f)

    predictions = []
    gt_labels = []
    for sample in results:
        gt_labels.append(sample["gold"].strip())
        predictions.append(sample["prediction"].strip())

    print_evaluation_results(predictions, gt_labels, num_of_classes=2)


def parse_args():
    parser = argparse.ArgumentParser()
    # dataset args
    parser.add_argument("--dataset_name", type=str)
    parser.add_argument("--FV_data_path", type=str)
    parser.add_argument("--result_file", type=str)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    if args.dataset_name == "FEVEROUS":
        evaluate_feverous(args.result_file)
    else:
        raise NotImplementedError
