def is_pandigital(a, b):
    s = str(a) + str(b) + str(a*b)
    return len(s) == 9 and all(ch in s for ch in '123456789')

c = set()
# ways to get 9 digits total
# 3 digits x 2 digits = 4 digits 
# 4 digits x 1 digit = 4 digits
for a in range(1, 1000):
    for b in range(a + 1, 10000 // a):
        if (is_pandigital(a, b)):
            print(a, b, a*b)
            c.add(a*b)
print(c)
print(sum(c))