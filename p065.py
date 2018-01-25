import convergents

def coeff(k):
    if k % 3 == 1: return 2*((k//3) + 1)
    return 1

n,d = convergents.convergent(98, coeff, 2)
print(sum(int(ch) for ch in str(n)))
