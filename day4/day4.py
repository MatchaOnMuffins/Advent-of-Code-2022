import re

regExp = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

with open('day4.in', 'r') as f:
    lines = f.readlines()

overlap = 0
for line in lines:
    line.replace('\n', '')
    m = regExp.match(line)
    if (int(m.group(1)) >= int(m.group(3))) and (int(m.group(2)) <= int(m.group(4))):
        overlap += 1
    elif (int(m.group(1)) <= int(m.group(3))) and (int(m.group(2)) >= int(m.group(4))):
        overlap += 1
print(overlap)
