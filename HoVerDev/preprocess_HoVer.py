import os
import pandas as pd
import numpy as np
import json
from sklearn.model_selection import StratifiedShuffleSplit

if not os.path.exists(f"./processed"):
    os.makedirs(f"./processed")

with open(f"./raw/hover_dev_release_v1.1.json") as f1:
    df = pd.read_json(f1)
print(df)

num_support = len(df[df.label == "SUPPORTED"])
num_not_support = len(df[df.label == "NOT_SUPPORTED"])
print(f"# SUPPORTED: {num_support}")
print(f"# NOT_SUPPORTED: {num_not_support}")

two_hop_df = df[df["num_hops"] == 2]
three_hop_df = df[df["num_hops"] == 3]
four_hop_df = df[df["num_hops"] == 4]

""" Two hop"""
# two_hop_support = two_hop_df[two_hop_df.label == "SUPPORTED"]
# two_hop_not_support = two_hop_df[two_hop_df.label == "NOT_SUPPORTED"]
# final_two_hop_df = pd.concat([two_hop_support.sample(
#     50), two_hop_not_support.sample(50)], axis=0).reset_index()
# print(final_two_hop_df)
# final_two_hop_df.to_pickle(f"./processed/two_hop_df.pkl")

""" Three hop """
# three_hop_support = three_hop_df[three_hop_df.label == "SUPPORTED"]
# three_hop_not_support = three_hop_df[three_hop_df.label == "NOT_SUPPORTED"]
# final_three_hop_df = pd.concat([three_hop_support.sample(
#     50), three_hop_not_support.sample(50)], axis=0).reset_index()
# print(final_three_hop_df)
# final_three_hop_df.to_pickle(f"./processed/three_hop_df.pkl")

""" Four hop """
# four_hop_support = four_hop_df[four_hop_df.label == "SUPPORTED"]
# four_hop_not_support = four_hop_df[four_hop_df.label == "NOT_SUPPORTED"]
# final_four_hop_df = pd.concat([four_hop_support.sample(
#     50), four_hop_not_support.sample(50)], axis=0).reset_index()
# print(final_four_hop_df)
# final_four_hop_df.to_pickle(f"./processed/four_hop_df.pkl")

""" Stratified Two Hop """
# # define total sample size desired
# N = 100
# final_two_hop_df = two_hop_df.groupby("label", group_keys=False).apply(
#     lambda x: x.sample(int(np.rint(N*len(x)/len(two_hop_df))))).sample(frac=1).reset_index(drop=True)
# print(final_two_hop_df)
# num_support = len(final_two_hop_df[final_two_hop_df.label == "SUPPORTED"])
# num_not_support = len(
#     final_two_hop_df[final_two_hop_df.label == "NOT_SUPPORTED"])
# print(f"# SUPPORTED: {num_support}")
# print(f"# NOT_SUPPORTED: {num_not_support}")
# final_two_hop_df.to_pickle("./processed/two_hop_df_new.pkl")
# final_two_hop_df.to_json("./processed/two_hop_df_new.json", orient="records")

""" Stratified Three Hop """
# # define total sample size desired
# N = 100
# final_three_hop_df = three_hop_df.groupby("label", group_keys=False).apply(
#     lambda x: x.sample(int(np.rint(N*len(x)/len(three_hop_df))))).sample(frac=1).reset_index(drop=True)
# print(final_three_hop_df)
# num_support = len(final_three_hop_df[final_three_hop_df.label == "SUPPORTED"])
# num_not_support = len(
#     final_three_hop_df[final_three_hop_df.label == "NOT_SUPPORTED"])
# print(f"# SUPPORTED: {num_support}")
# print(f"# NOT_SUPPORTED: {num_not_support}")
# final_three_hop_df.to_pickle(f"./processed/three_hop_df_new.pkl")
# final_three_hop_df.to_json("./processed/three_hop_df_new.json", orient="records")

""" Stratified Four Hop """
# # define total sample size desired
# N = 100
# final_four_hop_df = four_hop_df.groupby("label", group_keys=False).apply(
#     lambda x: x.sample(int(np.rint(N*len(x)/len(four_hop_df))))).sample(frac=1).reset_index(drop=True)
# print(final_four_hop_df)
# num_support = len(final_four_hop_df[final_four_hop_df.label == "SUPPORTED"])
# num_not_support = len(
#     final_four_hop_df[final_four_hop_df.label == "NOT_SUPPORTED"])
# print(f"# SUPPORTED: {num_support}")
# print(f"# NOT_SUPPORTED: {num_not_support}")
# final_four_hop_df.to_pickle(f"./processed/four_hop_df_new.pkl")
# final_four_hop_df.to_json("./processed/four_hop_df_new.json", orient="records")

print("Finished Preprocessing!")
