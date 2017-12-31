import utils

bound = 1000000
primes = utils.primes_up_to(bound)
primes_list = list(primes)
primes_list.sort()

def num_in_family(s, d):
    return sum(1 
        for i in range(0, 10) 
        for s2 in (s.replace(d, str(i)),) 
        if int(s2) in primes and s2[0] != "0")

def condition(p):
    s = str(p)
    distinct_digits = list(s)
    return max(num_in_family(s, d) for d in distinct_digits) >= 8

for p in primes:
    if condition(p):
        print(p)
        break

