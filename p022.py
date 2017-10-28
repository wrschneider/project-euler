import re

def score_one_name(name):
    return sum(ord(ch) - ord('A') + 1 for ch in name)

file = open("names.txt", "r")
txt = file.read()
names = [re.sub('"', '', name) for name in txt.split(",")]
names.sort()

print(sum((i + 1) * score_one_name(names[i]) for i in range(len(names))))
    