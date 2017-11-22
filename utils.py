import itertools
from functools import reduce
from operator import mul

primes_cache = []

def primes_up_to(n):
  if primes_cache:
    return primes_cache
  sieve = set(i for i in range(2, n + 1))
  for i in range(2, n + 1):
    if i not in sieve: continue
    for j in range(2, n // i + 1):
      multiple = i * j
      if multiple in sieve: sieve.remove(multiple)
  return sieve

def initialize_primes_cache(n):
    primes_cache.extend(primes_up_to(n))

prime_factor_cache = {}

def prime_factorization(n):
    if n == 1: return []
    if n in prime_factor_cache:
        return prime_factor_cache[n]

    primes = primes_up_to(n)
    for p in primes: 
        if p > n: continue
        if n % p == 0:
            factors = [p] + prime_factorization(n // p)
            prime_factor_cache[n] = factors
            return factors

    raise "should never get here"

def divisors(n):
    pf = prime_factorization(n)
    return set(reduce(mul, subset, 1) for k in range(0, len(pf) + 1) for subset in itertools.combinations(pf, k))

def proper_divisors(n):
    divs = divisors(n)
    divs.remove(n)
    return divs 

def text_to_int_array(s):
  return [[int(n) for n in line.split(' ')] for line in s.split('\n') if line]

def is_palindrome(s):
  return s == s[::-1]

if __name__ == '__main__':
    print (primes_up_to(19))
    print (prime_factorization(28))
    print (divisors(28))
    print (divisors(56))
    