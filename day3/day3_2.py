groups = []

with open('day3.in', 'r') as f:
    for _ in range(103):
        groups.append([f.readline().replace('\n', ''), f.readline().replace('\n', ''), f.readline().replace('\n', '')])

badges = []

for group in groups:
    for i in range(len(group[0])):
        if (group[0][i] in group[1]) and (group[0][i] in group[2]):
            badges.append(group[0][i])
            break

totalPriority = 0
for badge in badges:
    if badge.islower():
        totalPriority += ord(badge) - 96
    if badge.isupper():
        totalPriority += ord(badge) - 38

print(totalPriority)
