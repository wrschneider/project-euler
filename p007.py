def nth_prime(n):
  primes = []
  i = 2
  while len(primes) < n:
    if all(i % p != 0 for p in primes):
      primes = primes + [i]
    i += 1
  return primes[-1]

print (nth_prime(10001))

