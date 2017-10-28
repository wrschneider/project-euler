import utils

d = {}
utils.initialize_primes_cache(10001)

for i in range(1, 10000):
    d[i] = sum(utils.proper_divisors(i))

def amicable_pairs():
    for i in range(1, 10000):
        for j in range(i + 1, 10000):
            if d[i] == j and d[j] == i: yield i + j

print(sum(amicable_pairs()))