with open('day2.in', 'r') as f:
    rounds = f.readlines()

rounds = [x.strip() for x in rounds]
rounds = [x.replace('X', 'A') for x in rounds]
rounds = [x.replace('Y', 'B') for x in rounds]
rounds = [x.replace('Z', 'C') for x in rounds]
rounds = [x.split(' ') for x in rounds]
print(rounds)

points = 0
for OneRound in rounds:
    if OneRound[1] == 'A':
        points += 1
    elif OneRound[1] == 'B':
        points += 2
    elif OneRound[1] == 'C':
        points += 3
    if OneRound[0] == OneRound[1]:
        points += 3
    elif OneRound[0] == 'A' and OneRound[1] == 'B':
        points += 6
    elif OneRound[0] == 'A' and OneRound[1] == 'C':
        points += 0
    elif OneRound[0] == 'B' and OneRound[1] == 'A':
        points += 0
    elif OneRound[0] == 'B' and OneRound[1] == 'C':
        points += 6
    elif OneRound[0] == 'C' and OneRound[1] == 'A':
        points += 6
    elif OneRound[0] == 'C' and OneRound[1] == 'B':
        points += 0

print(points)
