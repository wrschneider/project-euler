import utils

def spiral_gen(n):
    if n == 1:
        return [1]
    if n % 2 == 0:
        raise "n must be odd"
    return [(n ** 2) - (n - 1) * i for i in range(4)]

n = 1
count = 0
primes_count = 0

while True:
    s = spiral_gen(n)

    primes_count += sum(1 for p in s if utils.is_prime_fermat(p))
    count += len(s)
    # print(n, count, primes_count, primes_count / count)
    if n > 3 and primes_count / count < 0.10: 
        break
    n += 2
    
print(n)

