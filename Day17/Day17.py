from heapq import heappop, heappush

with open("input.txt") as f:
    lines = f.read().split("\n")

move_dir = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}


def find_lowest_cost(lines, min_step=1, max_step=3):
    start = (0, 0)
    end = (len(lines) - 1, len(lines[0]) - 1)
    queue = [(0, start, "S", 1), (0, start, "E", 1)]
    visited = {}

    while queue:
        cost, location, direction, steps = heappop(queue)
        if (location, direction, steps) in visited:
            continue
        visited[(location, direction, steps)] = cost

        new_location = (
            location[0] + move_dir[direction][0],
            location[1] + move_dir[direction][1],
        )
        if (
            new_location[0] < 0
            or new_location[0] >= len(lines)
            or new_location[1] < 0
            or new_location[1] >= len(lines[0])
        ):
            continue

        new_cost = cost + int(lines[new_location[0]][new_location[1]])
        if new_location == end and steps >= min_step and steps <= max_step:
            return new_cost
        for next_direction in move_dir:
            if (
                next_direction == "N"
                and direction == "S"
                or next_direction == "S"
                and direction == "N"
                or next_direction == "E"
                and direction == "W"
                or next_direction == "W"
                and direction == "E"
            ):
                continue

            new_steps = steps + 1 if next_direction == direction else 1
            if new_steps > max_step or (
                next_direction != direction and steps < min_step
            ):
                continue
            heappush(queue, (new_cost, new_location, next_direction, new_steps))


print("Part 1: ", find_lowest_cost(lines))
print("Part 2: ", find_lowest_cost(lines, 4, 10))
