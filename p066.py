import convergents

def coeff(c):
    cycle = len(c) - 1 
    return lambda i: c[i % cycle + 1]

def solve(D):
    c = convergents.coefficients(D)
    if not c:
        return 0

    i = 0
    while True: 
        (n, d) = convergents.convergent(i, coeff(c), c[0])
        if n ** 2 - D*d**2 == 1:
            return n
        i += 1

print(max((D for D in range(2, 1001)), key=lambda D: solve(D)))
