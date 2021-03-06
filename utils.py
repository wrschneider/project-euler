from datetime import datetime
from collections import Counter
import itertools
import math
from functools import reduce
from operator import mul

primes_cache = []
prime_set = set()

def is_prime_naive_inner(n):
  for i in range(3, int(math.sqrt(n)) + 1, 2):
    if n % i == 0: return False
  return True

def is_prime_naive(n):
  if n == 1: return False
  if n <= 3: return True
  if n % 2 == 0: return False
  return is_prime_naive_inner(n)

def is_prime_fermat(n):
  if n == 1: return False
  if n <= 3: return True
  if n % 2 == 0: return False
  if pow(2, (n-1), n) != 1: return False
  return is_prime_naive_inner(n)

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
    for p in primes_cache:
      prime_set.add(p)

prime_factor_cache = {}

def prime_factorization(n, distinct=False):
    if n in prime_factor_cache:
        return prime_factor_cache[n]

    if n == 1: return []

    if n in prime_set: return[n] # optimization if prime set cached

    primes = primes_up_to(n)

    for p in primes:
        if n == p:
          return [n] # in case prime cache is not initialized
        if p*p > n: 
          continue
        if n % p == 0:
            next_n = n // p
            if distinct:
              while next_n % p == 0:
                next_n = next_n // p
            factors = [p] + prime_factorization(next_n)
            prime_factor_cache[n] = factors
            return factors

    prime_factor_cache[n] = [n]
    return prime_factor_cache[n] # either n is prime, OR we didn't initialize cache high enough

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

def is_pandigital(s, n=9):
    return len(s) == n and all(ch in s for ch in '123456789'[0:n])

def ncr(n, r):
  return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def check_permutation(n1, n2):
    return Counter(str(n1)) == Counter(str(n2))

def phi(n):  
    prime_factors = prime_factorization(n, True)
    denom = reduce(mul, (p for p in prime_factors), 1)
    num = n * reduce(mul, (p-1 for p in prime_factors), 1)
    return num // denom

def ratio(n):
    return n / phi(n) 

def gcd(a, b):
    divisors_a = divisors(a)
    divisors_b = divisors(b)

    return max(d for d in divisors_a if d in divisors_b)

def lowest_terms(a, b):
    d = gcd(a, b)
    return (a // d, b // d)

if __name__ == '__main__':
    print(ncr(5, 3))
    print(is_pandigital("123456789"))
    print(is_pandigital("12345678"))  
    print(is_pandigital("12345678", 8))
    print(is_prime_naive(6))
    print(is_prime_naive(13))
    print (primes_up_to(19))
    print (prime_factorization(28))
    print (divisors(28))
    print (divisors(56))