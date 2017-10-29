f0 = 1
f1 = 1
i = 1

while len(str(f0)) < 1000:
    i += 1
    (f0, f1) = (f1, f0 + f1)

print (i)