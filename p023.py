import utils
upper_bound = 28123
utils.initialize_primes_cache(upper_bound)

def abundant(n):
    return sum(utils.proper_divisors(n)) > n

abundant_set = set(i for i in range(1, upper_bound) if abundant(i))

sum_of_two_abundants = set(n for n in range(1, upper_bound) for i in abundant_set if (n - i) in abundant_set)

print(sum(i for i in range(1, upper_bound) if i not in sum_of_two_abundants)) 