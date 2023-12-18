import numpy as np

with open("input.txt") as f:
    lines = f.read().split("\n")

move_dir = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
move_dir_h = {"3": (-1, 0), "1": (1, 0), "2": (0, -1), "0": (0, 1)}


def shoelace(x_y):
    x = x_y[:, 0]
    y = x_y[:, 1]

    S1 = np.sum(x * np.roll(y, 1))
    S2 = np.sum(y * np.roll(x, 1))
    area = 0.5 * np.absolute(S1 - S2)

    return area


vertices = np.array([[0, 0]])
boundary = 0

vertices_h = np.array([[0, 0]])
boundary_h = 0

for line in lines:
    direction, size, colour = line.split()

    size = int(size)
    boundary += size

    size_h = int(colour[2:-2], 16)
    direction_h = colour[-2]
    boundary_h += size_h

    move_x = move_dir[direction][0] * size
    move_y = move_dir[direction][1] * size
    new_vertex = vertices[-1] + [move_x, move_y]
    vertices = np.vstack((vertices, new_vertex))

    move_x = move_dir_h[direction_h][0] * size_h
    move_y = move_dir_h[direction_h][1] * size_h
    new_vertex = vertices_h[-1] + [move_x, move_y]
    vertices_h = np.vstack((vertices_h, new_vertex))

print("Part 1: ", int(shoelace(vertices) + (boundary // 2 + 1)))
print("Part 2: ", int(shoelace(vertices_h) + (boundary_h // 2 + 1)))
