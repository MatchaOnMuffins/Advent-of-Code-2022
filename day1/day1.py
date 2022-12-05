with open('day1.in', 'r') as f:
    lines = f.readlines()

calories = []
temp = 0
for line in lines:
    if line == '\n':
        calories.append(temp)
        temp = 0
    else:
        temp += int(line)
calories.sort()
print(calories[-1])
