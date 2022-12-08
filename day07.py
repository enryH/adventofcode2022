# File system: Folder sizes and identification
# %%
from collections import defaultdict

# dict represents a folder
# if value is a dict -> key is a subfolder
# if value is an int -> key is a file

FNAME = "data/day07.txt"


## Parse data

with open(FNAME) as f:
    for line in f:
        if line.startswith("$ cd /"):
            folder_tree = {}
            parent_folders = list()
            current_folder = folder_tree
            print("Root folder")
            continue
        elif line.startswith("$ cd .."):
            current_folder = parent_folders.pop()
        elif line.startswith("$ cd"):
            change_to_folder = line.split("$ cd ")[-1].strip()
            parent_folders.append(current_folder)
            current_folder = current_folder[change_to_folder]
        elif line.startswith("$ ls"):
            # current_folder = []
            continue
        elif line.startswith("dir"):
            _, folder = line.split()
            current_folder[folder] = dict()
        else:
            fsize, fname = line.split()
            fsize = int(fsize)
            current_folder[fname] = fsize


# %%
folder_sizes = dict()

def count_folder_size(folder: dict, up_to_size=10000, parent=""):
    """Can count files more than once."""
    total = 0
    for name, obj in folder.items():
        if isinstance(obj, dict):
            size = count_folder_size(obj, parent=f"{parent}/{name}")
            folder_sizes[f"{parent}/{name}"] = size
            total += size
        else:
            total += obj
    return total


# test_case = {'fhqjzf':
#      {'fnnbrlc': {'dnbmm.ngb': 156413, 'zbfnjnnz.csg': 30790},
#       'hzqlb': {'cgzrdpr': 267451,
#                 'nfngbl.mcn': 77460,
#                 'plw.frm': 205978,
#                 'sjw.ctb': 66224,
#                 'zgwwvb.pcs': 212873},
#     'pcg.wnr': 254128,
#     'plw.frm': 168008,
#     'vwgvd': {'phdbz.tmc': 161177},
#     'zhq': {'hchlgv': {'dnbmm': {'pcg.wnr': 150415},
#                        'hcpnwbd': 270943,
#                         'hzqlb': {'qcvwtfg.wrl': 44475},
#                         'wdljw.cgn': 13433},
#             'rfngrlz.zzr': 218946,
#             'zhq': {'ggndpjzp.rpz': 155076}}},
#     'teada': 1234}

# _ = count_folder_size(test_case)
# folder_sizes

total_disk_space_used = count_folder_size(folder_tree)
folder_sizes

# %%
### Part one
total = 0
for name, size in folder_sizes.items():
    if size <= 100000:
        total += size

print(f"Total file sizes: {total}")


# %%
### part 2

to_free = 30000000 - (70000000 - total_disk_space_used)
candidates = []
for name, size in folder_sizes.items():
    if size >= to_free:
        candidates.append(size)

print(f"Minimum size: {min(candidates)}")

