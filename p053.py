import utils

print(sum(1 for n in range(23, 101) for r in range(0, n) if utils.ncr(n, r) > 1000000))