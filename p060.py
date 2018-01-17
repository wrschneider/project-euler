import utils

BOUND = 9999
N = 5
prime_set = utils.primes_up_to(BOUND)

prime_list = list(prime_set)
prime_list.sort()
prime_list_str = [str(n) for n in prime_list]
prime_set_str = set(prime_list_str)

def recurse(s, i0):
    if len(s) >= N:
        return s  
    for i in range(i0, len(prime_list_str)):
        p1 = prime_list_str[i]
        # hybrid strategy: enumerate primes to loop over, but make check explicitly
        # so we don't have to generate _all_ the primes because the space of primes generated
        # by concatenation is smaller
        if all(utils.is_prime_naive(int(p_concat)) for p0 in s for p_concat in (p0 + p1, p1 + p0)):
            new_s = s + [p1]
            x = recurse(new_s, i + 1)
            # print(new_s)
            if x:
                # stop looking early if we find something
                return x

x = recurse([], 0)
print(x, sum(int(s) for s in x))



