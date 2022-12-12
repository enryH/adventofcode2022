# %%
import numpy as np
from string import ascii_lowercase

letter_to_int = {letter: idx for idx, letter in enumerate(ascii_lowercase, start=1)}
letter_to_int["S"] = min(letter_to_int.values()) - 1
letter_to_int["E"] = max(letter_to_int.values()) + 1


test_grid = ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]

test_grid = [[letter_to_int[letter] for letter in row] for row in test_grid]
# keep track of options?
test_grid = np.array(test_grid)

# %%
# go down? (is possible, but then one needs to get back up again)

class Grid:
    def __init__(self, grid: np.array):
        self.start =  (
            np.argmin(grid) // grid.shape[-1],
            np.argmin(grid) % grid.shape[-1],
        )
        self.end = (
            np.argmax(grid) // grid.shape[-1],
            np.argmax(grid) % grid.shape[-1],
        )
        self.path = list()
        self.path.append(self.start)
        # self.current = self.start
        self.max_row, self.max_col = grid.shape
        self.grid = grid

    def get_options(self, current: tuple):
        row, col = current
        current_value = self.grid[row, col]
        options = list()
        if row > 0 and (self.grid[row -1, col] - current_value) <= 1:
            options.append((row - 1, col))
        if row < (self.max_row - 1) and (self.grid[row + 1, col] - current_value) <= 1:
            options.append((row + 1, col))
        if col > 0 and (self.grid[row, col - 1] - current_value) <= 1:
            options.append((row, col - 1))
        if col < (self.max_col - 1) and (self.grid[row, col + 1] - current_value) <= 1:
            options.append((row, col + 1))
        return options


# grid = Grid(test_grid)
# grid.get_options((0, 0))
# %%
from random import choice

grid = Grid(test_grid)

random_walks = list()

# random walk
for i in range(40):
    path = list()
    current = grid.start
    path.append(current)
    while current != grid.end:
        options = grid.get_options(current)
        options = [option for option in options if option not in path]
        if len(options) == 0:
            break
        current = choice(options)
        path.append(current)
    # print(path)
    if current == grid.end:
        random_walks.append(path)   
random_walks

# %%

# %%
# Load real data
FNAME_IN = 'data/day12.txt'
with open(file=FNAME_IN) as f:
    grid = f.read().splitlines()

grid = [[letter_to_int[letter] for letter in row] for row in grid]
# keep track of options?
grid = np.array(grid)
grid = Grid(grid)
grid.start, grid.end
# %%
# Part 1
# visit each node once
visited = set()
current = grid.start
last = grid.start
paths = list()
paths.append([grid.start])
solutions = list()
# while last not in visited:
while paths:
    path = paths.pop(0)
    last = path[-1]
    if last in visited:
        continue
    options = grid.get_options(path[-1])
    if options:
        for option in options:
            new_path = path + [option]
            if option not in path:
                paths.append(new_path)
            if option == grid.end:
                solutions.append(new_path)      
    visited.add(last)  
solutions

for solution in solutions:
    print(f"Steps: {len(solution)-1}")
# %%
# Part 2
# Explore all posssible starting options
