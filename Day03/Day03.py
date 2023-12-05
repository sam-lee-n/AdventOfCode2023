import re

with open("input.txt") as f:
    lines = f.readlines()

# Part 1
max_x = len(lines[0])
max_y = len(lines)
sum_total = 0
for n, line in enumerate(lines):
    for m in re.finditer(r"\d+", line):
        start_x = max(m.start() - 1, 0)
        end_x = min(m.end() + 1, max_x)

        # get a box round the value
        full_text = line[start_x:end_x]
        if n < max_y - 1:
            full_text += lines[n + 1][start_x:end_x]
        if n > 0:
            full_text += lines[n - 1][start_x:end_x]

        # check for symbols
        if len(re.sub("\d|\.", "", full_text)) > 0:
            sum_total += int(m.group())

print("Part 1:", sum_total)

# Part 2
sum_total = 0
for n, line in enumerate(lines):
    for m in re.finditer(r"\*", line):
        gear = 1
        start_x = max(m.start() - 1, 0)
        end_x = min(m.end() + 1, max_x)

        # get a box round the *
        full_text = line[start_x:end_x]
        if n > 0:
            full_text += " " + lines[n - 1][start_x:end_x]
        if n < max_y - 1:
            full_text += " " + lines[n + 1][start_x:end_x]

        # print(n, "test", start_x, end_x, full_text, len(re.findall("\d+", full_text)) == 2)
        if len(re.findall("\d+", full_text)) == 2:
            # same row
            if line[m.start() - 1].isdigit():
                gear *= int(re.findall("\d+", line[: m.start()])[-1])
            if line[m.end()].isdigit():
                gear *= int(re.findall("\d+", line[m.end():])[0])

            # above
            if n < max_y - 1:
                if len(re.findall("\d+", lines[n - 1][start_x:end_x])) == 2:
                    gear *= int(re.findall("\d+", lines[n - 1][: m.start()])[-1])
                    gear *= int(re.findall("\d+", lines[n - 1][m.start():])[0])

                elif len(re.findall("\d+", lines[n - 1][start_x:end_x])) > 0:
                    if lines[n - 1][m.start() - 1].isdigit():
                        gear *= int(re.findall("\d+", lines[n - 1][: m.end()+1])[-1])
                    elif len(re.findall("\d+", lines[n - 1][m.start():end_x])) > 0:
                        gear *= int(re.findall("\d+", lines[n - 1][m.start():])[0])

            # below
            if n > 0:
                if len(re.findall("\d+", lines[n + 1][start_x:end_x])) == 2:
                    gear *= int(re.findall("\d+", lines[n + 1][: m.start()])[-1])
                    gear *= int(re.findall("\d+", lines[n + 1][m.start():])[0])

                elif len(re.findall("\d+", lines[n + 1][start_x:end_x])) > 0:
                    if lines[n + 1][m.start() - 1].isdigit():
                        gear *= int(re.findall("\d+", lines[n + 1][: m.end()+1])[-1])
                    elif len(re.findall("\d+", lines[n + 1][m.start():end_x])) > 0:
                        gear *= int(re.findall("\d+", lines[n + 1][m.start():])[0])

        if gear > 1:
            sum_total += gear

print("Part 2:", sum_total)
