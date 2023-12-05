with open("input.txt") as f:
    lines = f.readlines()

# Part 1
max_cubes = {"red": 12, "green": 13, "blue": 14}
sum_total = 0
for line in lines:
    game, cubes = line.split(":")

    passed = True
    # print(game, cubes.replace(";", ",").split(","))
    for cube in cubes.replace(";", ",").split(","):
        num, colour = cube.strip().split(" ")
        if max_cubes[colour] < int(num):
            passed = False
            break

    if passed:
        # print("!!!!",passed,game.split(" ")[1])
        sum_total += int(game.split(" ")[1])

print("Part 1:", sum_total)

# Part 2
sum_total = 0
for line in lines:
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    game, cubes = line.split(":")

    for cube in cubes.replace(";", ",").split(","):
        num, colour = cube.strip().split(" ")
        if int(num) > max_cubes[colour]:
            max_cubes[colour] = int(num)

    sum_total += max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]

print("Part 2:", sum_total)
