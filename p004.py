# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(s):
    return s == s[::-1]

m = max(i * j for i in range(100, 1000) for j in range(100, 1000) if is_palindrome(str(i * j)))
print(m)