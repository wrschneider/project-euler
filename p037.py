import utils

upper_bound = 1000000
prime_set = utils.primes_up_to(upper_bound)

def is_truncatable_prime(n):
    s = str(n)
    return all(int(s[0:i]) in prime_set and int(s[i:]) in prime_set for i in range(1, len(s)))

print(sum(p for p in prime_set if p >= 10 and is_truncatable_prime(p)))