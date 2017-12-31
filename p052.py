from collections import Counter

i = 1
while True:
    c = [Counter(str(i * j)) for j in range(1, 7)]
    if all(c[0] == cx for cx in c):
        print(i)
        break
    i += 1