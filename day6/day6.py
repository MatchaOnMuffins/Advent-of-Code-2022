import re

with open('day6.in', 'r') as f:
    lines = f.readline()

print(re.search(r"(.)(?!\1)(.)(?!\1|\2)(.)(?!\1|\2|\3).", lines).end())  # magic regex
