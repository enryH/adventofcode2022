# %%
%cd "C:\Users\sambra\Desktop\adventofcode2022"

# %%
# DAY1

top = [0,0,0]
curr = 0
with open("day1.txt") as f:
    for line in f:
        if line != '\n':
            curr += int(line)
        else:
            top.append(curr)
            top.remove(min(top))
            curr = 0
            
print(max(top), sum(top))

# %%
# DAY2

dic = {'A X':3+1,
       'A Y':6+2, 
       'A Z':0+3,
       'B X':0+1,
       'B Y':3+2,
       'B Z':6+3,
       'C X':6+1,
       'C Y':0+2,
       'C Z':3+3,}

dic2 = {'A X':0+3,
       'A Y':3+1, 
       'A Z':6+2,
       'B X':0+1,
       'B Y':3+2,
       'B Z':6+3,
       'C X':0+2,
       'C Y':3+3,
       'C Z':6+1,}

total=0
with open("day2.txt") as f:
    temp = f.read().splitlines()
    for line in temp: total += dic2[line]
        
print(total)

# %%
# Day3

with open("day3.txt") as f:
    temp = f.read().splitlines()

letters = [chr(n) for n in range(97,123)] + [chr(n) for n in range(65,91)]
score = dict(zip(letters, range(1,53)))

total=0
for line in temp:
    split = int(len(line)/2)
    bag1, bag2 = {x for x in line[:split]}, {x for x in line[split:]}
    value = bag1.intersection(bag2)
    total += score[max(value)]        

print(total)

group, total2 = [], 0
for i in range(0, len(temp), 3):
    set1, set2, set3 = {x for x in temp[i]}, {x for x in temp[i+1]},{x for x in temp[i+2]}
    total2 += score[max(set1.intersection(set2,set3))]

print(total2)        

# %%
#day4

with open("day4.txt") as f:
    temp = f.read().splitlines()

def flatten(S):
    if S == []: return S
    if isinstance(S[0], list): return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
    
within, overlap = 0,0
for line in temp:
    #part1
    tasks = flatten([x.split("-") for x in line.split(",")])
    tasks =[int(x) for x in tasks]
    set1, set2 = set(range(tasks[0], tasks[1]+1)), set(range(tasks[2], tasks[3]+1))
    
    if set1.intersection(set2) == set1 or set2.intersection(set1) == set2:
        within+=1
        
    #part2
    if set1.intersection(set2): overlap += 1
        
print(within, overlap)

 

# %%
#day5
with open("day5.txt") as f:
    temp = f.read().splitlines()
table = temp[:8]
instructions = temp[10:]
instructions = [[int(x.split()[i]) for i in (1,3,5)] for x in instructions]

#part1
import numpy as np
def extract_table(input_table):
    table = []
    for i in range(8):
        table.append([input_table[i][x] for x in range(1, len(input_table[i])+1,4)])
    
    table = [i[::-1] for i in np.array(table).T]
    for i in range(len(table)):
        table[i] = [x for x in table[i] if x != ' ']
    
    dic = {i+1:table[i] for i in range(0,len(table))}
    
    return dic

dic = extract_table(temp[:8])

def move_boxes(dic, num, start, end):
    for i in range(num):
        dic[end].append(dic[start].pop())
    return dic
    
for instruction in instructions:
    dic = move_boxes(dic, *instruction)

output=""
for key in dic.keys():
    output += dic[key].pop()
    
print(output)

#part 2
dic = extract_table(temp[:8])

def move_boxes2(dic, num, start, end):
    dic[end] += dic[start][-num:]
    dic[start] = dic[start][:-num]
    return dic
    
for instruction in instructions:
    dic = move_boxes2(dic, *instruction)

output=""
for key in dic.keys():
    output += dic[key].pop()
    
print(output)
    

# %%
# day6

with open("day6.txt") as f:
    code = f.read()

#part1
def find_non_repeat(length, seq):
    start = 0
    for i in range(len(seq)):
        if len(set(seq[i:i+length])) == length: return start+length
        start += 1

print(find_non_repeat(4, code))

#part2
print(find_non_repeat(14, code))

# %%
# day7

with open("day7.txt") as f:
    directory = f.read().splitlines()
    
# part1
path = "/"
directory_dic = {path:[]} 
# cdx = in, cd.. = out, cd/ = top
for i in directory:
    split = i.split()
    if split[0] == "$":
        if split[1] == "cd":
            if split[2] == "/": # move to top
                path = "/"
                
            elif split[2] == "..": # move out one level
                path = "_".join(path.split("_")[:-1])
                
            else: # move in one level to dir
                path += f"_{split[2]}" 
                            
        if split[1] == ["ls"]: # lists files in directory
            None
            
    elif split[0] == "dir": # add new directory
        new_path = f"{path}_{split[1]}"
        if new_path not in directory_dic.keys():
            directory_dic[new_path] = []
        
    else: # add file_size to directory and all parent directories
        file_size = int(split[0])
        
        places_to_add = ["_".join(path.split("_")[:i]) for i in range(1,len(path.split("_"))+1)]
        for place in places_to_add:
            if place not in directory_dic: directory_dic[place] = []
            directory_dic[place].append(file_size)
            
total = {key:sum(directory_dic[key]) for key in directory_dic if sum(directory_dic[key])}
print(sum([value for value in total.values() if value <= 100000]))

#part 2

total_space = 70000000
needed_free_space = 30000000
used_space = total["/"]
free_space = total_space - used_space

space_to_be_freed = needed_free_space - free_space

for i in sorted(total.values()):
    if i > space_to_be_freed:
        print(i)
        break

# %%
directory_dic


