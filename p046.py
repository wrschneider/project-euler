import utils

primes = utils.primes_up_to(100000)
double_squares = set(2*n*n for n in range(1, 10000))

def search(n):
    return any(n - p in double_squares for p in primes)

print (min(i for i in range(3, 100000, 2) if i not in primes and not search(i)))



