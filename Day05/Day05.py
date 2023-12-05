import re
import time
from collections import defaultdict

start = time.time()
with open("input.txt") as f:
    lines = f.readlines()

# Part 1
seeds = [int(x) for x in re.findall(r"\d+", lines[0])]
map_type = "Seed"
maps = defaultdict(list)

for line in lines:
    if "-to-" in line:
        map_type = line.split(" ")[0]

    if re.match(r"\d+", line):
        maps[map_type].append([int(x) for x in re.findall(r"\d+", line)])

for key in maps.keys():
    for i in range(len(seeds)):
        remapped = False
        for converter in maps[key]:
            if converter[1] <= seeds[i] < converter[1] + converter[2] + 1:
                seeds[i] += converter[0] - converter[1]
                remapped = True
                break
        if not remapped:
            seeds[i]

print("Part 1:", min(seeds))

# Part 2
seeds_pair = []
loc_pair = []
seeds = [int(x) for x in re.findall(r"\d+", lines[0])]
for i in range(0, len(seeds), 2):
    seeds_pair.append([seeds[i], seeds[i + 1] + seeds[i]])

for key in maps.keys():
    next_seeds_pair = []
    for seed in seeds_pair:
        for converter in maps[key]:
            # print ("start", seeds_pair, seed, converter, "!!!!!!!", next_seeds_pair)
            offset = converter[0] - converter[1]
            if seed[1] < converter[1] or seed[0] > converter[1] + converter[2]:
                continue
            new_range = [
                max(seed[0], converter[1]),
                min(seed[1], converter[1] + converter[2]),
            ]
            left_gap = [seed[0], new_range[0]]
            right_gap = [new_range[1], seed[1]]
            if left_gap[1] > left_gap[0]:
                seeds_pair.append(left_gap)
            if right_gap[1] > right_gap[0]:
                seeds_pair.append(right_gap)
            next_seeds_pair.append([new_range[0] + offset, new_range[1] + offset])
            break
        else:
            next_seeds_pair.append(seed)
        seeds_pair = next_seeds_pair
    # print("End:", seeds_pair, key)

print("Part 2:", min([x[0] for x in seeds_pair]))
