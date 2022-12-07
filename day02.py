# Rock-Paper-Scissors
# 2022-12-04 - quiz 01

FNAME_IN = "data/day02.txt"

# read file to dict
with open(FNAME_IN) as f:
    data = [tuple(line.split()) for line in f]

# 'A B C',
# 'X Y Z',
# 'Rock Paper Scissors',

action_score = {k: v for k, v in zip("A B C X Y Z".split(), [1, 2, 3, 1, 2, 3])}

# '0 3 6', 'lost draw won'
win_loose = {
    # A
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    # B
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    # C
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}

amount = 0
for t in data:
    outcome = win_loose[t]
    outcome = outcome + action_score[t[1]]
    amount += outcome

print(f"Total quiz one: {amount}")

##########################################################################################
# Part two

# 'X Y Z', 'loose, draw, win'

action_map = {
    # A
    ("A", "X"): "Z",
    ("A", "Y"): "X",
    ("A", "Z"): "Y",
    # B
    ("B", "X"): "X",
    ("B", "Y"): "Y",
    ("B", "Z"): "Z",
    # C
    ("C", "X"): "Y",
    ("C", "Y"): "Z",
    ("C", "Z"): "X",
}

game_score = {k: v for k, v in zip("X Y Z".split(), [0, 3, 6])}

amount = 0
for t in data:
    action = action_map[t]
    amount += action_score[action]
    amount += game_score[t[1]]

print(f"Total quiz two: {amount}")

# Options:
# match statement
# if-else
