import utils

utils.initialize_primes_cache(1000001)

print(max((n for n in range(2, 1000001)), key=utils.ratio))