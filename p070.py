import utils

utils.initialize_primes_cache(10 ** 7 + 1)
print("Primes initialized", flush=True)

min_n = 10 ** 7
min_ratio = 10 ** 7
# note that n can't be prime because phi(p) = p-1 if p is prime - 
# this would minimize n/phi(n) but not satisfy permutation condition
# skip even numbers because if n even , n/phi(n) closer to 2  
for n in range(3, 10 ** 7 + 1, 2):
    phi = utils.phi(n)
    if n/phi < min_ratio and utils.check_permutation(n, phi):
        min_ratio = n/phi
        min_n = n
        print((min_n, min_ratio), flush=True)

print (min_n)
