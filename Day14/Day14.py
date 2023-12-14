with open("input.txt") as f:
    lines = f.read().split("\n")


# Part 1
def get_weight(lines):
    return sum(
        [i + 1 for line in lines for i, char in enumerate(line[::-1]) if char == "O"]
    )


def transpose(lines):
    return ["".join(chars) for chars in zip(*lines)]


def tumble(lines):
    tilted = []
    for line in lines:
        line = list(line)
        for i, char in enumerate(line):
            if char == "O":
                for j in range(1, i + 1):
                    if line[i - j] == ".":
                        line[i - j], line[i - j + 1] = line[i - j + 1], line[i - j]
                    else:
                        break
        tilted.append("".join(line))
    return tilted


def p1(lines):
    return get_weight(tumble(transpose(lines)))


def p2(lines, cycles=1):
    pre_states = {}
    c = 0
    while c < cycles:
        # add logic to spot have we seen this before...then we can skip ahead
        seen_lines = "".join(lines)
        if seen_lines in pre_states:
            time_to_repeat = c - pre_states[seen_lines]
            c += (cycles - c) // time_to_repeat * time_to_repeat
            if c >= cycles:
                break
        else:
            pre_states[seen_lines] = c

        # North
        lines = transpose(lines)
        lines = tumble(lines)

        # East
        lines = transpose(lines)
        lines = tumble(lines)

        # South
        lines = lines[::-1]
        lines = transpose(lines)
        lines = tumble(lines)

        # West
        lines = transpose(lines)
        lines = lines[::-1]
        lines = [line[::-1] for line in lines]
        lines = tumble(lines)
        lines = [line[::-1] for line in lines]

        c += 1

    return get_weight(transpose(lines))


print("Part 1:", p1(lines))
print("Part 2:", p2(lines, 1000000000))
