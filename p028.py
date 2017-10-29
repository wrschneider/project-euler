def spiral(n):
    if n == 1: return 1
    corners = sum((n ** 2) - (n - 1) * i for i in range(4))
    return corners + spiral(n - 2)

print(spiral(1001))
