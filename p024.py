import math

def nth_permutation(n, digits):
    if len(digits) == 1: return digits[0]

    # observation: if 10 digits total, 0 will be first digit for first 9! permutations, 1 will be first for the second 9!, etc.
    # then you can repeat that process recursively for each successive digit
    
    remaining_digits = len(digits) - 1
    permuts_per_initial_digit = math.factorial(remaining_digits)
    index_first_digit = n // permuts_per_initial_digit
    return digits[index_first_digit] + nth_permutation(n % permuts_per_initial_digit, digits[:index_first_digit] + digits[index_first_digit + 1:])

print(nth_permutation(1000001, "0123456789"))
