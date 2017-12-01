# try brute force

limit = 100000
triangle = set(n * (n+1) // 2 for n in range(1, limit))
pentagonal = set(n * (3*n-1) // 2 for n in range(1, limit))
hexagonal = set(n * (2*n-1) for n in range(1, limit))

print(min(n for n in triangle & pentagonal & hexagonal if n > 40755))