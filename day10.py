# Signal strenghts

# %%
FNAME = "data/day10.txt"

parser = {"addx": lambda line: int(line[1]), "noop": lambda line: None}

with open(FNAME) as f:
    instructions = []
    for line in f:
        line = line.strip().split()
        instruction = line[0]
        instructions.append(parser[instruction](line))

instructions[:10]

# %%
# Part 1

cycle = 0
X = 1


def start_program(instructions):
    cycle = 0
    X = 1
    for instruction in instructions:
        cycle += 1
        if instruction:
            yield cycle, X
            cycle += 1
            yield cycle, X
            X += instruction
        else:
            yield cycle, X


test_instructions = [
    None,
    3,
    -5,
]
list(start_program(test_instructions))
# %%
test_instructions = [
    15,
    -11,
    6,
    -3,
    5,
    -1,
    -8,
    13,
    4,
    0,
    -1,
    5,
    -1,
    5,
    -1,
    5,
    -1,
    5,
    -1,
    -35,
    1,
    24,
    -19,
    1,
    16,
    -11,
    0,
    0,
    21,
    -15,
    0,
    0,
    -3,
    9,
    1,
    -3,
    8,
    1,
    5,
    0,
    0,
    0,
    0,
    0,
    -36,
    0,
    1,
    7,
    0,
    0,
    0,
    2,
    6,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    7,
    1,
    0,
    -13,
    13,
    7,
    0,
    1,
    -33,
    0,
    0,
    0,
    2,
    0,
    0,
    0,
    8,
    0,
    -1,
    2,
    1,
    0,
    17,
    -9,
    1,
    1,
    -3,
    11,
    0,
    0,
    1,
    0,
    1,
    0,
    0,
    -13,
    -19,
    1,
    3,
    26,
    -30,
    12,
    -1,
    3,
    1,
    0,
    0,
    0,
    -9,
    18,
    1,
    2,
    0,
    0,
    9,
    0,
    0,
    0,
    -1,
    2,
    -37,
    1,
    3,
    0,
    15,
    -21,
    22,
    -6,
    1,
    0,
    2,
    1,
    0,
    -10,
    0,
    0,
    20,
    1,
    2,
    2,
    -6,
    -11,
    0,
    0,
    0,
]

sum_signal = 0
keep_for = {20, 60, 100, 140, 180, 220}
for cycle, X in start_program(test_instructions):
    if cycle in keep_for:
        print(cycle, X, cycle * X)
        sum_signal += cycle * X

print(f"Total signal for requested cycles: {sum_signal}")

# %%
sum_signal = 0
keep_for = {20, 60, 100, 140, 180, 220}
for cycle, X in start_program(instructions):
    if cycle in keep_for:
        sum_signal += cycle * X
print(f"Total signal for requested cycles: {sum_signal}")


# %%
# Part 2
# sprite = 3 pixels
# X sets middle pixel position

# we go through one cycle of screen printing

CRT = []
# sprite_pos = 1

for pixel, (cycle, X) in zip(range(0,240),
                            start_program(instructions)):
    strite_pos = X
    pixel = pixel % 40
    if abs(X-pixel)<=1:
        CRT.append("#")
    else:
        CRT.append(".")


for i in range(0,240,40):
    # print(i)
    print("".join(CRT[i:i+40]))
# RBPARAGF