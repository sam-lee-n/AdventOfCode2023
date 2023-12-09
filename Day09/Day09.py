import re


def get_next_number(input, direction=1):
    diff = [j - i for i, j in zip(input[:-1], input[1:])]
    if all(x == 0 for x in diff):
        return input[-1]
    else:
        return input[-1] + get_next_number(diff)


def get_prev_number(input):
    diff = [j - i for i, j in zip(input[:-1], input[1:])]
    if all(x == 0 for x in diff):
        return input[0]
    else:
        return input[0] - get_prev_number(diff)


with open("input.txt") as f:
    lines = f.readlines()

# Part 1
inputs = []
for line in lines:
    inputs.append([int(x) for x in re.findall(r"-?\d+", line)])

print("Part 1:", sum([get_next_number(x) for x in inputs]))

# Part 2
print("Part 2:", sum([get_prev_number(x) for x in inputs]))
