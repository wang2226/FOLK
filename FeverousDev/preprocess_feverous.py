import os
import pandas as pd
import json

if not os.path.exists(f"./processed"):
    os.makedirs(f"./processed")

id_list, claim_list, label_list, challenge_list = [], [], [], []
with open(f"./raw/feverous_dev_challenges.jsonl") as f1:
    for line in f1:
        l = json.loads(line)
        id_list.append(l["id"])
        claim_list.append(l["claim"])
        label_list.append(l["label"])
        challenge_list.append(l["challenge"])

df = pd.DataFrame(
    list(zip(id_list, claim_list, label_list, challenge_list)),
    columns=["uid", "claim", "label", "challenge"],
)
# print(df)

num_support = len(df[df.label == "SUPPORTS"])
num_refutes = len(df[df.label == "REFUTES"])
num_not_enough_info = len(df[df.label == "NOT ENOUGH INFO"])

print(f"# SUPPORTED: {num_support}")
print(f"# REFUTES: {num_refutes}")
print(f"# NOT ENOUGH INFO: {num_not_enough_info}")

""" Multi-hop Reasoning """
# reasoning_df = df[df["challenge"] == "Multi-hop Reasoning"]
# reasoning_df = reasoning_df[reasoning_df.label !=
#                             "NOT ENOUGH INFO"].reset_index()

# support = reasoning_df[reasoning_df.label == "SUPPORTS"]
# refute = reasoning_df[reasoning_df.label == "REFUTES"]
# final_reasoning_df = pd.concat([support.sample(
#     50), refute.sample(50)], axis=0).reset_index()
# print(final_reasoning_df)
# final_reasoning_df.to_pickle(f"./processed/reasoning_df.pkl")

""" Numerical """
# numerical_df = df[df["challenge"] == "Numerical Reasoning"]
# numerical_df = numerical_df[numerical_df.label !=
#                             "NOT ENOUGH INFO"].reset_index()

# support = numerical_df[numerical_df.label == "SUPPORTS"]
# refute = numerical_df[numerical_df.label == "REFUTES"]
# final_numerical_df = pd.concat([support.sample(
#     50), refute.sample(50)], axis=0).reset_index()
# print(final_numerical_df)
# final_numerical_df.to_pickle(f"./processed/numerical_df.pkl")

""" Combining Tables and Text """
# table_df = df[df["challenge"] == "Combining Tables and Text"]
# table_df = table_df[table_df.label !=
#                     "NOT ENOUGH INFO"].reset_index()

# support = table_df[table_df.label == "SUPPORTS"]
# refute = table_df[table_df.label == "REFUTES"]
# final_table_df = pd.concat([support.sample(
#     50), refute.sample(50)], axis=0).reset_index()
# print(final_table_df)
# final_table_df.to_pickle(f"./processed/table_df.pkl")

print("Finished Preprocessing!")
