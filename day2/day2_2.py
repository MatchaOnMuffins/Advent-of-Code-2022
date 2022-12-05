with open('day2.in', 'r') as f:
    rounds = f.readlines()

rounds = [x.strip() for x in rounds]
rounds = [x.split(' ') for x in rounds]


def getScore(OpponentMove: str, Outcome: str) -> int:
    moveScore = 0
    matchScore = 0
    if OpponentMove == 'A' and Outcome == 'X':
        moveScore += 3
    elif OpponentMove == 'B' and Outcome == 'X':
        moveScore += 1
    elif OpponentMove == 'C' and Outcome == 'X':
        moveScore += 2
    elif OpponentMove == 'A' and Outcome == 'Y':
        moveScore += 1
    elif OpponentMove == 'B' and Outcome == 'Y':
        moveScore += 2
    elif OpponentMove == 'C' and Outcome == 'Y':
        moveScore += 3
    elif OpponentMove == 'A' and Outcome == 'Z':
        moveScore += 2
    elif OpponentMove == 'B' and Outcome == 'Z':
        moveScore += 3
    elif OpponentMove == 'C' and Outcome == 'Z':
        moveScore += 1
    if Outcome == 'Y':
        matchScore += 3
    elif Outcome == 'Z':
        matchScore += 6
    return moveScore + matchScore


points = 0
for OneRound in rounds:
    points += getScore(OneRound[0], OneRound[1])

print(points)
