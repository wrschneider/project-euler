import utils

primes = set(utils.primes_up_to(10000-0))

def consecutive_primes(a,b):
    n = 0
    while n ** 2 + a * n + b in primes:
        n += 1
    return n

print (consecutive_primes(1, 41))

print (consecutive_primes(-79, 1601))

(a, b) = max(((a, b) for a in range(-999, 1000) for b in range(-1000, 1001)), key=lambda pair: consecutive_primes(pair[0], pair[1]))
print(a*b)
