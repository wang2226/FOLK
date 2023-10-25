import pandas as pd

reasoning_df = pd.read_pickle("./processed/reasoning_df.pkl")
reasoning_df.to_json("./processed/reasoning_df.json", orient="records")
numerical_df = pd.read_pickle("./processed/numerical_df.pkl")
numerical_df.to_json("./processed/numerical_df.json", orient="records")
table_df = pd.read_pickle("./processed/table_df.pkl")
table_df.to_json("./processed/table_df.json", orient="records")