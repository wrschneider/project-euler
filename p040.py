from operator import mul
from functools import reduce

# brute force is fast enough
requested_digits = [1, 10, 100, 1000, 10000, 100000, 1000000]

# would prefer a more direct approach but at least we can separate 
# digit generation from choosing and multiplying the requested digits  
def generate_digits(upper_bound):
    i = 0
    num = 1
    while i <= upper_bound:
        for d in str(num):
            i += 1
            yield(i, int(d))
        num += 1

prod = reduce(mul, (d for (i, d) in generate_digits(max(requested_digits)) if i in requested_digits))
print(prod)