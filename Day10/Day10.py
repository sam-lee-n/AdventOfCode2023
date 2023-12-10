with open("input.txt") as f:
    lines = f.readlines()

#   Part 1
pipe_map = []
for line in lines:
    pipe_map.append(list(line.strip()))
max_x = len(pipe_map[0])
max_y = len(pipe_map)

dis_map = [[-1] * len(pipe_map[0]) for i in range(len(pipe_map))]

path = []
path.append([(i, x.index("S")) for i, x in enumerate(pipe_map) if "S" in x][0])
dis_map[path[0][0]][path[0][1]] = 0

step = 0
s_con = {"|", "-", "J", "L", "7", "F"}
for loc in path:
    current_dis = dis_map[loc[0]][loc[1]]
    current_pipe = pipe_map[loc[0]][loc[1]]

    if (
        loc[1] + 1 < max_x
        and dis_map[loc[0]][loc[1] + 1] < 0
        and current_pipe in ["S", "L", "F", "-"]
        and pipe_map[loc[0]][loc[1] + 1] in ["7", "J", "-"]
    ):
        dis_map[loc[0]][loc[1] + 1] = current_dis + 1
        path.append((loc[0], loc[1] + 1))
        if current_pipe == "S":
            s_con &= {"L", "F", "-"}

    if (
        loc[1] != 0
        and dis_map[loc[0]][loc[1] - 1] < 0
        and current_pipe in ["S", "7", "J", "-"]
        and pipe_map[loc[0]][loc[1] - 1] in ["L", "F", "-"]
    ):
        dis_map[loc[0]][loc[1] - 1] = current_dis + 1
        path.append((loc[0], loc[1] - 1))
        if current_pipe == "S":
            s_con &= {"7", "J", "-"}

    if (
        loc[0] != 0
        and dis_map[loc[0] - 1][loc[1]] < 0
        and current_pipe in ["S", "L", "J", "|"]
        and pipe_map[loc[0] - 1][loc[1]] in ["F", "7", "|"]
    ):
        dis_map[loc[0] - 1][loc[1]] = current_dis + 1
        path.append((loc[0] - 1, loc[1]))
        if current_pipe == "S":
            s_con &= {"L", "J", "|"}

    if (
        loc[0] + 1 < max_y
        and dis_map[loc[0] + 1][loc[1]] < 0
        and current_pipe in ["S", "F", "7", "|"]
        and pipe_map[loc[0] + 1][loc[1]] in ["L", "J", "|"]
    ):
        dis_map[loc[0] + 1][loc[1]] = current_dis + 1
        path.append((loc[0] + 1, loc[1]))
        if current_pipe == "S":
            s_con &= {"F", "7", "|"}

# print("\n".join(map(str, dis_map)))
print("Part 1:", max([max(x) for x in dis_map]))

#   Part 2
enclosed_map = [[0] * len(pipe_map[0]) for i in range(len(pipe_map))]
(s_con,) = s_con
for i in range(len(pipe_map)):
    for j in range(len(pipe_map[0])):
        if pipe_map[i][j] == "S":
            pipe_map[i][j] = s_con[0]


for i, row in enumerate(pipe_map):
    enclosed = False
    going_down = None
    for j, col in enumerate(row):
        if dis_map[i][j] > -1 and col == "|":
            enclosed = not enclosed
        elif dis_map[i][j] > -1 and col in "LF":
            going_down = col == "F"
        elif dis_map[i][j] > -1 and col in "7J":
            if col == ("J" if going_down else "7"):
                enclosed = not enclosed
                going_down = None
        if enclosed:
            if dis_map[i][j] < 0:
                enclosed_map[i][j] = 1

# print("\n".join(map(str, enclosed_map)))
print("Part 2:", sum([x for line in enclosed_map for x in line]))


symbolMap = {
"F": "\u250F",
"J": "\u251B",
"L": "\u2517",
"7": "\u2513",
"|": "\u2503",
"-": "\u2501",
".": " "
}

for i in range(len(pipe_map)):
    for j in range(len(pipe_map[0])):
        if dis_map[i][j] > -1:
            pipe_map[i][j] = symbolMap[pipe_map[i][j]]
        else:
            pipe_map[i][j] = " "
        if enclosed_map[i][j] == 1:
            pipe_map[i][j] = "I"

print("\n".join(["".join(x) for x in pipe_map]))