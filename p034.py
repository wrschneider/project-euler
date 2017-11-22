from math import factorial

def is_digit_factorial(n):
    return n == sum(factorial(int(d)) for d in str(n))

print(sum(i for i in range(3, 1000000) if is_digit_factorial(i)))
