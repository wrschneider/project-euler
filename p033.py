import utils
from utils import lowest_terms

def equal(a1, b1, a2, b2):
    if a2 == 0 or b2 == 0: return False
    return lowest_terms(a1, b1) == lowest_terms(a2, b2)

def is_digit_cancelling(a, b):
    a_str = str(a)
    b_str = str(b)
    return any( a_str[1-i] == b_str[1-j] and a_str[1-i] != '0' and equal(a, b, int(a_str[i]), int(b_str[j])) for i in [0, 1] for j in [0, 1])

utils.initialize_primes_cache(100000)
a = 1
b = 1
for i in range(10, 100):
    for j in range(i + 1, 100):
        if is_digit_cancelling(i, j): 
            print(i, j)
            a *= i
            b *= j

print(a,b)
print(lowest_terms(a, b))