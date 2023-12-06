import re
from functools import reduce

with open("input.txt") as f:
    lines = f.readlines()

# Part 1
time = [int(x) for x in re.findall(r"\d+", lines[0])]
distance = [int(x) for x in re.findall(r"\d+", lines[1])]
win_condition = [0 for x in range(len(time))]

for i, t in enumerate(time):
    for j in range(t):
        travelled = (t - j) * j
        if travelled > distance[i]:
            win_condition[i] += 1
ans = reduce(lambda x, y: x * y, win_condition)
print("Part 1:", ans)

# Part 2
time = int("".join(re.findall(r"\d+", lines[0])))
distance = int("".join(re.findall(r"\d+", lines[1])))
win_condition = 0

for t in range(time):
    travelled = (time - t) * t
    if travelled > distance:
        win_condition += 1

print("Part 2:", win_condition)
