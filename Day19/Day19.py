from collections import defaultdict
from collections import deque
from functools import reduce
import re

with open("input.txt") as f:
    lines = f.read().split("\n\n")

rules = lines[0].split("\n")
parts = lines[1].split("\n")

rules_list = defaultdict(list)
for rule in rules:
    name, *statments = re.split("\{|\}|,", rule)
    rules_list[name] = statments[:-1]


def is_accepted(part, start="in"):
    x = part["x"]
    m = part["m"]
    a = part["a"]
    s = part["s"]

    for statment in rules_list[start]:
        check = statment.split(":")
        if len(check) > 1:
            if eval(check[0]):
                if check[1] == "A":
                    return x + m + a + s
                elif check[1] == "R":
                    return 0
                return is_accepted(part, check[1])
        if len(check) == 1:
            if check[0] == "A":
                return x + m + a + s
            elif check[0] == "R":
                return 0
            else:
                return is_accepted(part, check[0])
    return x + m + a + s


def unpack_parts(part):
    unpacked = defaultdict(list)
    _, _, x, _, m, _, a, _, s, *_ = re.split("\{|\}|,|=", part)
    unpacked["x"] = int(x)
    unpacked["m"] = int(m)
    unpacked["a"] = int(a)
    unpacked["s"] = int(s)
    return unpacked

def rules_permutations(start="in"):
    ans = 0
    q = deque()
    q.append((start, *[[1, 4001] for _ in range(4)]))

    while q:
        current, x, m, a, s = q.popleft()
        if current == "R":
            continue
        if current == "A":
            ans += reduce(lambda x, y: x*y, [len(range(i[0], i[1])) for i in [x,m,a,s]])
            continue
        for statment in rules_list[current]:
            check = statment.split(":")
            if len(check) > 1:
                if "<" in check[0]:
                    variable, value = check[0].split("<")
                    if variable == "x":
                        q.append((check[1], [x[0], int(value)], m.copy(), a.copy(), s.copy()))
                    if variable == "m":
                        q.append((check[1], x.copy()  , [m[0], int(value)], a.copy(), s.copy()))
                    if variable == "a":
                        q.append((check[1], x.copy(), m.copy(), [a[0], int(value)], s.copy()))
                    if variable == "s":
                        q.append((check[1], x.copy(), m.copy(), a.copy(), [s[0], int(value)]))
                    exec(f"{variable}[0] = {value}")
                if ">" in check[0]:
                    variable, value = check[0].split(">")
                    if variable == "x":
                        q.append((check[1], [int(value)+1, x[1]], m.copy(), a.copy(), s.copy()))
                    if variable == "m":
                        q.append((check[1], x.copy(), [int(value)+1, m[1]], a.copy(), s.copy()))
                    if variable == "a":
                        q.append((check[1], x.copy(), m.copy(), [int(value)+1, a[1]], s.copy()))
                    if variable == "s":
                        q.append((check[1], x.copy(), m.copy(), a.copy(), [int(value)+1, s[1]]))
                    exec(f"{variable}[1] = {value}+1")
                    
            if len(check) == 1:
                q.append((check[0], x.copy(), m.copy(), a.copy(), s.copy()))
    return ans
    

print("Part 1:", sum(is_accepted(unpack_parts(item)) for item in parts)) 
print("Part 2:", rules_permutations())