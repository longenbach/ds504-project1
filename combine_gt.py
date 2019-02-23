import os

import pandas as pd

dir_path = "./groundTruth"

files = os.listdir(dir_path)

df_list = []

for file in files:
    raw = pd.read_json(os.path.join(dir_path, file))
    valid = raw[raw["itemId"] != -1]
    df_list.append(valid)

all_valid = pd.concat(df_list)

all_valid.to_csv("allValidProducts.csv", index=False)
