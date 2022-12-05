# 2022-12-05
# Move crates
from collections import namedtuple

FNAME_IN = "data/day05.txt"

Instruction = namedtuple("Instruction", "reps fr to")


def parse_header_line(line, spacing=4) -> list:
    return [line[i : i + 4].strip().strip("[]") for i in range(0, len(line), spacing)]


# line = "                    [L]     [H] [W]"


def parse_instruction(line):
    line = line.split()
    line = [(line[i], line[i + 1]) for i in range(0, len(line), 2)]
    line = {key: int(number) for key, number in line}
    return line


# line = "move 1 from 2 to 3"
# parse_instruction(line)

##############
### Parse File

in_instructions_part = False

stacks = list()
instructions = list()

with open(FNAME_IN) as f:
    for line in f:
        if not in_instructions_part:
            line = line[:-1]
            if not line:
                in_instructions_part = True
                continue
            row = parse_header_line(line)
            stacks.append(row)
            continue
        # instruction
        instruction = parse_instruction(line)
        instruction = Instruction(*instruction.values())
        instructions.append(instruction)

_stacks = {int(k): list() for k in stacks.pop()}

while stacks:
    row = stacks.pop()
    for i, crate in enumerate(row, start=1):
        if crate:
            _stacks[i].append(crate)

if not stacks:
    stacks = _stacks
    del _stacks

# Copy for part 2
stacks_raw = dict({k: list(l) for k, l in stacks.items()})

##########
### Part 1
for instruction in instructions:
    for _ in range(instruction.reps):
        crate = stacks[instruction.fr].pop()
        stacks[instruction.to].append(crate)

msg = [stack[-1] for stack in stacks.values()]
msg = "".join(msg)
print(f"top crates CreateMover 9000: {msg}")

##########
### Part 2
stacks = stacks_raw

for instruction in instructions:
    stacks[instruction.fr], crate = (
        stacks[instruction.fr][: -instruction.reps],
        stacks[instruction.fr][-instruction.reps :],
    )
    stacks[instruction.to].extend(crate)

msg = [stack[-1] for stack in stacks.values()]
msg = "".join(msg)
print(f"top crates CreateMover 9001: {msg}")
