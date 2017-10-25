def prime_factors(n, l):
    print("called ", n, l)
    for i in range(2, n + 1):
        if n % i == 0: return prime_factors(n // i, l + [i])
    return l

l = prime_factors(600851475143, [])
print(l)
print(max(l))

