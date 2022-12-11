# Monkeys playing keep away
# %%
from dataclasses import dataclass

FNAME_IN = "data/day11.txt"


@dataclass
class Monkey:
    items: list
    operation: callable
    test: callable
    throw_to: dict



# %%
def get_test_monkeys():
    test_monkeys = [
        Monkey([79, 98], lambda x: x * 19, lambda x: x % 23 == 0, {True: 2, False: 3}),
        Monkey(
            [54, 65, 75, 74], lambda x: x + 6, lambda x: x % 19 == 0, {True: 2, False: 0}
        ),
        Monkey([79, 60, 97], lambda x: x * x, lambda x: x % 13 == 0, {True: 1, False: 3}),
        Monkey([74], lambda x: x + 3, lambda x: x % 17 == 0, {True: 0, False: 1}),
    ]
    return test_monkeys

test_monkeys = get_test_monkeys()

total = [0] * len(test_monkeys)

def play_round(monkeys):
    for i, monkey in enumerate(monkeys):
    # Monkey throws all items one after the other (after inspecting them)
        while monkey.items:
            item = monkey.items.pop(0)
            total[i] += 1
            level = monkey.operation(item)
            level = int(level / 3)  # round down
            give_to_monkey = monkey.throw_to[monkey.test(level)]
            monkeys[give_to_monkey].items.append(level)


for round in range(20):
    # Monkey play one at a time
    play_round(test_monkeys)
    print('#'* 20)
    print(f'# Round {round+1} #')
    for i, monkey in enumerate(test_monkeys):
        print(f"{i}: {monkey.items}")

print(total)

res = sorted(total)
print("Sorted: ", res)
print("Monkey business: ", res[-1] * res[-2])


with open(file=FNAME_IN) as f:
    monkeys = list()
    for line in f:
        line = line.strip()
        if line.startswith("Monkey"):
            new_monkey = list()
        elif not line:
            monkeys.append(new_monkey)
        else:
            new_monkey.append(line)
    monkeys.append(new_monkey)

# %%
# would have been better to do it manuelly
def process_monkey(monkey: list):
    parsed_monkey = [None] * 4
    parsed_monkey[0] = list(map(int, monkey[0].split(":")[-1].split(",")))
    if "+" in monkey[1]:
        parsed_monkey[1] = lambda x: x + int(monkey[1].split("+")[-1])
    elif "*" in monkey[1]:
        parsed_monkey[1] = lambda x: x * int(monkey[1].split("*")[-1])
    parsed_monkey[2] = lambda x: x % int(monkey[2].split("by")[-1]) == 0
    parsed_monkey[3] = {
        True: int(monkey[3].split("monkey")[-1]),
        False: int(monkey[4].split("monkey")[-1]),
    }

    return Monkey(*parsed_monkey)


monkeys = list(map(process_monkey, monkeys))

# would have been better to do it manuelly
monkeys[6] = Monkey(
    monkeys[6].items, lambda x: x * x, monkeys[6].test, monkeys[6].throw_to
)

# %%
# # test my data
# monkey = monkeys[0]
# monkey.test(8)

# assert monkey.throw_to[monkey.test(14)] == 6
# assert monkey.throw_to[monkey.test(8)] == 7
# assert monkey.operation(2) == 22
# assert monkeys[2].operation(6) == 14
# assert monkeys[6].operation(6) == 36

# %%
# Part 1: 20 rounds
total = [0] * len(monkeys)

for round in range(20):
    # Monkey play one at a time
    play_round(monkeys)

print(total)

res = sorted(total)
print("Sorted: ", res)
print("Monkey business: ", res[-1] * res[-2])


# %%
# Part 2: 10,000 rounds
# needs to be implemented in a more efficient way
@dataclass
class Monkey:
    items: list
    operation: callable
    mod: int
    throw_to: dict



# def get_test_monkeys():
#     test_monkeys = [
#         Monkey([79, 98], lambda x: x * 19, 23, {True: 2, False: 3}),
#         Monkey(
#             [54, 65, 75, 74], lambda x: x + 6, 19, {True: 2, False: 0}
#         ),
#         Monkey([79, 60, 97], lambda x: x * x, 13, {True: 1, False: 3}),
#         Monkey([74], lambda x: x + 3, 17, {True: 0, False: 1}),
#     ]
#     return test_monkeys

# monkeys = get_test_monkeys()    


with open(file=FNAME_IN) as f:
    monkeys = list()
    for line in f:
        line = line.strip()
        if line.startswith("Monkey"):
            new_monkey = list()
        elif not line:
            monkeys.append(new_monkey)
        else:
            new_monkey.append(line)
    monkeys.append(new_monkey)

# would have been better to do it manuelly
def process_monkey(monkey: list):
    parsed_monkey = [None] * 4
    parsed_monkey[0] = list(map(int, monkey[0].split(":")[-1].split(",")))
    if "+" in monkey[1]:
        parsed_monkey[1] = lambda x: x + int(monkey[1].split("+")[-1])
    elif "*" in monkey[1]:
        parsed_monkey[1] = lambda x: x * int(monkey[1].split("*")[-1])
    parsed_monkey[2] = int(monkey[2].split("by")[-1])
    parsed_monkey[3] = {
        True: int(monkey[3].split("monkey")[-1]),
        False: int(monkey[4].split("monkey")[-1]),
    }

    return Monkey(*parsed_monkey)


monkeys = list(map(process_monkey, monkeys))

# would have been better to do it manuelly
monkeys[6] = Monkey(
    monkeys[6].items, lambda x: x * x, monkeys[6].mod, monkeys[6].throw_to
)


total = [0] * len(monkeys)

from math import gcd

def play_round(monkeys):
    mod = 1
    for monkey in monkeys:
        # calculate a common denominator
        mod *= monkey.mod

    for i, monkey in enumerate(monkeys):
    # Monkey throws all items one after the other (after inspecting them)
        # map opteration to all items?
        for item in monkey.items:
            total[i] += 1
            level = monkey.operation(item)
            # level = int(level / 3)  # round down
            devisible = level % monkey.mod == 0
            give_to_monkey = monkey.throw_to[devisible]

            level = (level % mod) # keep level in range
            monkeys[give_to_monkey].items.append(level)
        monkey.items = list() # all thrown away


for round in range(10000): # this takes forever in the current implementation
    # Monkey play one at a time
    play_round(monkeys)
    if (round+1) in [1, 20, 1000, 2000, 3000, 6000, 10000]:
        print(f'== After round {round+1}  ==')
        for i, inspected_total in enumerate(total):
            print(f"Monkey {i}: {inspected_total}")
        print('#'* 20)


# %%
res = sorted(total)
print("Sorted: ", res)
print("Monkey business: ", res[-1] * res[-2])
# %%
