import re
from collections import defaultdict

with open("input.txt") as f:
    lines = f.readlines()

#   Part 1
grid_map = []
for line in lines:
    grid_map.append(list(line.strip()))

# print("\n".join(["".join(x) for x in grid_map]))
move_dir = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}

def find_energized(grid_map, start=(0,0), dstart="E"):
    energized = defaultdict(list)
    path = []
    path.append([start, dstart])

    for step, direction in path:
        next_step = tuple(x + y for x, y in zip(step, move_dir[direction]))

        if (
            step[0] < 0
            or step[0] >= len(grid_map)
            or step[1] < 0
            or step[1] >= len(grid_map[0])
            or direction in energized[step]
        ):
            continue
        energized[step].append(direction)
        # print("\n",step, grid_map[step[0]][step[1]],direction)
        if grid_map[step[0]][step[1]] == "|" and direction in "EW":
            path.append([tuple(x + y for x, y in zip(step, move_dir["N"])), "N"])
            path.append([tuple(x + y for x, y in zip(step, move_dir["S"])), "S"])

        elif grid_map[step[0]][step[1]] == "-" and direction in "NS":
            path.append([tuple(x + y for x, y in zip(step, move_dir["E"])), "E"])
            path.append([tuple(x + y for x, y in zip(step, move_dir["W"])), "W"])

        elif grid_map[step[0]][step[1]] == "/":
            if direction in "E":
                path.append([tuple(x + y for x, y in zip(step, move_dir["N"])), "N"])
            elif direction in "W":
                path.append([tuple(x + y for x, y in zip(step, move_dir["S"])), "S"])
            elif direction in "N":
                path.append([tuple(x + y for x, y in zip(step, move_dir["E"])), "E"])
            elif direction in "S":
                path.append([tuple(x + y for x, y in zip(step, move_dir["W"])), "W"])

        elif grid_map[step[0]][step[1]] == "\\":
            if direction in "E":
                path.append([tuple(x + y for x, y in zip(step, move_dir["S"])), "S"])
            elif direction in "W":
                path.append([tuple(x + y for x, y in zip(step, move_dir["N"])), "N"])
            elif direction in "N":
                path.append([tuple(x + y for x, y in zip(step, move_dir["W"])), "W"])
            elif direction in "S":
                path.append([tuple(x + y for x, y in zip(step, move_dir["E"])), "E"])
        else:
            path.append([next_step, direction])


    return len(energized)

print("Part 1:", find_energized(grid_map))

ans = 0
ans = max(ans, max([find_energized(grid_map, (y, 0), "E") for y in range(len(grid_map))]))
ans = max(ans, max([find_energized(grid_map, (y, len(grid_map[0]) - 1), "W") for y in range(len(grid_map))]))
ans = max(ans, max([find_energized(grid_map, (0, x), "S") for x in range(len(grid_map[0]))]))
ans = max(ans, max([find_energized(grid_map, (len(grid_map) -1, x), "N") for x in range(len(grid_map[0]))]))

print("Part 2:", ans)
