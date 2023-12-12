from functools import cache

with open("input.txt") as f:
    lines = f.readlines()

# Part 1
inputs = []
for line in lines:
    springs, groups = line.split()
    groups = tuple([int(x) for x in groups.split(",")])
    inputs.append((springs, groups))


@cache
def count_possible_perms(springs, groups):
    if not groups:
        if all([x in ["?", "."] for x in springs]):
            return 1
        else:
            return 0
    total = 0
    first_group = groups[0]
    latter_groups = groups[1:]
    min_char_for_latter = sum(latter_groups) + len(latter_groups) - 1

    for i in range(len(springs) - min_char_for_latter - first_group):
        test_spring = "." * i + "#" * first_group + "."
        if all([x == y or y == "?" for x, y in zip(test_spring, springs)]):
            total += count_possible_perms(springs[len(test_spring) :], latter_groups)
    return total


print(
    "Part 1:",
    sum([count_possible_perms(springs, groups) for springs, groups in inputs]),
)
print(
    "Part 2:",
    sum(
        [
            count_possible_perms("?".join([springs] * 5), groups * 5)
            for springs, groups in inputs
        ]
    ),
)
