import utils

prime_set = utils.primes_up_to(1000000)

def is_circular_prime(n):
    s = str(n)
    return all (r in prime_set for i in range(len(s)) for r in (int(s[i:] + s[0:i]),))

print (sum(1 for i in range(2, 1000000) if is_circular_prime(i)))