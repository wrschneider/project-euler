from utils import is_pandigital, is_prime_naive, primes_up_to

# note that 3, 8 and 9-digit pandigitals are all divisible by 3 
# so biggest is 7 digits at most 

primes = primes_up_to(7654321 +1)
print (max(p for p in primes for s in (str(p),) if is_pandigital(s, len(s))))
