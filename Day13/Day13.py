from functools import cache

with open("input.txt") as f:
    notes = f.read().split("\n\n")

total = 0
first_pass = []
for lines in notes:
    lines = lines.split("\n")
    mirror_row = 0
    mirror_col = 0

    for i in range(1, len(lines)):
        if lines[i] == lines[i - 1]:
            for j in range(1, min(i, len(lines) - i)):
                if lines[i - j - 1] != lines[i + j]:
                    break
            else:
                mirror_row = i
                # print("row", mirror_row)

    for i in range(1, len(lines[0])):
        col = "".join([x[i] for x in lines])
        col2 = "".join([x[i - 1] for x in lines])
        if col == col2:
            for j in range(1, min(i, len(lines[0]) - i)):
                col = "".join([x[i - j - 1] for x in lines])
                col2 = "".join([x[i + j] for x in lines])

                if col != col2:
                    break
            else:
                mirror_col = i
                # print("col", mirror_col)

    total += mirror_row * 100 + mirror_col


print("Part 1:", total)


# Part 2
def smugdes(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))


total = 0
for lines in notes:
    lines = lines.split("\n")
    mirror_row = 0
    mirror_col = 0

    for i in range(1, len(lines)):
        potential = smugdes(lines[i], lines[i - 1])
        if lines[i] == lines[i - 1] or potential == 1:
            for j in range(1, min(i, len(lines) - i)):
                if lines[i - j - 1] != lines[i + j]:
                    if smugdes([i - j - 1], lines[i + j]) == 1 and potential != 1:
                        potential = 1
                        continue
                    else:
                        break
            else:
                if potential == 1:
                    mirror_row = i
                    # print("row", mirror_row, loop)

    for i in range(1, len(lines[0])):
        col = "".join([x[i] for x in lines])
        col2 = "".join([x[i - 1] for x in lines])
        potential = smugdes(col, col2)
        if col == col2 or potential == 1:
            for j in range(1, min(i, len(lines[0]) - i)):
                col = "".join([x[i - j - 1] for x in lines])
                col2 = "".join([x[i + j] for x in lines])
                if col != col2:
                    if smugdes(col, col2) == 1 and potential != 1:
                        potential = 1
                        continue
                    else:
                        break
            else:
                if potential == 1:
                    mirror_col = i
                    # print("col", mirror_col)

    total += mirror_row * 100 + mirror_col

print("Part 2:", total)
