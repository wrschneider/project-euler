import utils

upper_bound = 200000
num_consec = 4

utils.initialize_primes_cache(upper_bound)
factors = dict((i, set(utils.prime_factorization(i))) for i in range(4, upper_bound))
for i in range(4, upper_bound):
    if all(len(factors[i+j]) >= num_consec for j in range(num_consec)): 
        print(i, factors[i])
        break


