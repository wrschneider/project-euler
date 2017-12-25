modulus = (10 ** 10)

print(sum((i ** i) % modulus for i in range(1, 1001)) % modulus)