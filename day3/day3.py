with open('day3.in', 'r') as f:
    lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]

duplicateList = []

for i in range(len(lines)):
    length = len(lines[i])
    firstCompartment = lines[i][:int(length / 2)]
    secondCompartment = lines[i][int(length / 2):]
    found = False
    for j in range(len(firstCompartment)):
        if found:
            break
        for k in range(len(secondCompartment)):
            if found:
                break
            if firstCompartment[j] == secondCompartment[k]:
                duplicateList.append(firstCompartment[j])
                found = True
totalPriority = 0
for duplicate in duplicateList:
    if duplicate.islower():
        totalPriority += ord(duplicate) - 96
    if duplicate.isupper():
        totalPriority += ord(duplicate) - 38

print(totalPriority)
