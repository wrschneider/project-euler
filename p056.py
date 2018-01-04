def digit_sum(n):
    return sum(int(d) for d in str(n))

print(max(digit_sum(a ** b) for a in range(1, 101) for b in range(1, 101)))
