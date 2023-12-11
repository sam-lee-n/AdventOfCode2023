import re
from itertools import combinations

with open("input.txt") as f:
    lines = f.readlines()

# Part 1
space = []
for line in lines:
    space.append(line.strip())

galaxy_pre_list = []
for i, line in enumerate(space):
    for galaxy in re.finditer(r"#", line):
        galaxy_pre_list.append((i, galaxy.start()))

empty_rows = []
for i, line in enumerate(space):
    if "#" not in line:
        empty_rows.append(i)
for i in empty_rows[::-1]:
    space.insert(i, "." * len(space[0]))

empty_cols = []
for j in range(len(space[0])):
    col = "".join([x[j] for x in space])
    if "#" not in col:
        empty_cols.append(j)
for j in empty_cols[::-1]:
    for i, col in enumerate(space):
        space[i] = col[:j] + "." + col[j:]

galaxy_list = []
for i, line in enumerate(space):
    for galaxy in re.finditer(r"#", line):
        galaxy_list.append((i, galaxy.start()))

dist = []
for pair in combinations(galaxy_list, 2):
    dist.append(abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]))
print("Part 1:", sum(dist))

# Part 2
dist = []
expand = 1000000
for pair in combinations(galaxy_pre_list, 2):
    dist.append(
        abs(pair[0][0] - pair[1][0])
        + abs(pair[0][1] - pair[1][1])
        + (expand - 1)
        * len(
            set(empty_rows)
            & set(range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0]) + 1))
        )
        + (expand - 1)
        * len(
            set(empty_cols)
            & set(range(min(pair[0][1], pair[1][1]), max(pair[0][1], pair[1][1]) + 1))
        )
    )
print("Part 2:", sum(dist))
