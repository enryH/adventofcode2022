# 2022-12-04

FNAME_IN = "data/day04.txt"

def get_range(s):
     start, end = map(int, s.split('-'))
     return range(start, end+1)

data = list()

overlaps = 0

with open(FNAME_IN) as f:
    for line in f:
        line = line.strip()
        first, second = map(set, map(get_range, line.split(',')))
        data.append((first, second, line))
        
        len_min = min(len(first), len(second))
        overlap = first.intersection(second)
        if len_min == len(overlap):
            print(f"{line} -- {min(overlap)}-{max(overlap)}")
            overlaps += 1

print(f"Total entire overlaps: {overlaps}")


### Part 2
overlaps = 0
for first, second, line in data:
        overlap = first.intersection(second)
        if overlap:
            print(f"{line} -- {min(overlap)}-{max(overlap)}")
            overlaps += 1

print(f"Total rows with any overlap: {overlaps}")