# %%
from collections import namedtuple

FNAME = "data/day09.txt"

Move = namedtuple("Move", "direction, steps")

moves = []
with open(FNAME) as f:
    for line in f:
        direction, steps = line.strip().split()
        move = Move(direction, int(steps))
        moves.append(move)

test_moves = [
    ("R", 4),
    ("U", 4),
    ("L", 3),
    ("D", 1),
    ("R", 4),
    ("D", 1),
    ("L", 5),
    ("R", 2),
]

test_moves = [Move(d, s) for d, s in test_moves]

moves[:10]
# %%
import math


def too_far(position_head, position_tail):
    distance = math.sqrt(
        (position_head[0] - position_tail[0]) ** 2
        + (position_head[1] - position_tail[1]) ** 2
    )
    if distance >= 2:
        return True
    else:
        return False


print(too_far((0, 0), (0, 2)))
print(too_far((-1, 0), (0, -2)))


def same_row_or_column(position_head, position_tail):
    if position_tail[0] == position_head[0] or position_tail[1] == position_head[1]:
        return True
    else:
        return False


print(same_row_or_column((0, 0), (0, 2)))
print(same_row_or_column((-1, 0), (0, -2)))

# %%
# Assume same starting point
head = (0, 0)
positions_head = [
    head,
]

tail = (0, 0)
positions_tail = [
    tail,
]

move_fct = {
    "U": lambda x: (x[0], x[1] + 1),
    "D": lambda x: (x[0], x[1] - 1),
    "L": lambda x: (x[0] - 1, x[1]),
    "R": lambda x: (x[0] + 1, x[1]),
}

# return new tail position for diagonal moves based on head movement
align_tail = {
    "U": lambda x: (x[0], x[1] - 1),
    "D": lambda x: (x[0], x[1] + 1),
    "L": lambda x: (x[0] + 1, x[1]),
    "R": lambda x: (x[0] - 1, x[1]),
}

for move in moves:
    for i in range(move.steps):
        head = move_fct[move.direction](head)
        positions_head.append(head)

        if too_far(head, tail):
            if same_row_or_column(head, tail):
                tail = move_fct[move.direction](tail)
            else:
                tail = align_tail[move.direction](head)
            positions_tail.append(tail)

list(zip(positions_head[-10:], positions_tail[-10:]))
# %%

print(f"Tail visited in total {len(set(positions_tail))}positions")  # 6190


# %%
# part 2
# figure out direction of movement
# if distance is too large
dist_move_map = {
    # same row and column
    (0, 2): (0, 1),
    (0, -2): (0, -1),
    (2, 0): (1, 0),
    (-2, 0): (-1, 0),
    # diagnonal cases
    # if the head and tail aren't touching
    # and aren't in the same row or column,
    # the tail always moves one step diagonally to keep up
    (2, 1): (1, 1),
    (1, 2): (1, 1),
    (-2, 1): (-1, 1),
    (-1, 2): (-1, 1),
    (2, -1): (1, -1),
    (1, -2): (1, -1),
    (-2, -1): (-1, -1),
    (-1, -2): (-1, -1),
    (2, 2): (1, 1),
    (-2, 2): (-1, 1),
    (2, -2): (1, -1),
    (-2, -2): (-1, -1),
}


def get_dist(position_head, position_tail):
    distance = (
        (position_head[0] - position_tail[0]),
        (position_head[1] - position_tail[1]),
    )
    return distance


# test_moves_large = [
#     ("R", 5),
#     ("U", 8),
#     ("L", 8),
#     ("D", 3),
#     ("R", 17),
#     ("D", 10),
#     ("L", 25),
#     ("U", 20),
# ]
# test_moves_large = [Move(d, s) for d, s in test_moves_large]


head = (0, 0)
positions_head = [
    head,
]
knods = [tuple(head)] * 9
positions_tail = [
    knods[-1],
]

for move in moves:
    for i in range(move.steps):
        head = move_fct[move.direction](head)
        positions_head.append(head)
        new_positions = []
        current_head = head
        for knod in knods:
            if too_far(current_head, knod):
                #     if same_row_or_column(head, tail):
                #         tail = move_fct[move.direction](tail)
                # else:
                #     tail = align_tail[move.direction](head)

                dist = get_dist(current_head, knod)
                x_move, y_move = dist_move_map[dist]
                knod = (knod[0] + x_move, knod[1] + y_move)
            new_positions.append(knod)
            current_head = knod

        positions_tail.append(new_positions[-1])
        knods = new_positions


print(f"Tail visited in total {len(set(positions_tail))} positions")

# %%
