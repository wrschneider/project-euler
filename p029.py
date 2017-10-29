# brute force works at these interval sizes
terms = set(a ** b for a in range(2, 101) for b in range (2, 101))
print(len(terms))