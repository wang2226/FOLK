import os
import pandas as pd
import numpy as np
import json

if not os.path.exists(f"./processed"):
    os.makedirs(f"./processed")

id_list, claim_list, label_list = [], [], []
with open(f"./raw/claims.jsonl") as f1:
    for index, line in enumerate(f1):
        l = json.loads(line)
        temp = []
        for i in l["evidence"]:
            temp.append(l["evidence"][i]["label"])
        if temp != [] and all(element == temp[0] for element in temp):
            # print(temp)
            id_list.append(l["id"])
            claim_list.append(l["claim"])
            label_list.append(temp[0])

assert len(id_list) == len(claim_list) == len(label_list)

df = pd.DataFrame(
    list(zip(id_list, claim_list, label_list)), columns=["uid", "claim", "label"]
)
print(df)
df.to_pickle(f"./processed/scifact_df.pkl")

# define total sample size desired
N = 100
final_df = (
    df.groupby("label", group_keys=False)
    .apply(lambda x: x.sample(int(np.rint(N * len(x) / len(df)))))
    .sample(frac=1)
    .reset_index(drop=True)
)
print(final_df)
num_support = len(final_df[final_df.label == "SUPPORT"])
num_not_support = len(final_df[final_df.label == "CONTRADICT"])
print(f"# SUPPORTED: {num_support}")
print(f"# NOT_SUPPORTED: {num_not_support}")
final_df.to_pickle("./processed/df_new.pkl")
final_df.to_json("./processed/df_new.json", orient="records")

print("Finished Preprocessing!")
