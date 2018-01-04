import utils

def is_lychrel(n): 
    if n > 10000: raise "n must be < 10000"
    i = 0
    while i < 50:
        s = str(n)
        n = int(s) + int(s[::-1])
        if utils.is_palindrome(str(n)): return False
        i += 1
    return True

print(is_lychrel(47)) 
print(is_lychrel(349))
print(is_lychrel(196))
print(is_lychrel(4994))

print(sum(1 for n in range(1, 10001) if is_lychrel(n)))
