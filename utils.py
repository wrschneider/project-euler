def primes_up_to(n):
  sieve = set(i for i in range(2, n + 1))
  for i in range(2, n + 1):
    if i not in sieve: continue
    for j in range(2, n // i + 1):
      multiple = i * j
      if multiple in sieve: sieve.remove(multiple)
  return sieve

if __name__ == '__main__':
    print (primes_up_to(19))
