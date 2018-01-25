def convergent(i, coeff, a0):
    (n, d) = (0, 1)
    for k in range(i, -1, -1):
        x = coeff(k)
        (n, d) = (d, x * d + n)
        # print(n,d)

    return (n + a0*d, d)

def coefficients(n):
    a0 = int(n ** 0.5)
    if a0 ** 2 == n: 
        return None
    t = (a, x, y) = (a0, 1, a0)
    tuples = []

    # process:
    # x / (sqrt(n) - y)
    # => x(sqrt(n) + y) / (n - y^2)
    # assumption is that (n-y^2) is a multiple of x - not sure why this is always true
    # => (sqrt(n) + y) / ((n - y^2) / x)
    while t not in tuples:
        tuples.append(t)
    
        denom = ((n - y ** 2) // x)
        int_part = (a0 + y) // denom
        t = (a, x, y) = (int_part, denom,  denom * int_part - y)
    
    return [t[0] for t in tuples]