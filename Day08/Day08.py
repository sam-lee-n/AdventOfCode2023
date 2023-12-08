import re
from collections import defaultdict
import math

with open("input.txt") as f:
    lines = f.readlines()

routes = lines[0].strip()
routes = routes.replace("L", "0")
routes = routes.replace("R", "1")

map = defaultdict(list)
for line in lines[2:]:
    values = re.findall(r"\w+", line)
    map[values[0]] = [values[1], values[2]]

current_location = "AAA"
steps = 0
while current_location != "ZZZ":
    next_step = int(routes[steps % (len(routes))])
    current_location = map[current_location][next_step]
    steps += 1

print("Part1 :", steps)

# Part 2
current_list = [x for x in map.keys() if x.endswith("A")]
steps = 0
ans = [None for x in current_list]
while not all([x.endswith("Z") for x in current_list]):
    next_step = int(routes[steps % (len(routes))])
    for i, loc in enumerate(current_list):
        current_list[i] = map[loc][next_step]
    steps += 1

    if any([x.endswith("Z") for x in current_list]):
        for i, x in enumerate(current_list):
            if not ans[i]:
                if x.endswith("Z"):
                    ans[i] = steps

    if all(ans):
        print("Found all")
        break

print("Part2 :", math.lcm(*ans))
