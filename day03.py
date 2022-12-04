# Backpack items priorities
# 2022-12-04 - quiz 01
from collections import namedtuple
import string

FNAME_IN = "data/day03.txt"

Compartments = namedtuple("Backpack", "first second")

# Load data

backpacks = list()
# read file to dict
with open(FNAME_IN) as f:
    for line in f:
        line = line.strip()
        assert len(line) % 2 == 0, "Assumption not met"
        pos_half = len(line) // 2
        first, second = line[:pos_half], line[pos_half:]
        assert len(first) == len(second)
        backpacks.append(Compartments(first, second))

### priorites loop-up
priority = {
    letter: priority for priority, letter in enumerate(string.ascii_letters, start=1)
}

assert priority["L"] == 38

##########################################################################################
### Part 1
total = 0
for compartments in backpacks:
    shared = set(compartments.first).intersection(compartments.second)
    assert len(shared) == 1, f"More than one item shared: {shared}"
    total += priority[shared.pop()]

print(f"Total sum of priorities: {total}")

##########################################################################################
### Part 2

total = 0
for group in [backpacks[idx:idx+3] for idx in range(0, len(backpacks), 3)]:
    shared = set(string.ascii_letters)
    for compartments in group:
        shared = shared.intersection(compartments.first + compartments.second)
    assert len(shared) == 1, f"More than one item shared: {shared}"
    total += priority[shared.pop()]

print(f"Total sum of group priorities: {total}")