import re

with open("input.txt") as f:
    lines = f.readlines()

# Part 1
total = 0
for line in lines:
    my_num, winning_num = line.split(":")[1].split("|")
    score = 0
    for num in re.findall(r"\d+", my_num):
        if num in re.findall(r"\d+", winning_num):
            score += 1
    if score > 0:
        total += 2 ** (score - 1)

print("Part1 :", total)

# Part 2
card_list = [1 for a in range(len(lines))]
for line in lines:
    game, nums = line.split(":")
    game = int(re.findall(r"\d+", game)[0])
    my_num, winning_num = nums.split("|")

    num_of_wins = 0
    for num in re.findall(r"\d+", my_num):
        if num in re.findall(r"\d+", winning_num):
            num_of_wins += 1
    for x in range(num_of_wins):
        if game + x < len(card_list):
            card_list[game + x] += card_list[game - 1]

print("Part2 :", sum(card_list))
