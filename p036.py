from utils import is_palindrome

def is_palindrome_both(n):
    return is_palindrome(str(n)) and is_palindrome(bin(n)[2:])

print(sum(i for i in range(0, 1000000) if is_palindrome_both(i)))