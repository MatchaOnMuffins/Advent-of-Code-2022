with open('day6.in', 'r') as f:
    lines = f.readline()

s = ''
print([len({*(s := s + c)[-14:]}) for c in lines].index(14) + 1)
