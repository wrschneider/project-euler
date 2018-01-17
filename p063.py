def gen():
    for a in range(1, 10):
        b = 1
        while True:
            p = str(a ** b)
            if len(p) < b:
                break
            #if len(p) == b:
                print(a, b, a ** b)
            yield (a, b)
            b += 1

print(sum(1 for s in gen()))