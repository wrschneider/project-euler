def test(x):
    return all(x % i == 0 for i in range(2, 20))

i = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19 
print(i)
print(test(i))
