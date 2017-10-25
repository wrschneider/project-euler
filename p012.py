from collections import Counter
from functools import reduce
from operator import mul
import utils

high = 100000
utils.initialize_primes_cache(high) 
# explanation: nth triangle number = n*(n-1)/2 = (n^2 - n)/2  < n^2
# highest prime factor of that can be sqrt 
# so n is upper bound on highest prime factor of nth triangle number

s = 0
for i in range(1, high):
    s += i
    pf = Counter(utils.prime_factorization(s))
    # explanation: we don't need to know the actual divisors, just how many of them there are
    # itertools.combinations would let us enumerate the actual divisors
    num_divisors = reduce(mul, (exp + 1 for (prime, exp) in pf.items()), 1) 
    print(s, num_divisors)
    if num_divisors > 500: break
 
