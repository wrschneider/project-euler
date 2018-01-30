import utils
from collections import Counter
from operator import mul
from functools import reduce

BOUND = 1000001

utils.initialize_primes_cache(BOUND)

print("done with cache", flush=True)
factors = {}
for i in range(BOUND, 2, -1):
    (n, d) = (3 * i - 1, 7*i)
    (low_n, low_d) = utils.lowest_terms(n, d)
    if low_d < BOUND:
        print(low_n, low_d)
        break