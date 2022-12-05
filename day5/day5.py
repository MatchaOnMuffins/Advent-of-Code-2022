import re

"""
                        [R] [J] [W]
            [R] [N]     [T] [T] [C]
[R]         [P] [G]     [J] [P] [T]
[Q]     [C] [M] [V]     [F] [F] [H]
[G] [P] [M] [S] [Z]     [Z] [C] [Q]
[P] [C] [P] [Q] [J] [J] [P] [H] [Z]
[C] [T] [H] [T] [H] [P] [G] [L] [V]
[F] [W] [B] [L] [P] [D] [L] [N] [G]
 1   2   3   4   5   6   7   8   9 
"""

stacks = ['RQGPCF', 'PCTW', 'CMPHB', 'RPMSQTL', 'NGVZJHP', 'JPD', 'RTJFZPGL', 'JTPFCHLN', 'WCTHQZVG']
stacks = [list(s) for s in stacks]
for stack in stacks:
    stack.reverse()

reExp = re.compile(r'^move (\d+) from (\d) to (\d)')

with open('day5.in', 'r') as f:
    for i in range(10):
        f.readline()
    for i in range(502):
        line = f.readline()
        m = reExp.match(line)
        containerCount = int(m.group(1))
        fromStack = int(m.group(2))
        toStack = int(m.group(3))
        # print('Move {} containers from stack {} to stack {}'.format(containerCount, fromStack, toStack))
        for j in range(containerCount):
            stacks[toStack - 1].append(stacks[fromStack - 1].pop())
ans = ''
for i in range(9):
    ans += stacks[i][-1]
print('Answer:', ans)
