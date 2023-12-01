import re

with open('input.txt') as f:
    lines = f.readlines()

# Part 1
total = 0 
for line in lines:
  num = re.sub('\D', '', line)
  total += int(num[0]+num[-1])
#   print(line, int(num[0]+num[-1]), total)
print('Part 1:', total)

# Part 2
num_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,'seven':7,'eight':8,'nine':9,}
total = 0 
for line in lines:
    new_line = ''
    for i in range(len(line)):
        if line[i].isdigit():
            new_line += line[i]
        else:
            for key, value in num_dict.items():
                if re.match(f"^{key}", line[i:]):
                    new_line += str(value)
    total += int(new_line[0]+new_line[-1])
print('Part 2:', total)
