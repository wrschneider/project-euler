import convergents

def period(n):
    c = convergents.coefficients(n)
    if c:
        return len(c) - 1
    else:
        return 0

def has_odd_period(i): 
    p = period(i)
    if p:
        return p % 2 == 1
    else:
        return False

print(sum(1 for i in range(2, 10001) if has_odd_period(i)))