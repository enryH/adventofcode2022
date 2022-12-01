import numpy as np
import pandas as pd
# 2022-12-01 - quiz 01

FNAME_IN = 'data/day01.txt' 

# read file to dict
with open(FNAME_IN) as f:
    data = dict()
    name_template = "elve {:2d}"
    i = 1
    current_key = name_template.format(i)
    current_entry = list()
    for line in f:
        try:
            line = int(line)
            current_entry.append(line)
        except ValueError:
            data[current_key] = {i: e for i, e in enumerate(current_entry)}
            i += 1
            current_key = name_template.format(i)
            current_entry = list()

# DataFrame
data = pd.DataFrame(data)
print(data.iloc[:4, :4].to_string())

max_calories = data.sum().max()
print(f"Maximum calories: {max_calories}")

# mask = data.sum() == max_calories
# idx = mask.loc[mask].index
# display(data[idx])

top_3_calories = data.sum().nlargest(3)
print(top_3_calories.to_string() )
print(f"Top 3 calories summed: {top_3_calories.sum()}")
