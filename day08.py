# build a tree house

# %%
import numpy as np
import itertools

FNAME = "data/day08.txt"

with open(FNAME) as f:
    data = []
    for line in f:
        row = [int(i) for i in line.strip()]
        data.append(row)

data = np.array(data)
N, M = data.shape
print(f"{N} Rows, {M} Columns")

# %%
# Part one:
out_trees = N * 2 + M * 2 - 4

inner_visible = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        top = data[:i, j].max()
        bottom = data[(i + 1) :, j].max()
        left = data[i, :j].max()
        right = data[i, (j + 1) :].max()
        edges = np.array([top, bottom, left, right])
        tree = data[i, j]
        visible = (edges < tree).any()

        inner_visible += visible

print(f"Total visible: {inner_visible+out_trees}")


# %%
# Part 2: Scenic tree score
def find_max(array, value):
    array = array >= tree
    if not array.sum():
        return len(array)
    else:
        return array.argmax() + 1


max_score = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        tree = data[i, j]
        top = find_max(data[:i, j][::-1], tree)
        bottom = find_max(data[(i + 1) :, j], tree)
        left = find_max(data[i, :j][::-1], tree)
        right = find_max(data[i, (j + 1) :], tree)

        score = bottom * top * left * right
        if score > max_score:
            max_score = score
            print(top, bottom, left, right)

print(f"Max score: {max_score}")
