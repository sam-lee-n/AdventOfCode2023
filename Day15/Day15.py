import re
from collections import defaultdict


def decode(char, current_value=0):
    return (int(ord(char)) + current_value) * 17 % 256


def hash(code):
    current_value = 0
    for char in code:
        current_value = decode(char, current_value)
    return current_value


# Part 1
with open("input.txt") as f:
    lines = f.readlines()

sequence = [x for x in lines[0].strip().split(",")]
print("Part 1:", sum([hash(x) for x in sequence]))

lens_boxes = defaultdict(list)

for code in sequence:
    box, lens = re.split("=|-", code)
    box_h = hash(box)
    if "=" in code:
        lens = int(lens)
        for i, char in enumerate(lens_boxes[f"Box {box_h}"]):
            if char[0] == box:
                lens_boxes[f"Box {box_h}"][i] = [box, lens]
                break
        else:
            lens_boxes[f"Box {box_h}"].append([box, lens])
    elif "-" in code:
        if lens_boxes[f"Box {box_h}"]:
            for i, char in enumerate(lens_boxes[f"Box {box_h}"]):
                if char[0] == box:
                    lens_boxes[f"Box {box_h}"].pop(i)
                    break

lens_power = 0
for key in lens_boxes.keys():
    if len(lens_boxes[key]) > 0:
        box_power = 0
        for i, lens in enumerate(lens_boxes[key], 1):
            box_power += i * lens[1] * (int(key.split(" ")[1]) + 1)
        lens_power += box_power
print("Part 2:", lens_power)
