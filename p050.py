import utils

bound = 1000000
primes = utils.primes_up_to(bound)

primes_list = list(primes)
primes_list.sort()

def candidates():
    for i in range(len(primes_list)):
        for j in range(i + 1, len(primes_list)):
            s = sum(primes_list[i:j])
            if s > bound: 
                break
            if s in primes:
                yield(j-i, s)

print(max((c for c in candidates()), key=lambda t: t[0]))