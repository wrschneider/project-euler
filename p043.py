import itertools

def has_property(s):
    divisors = [2,3,5,7,11,13,17]
    return all(int(s[i+1:i+4]) % divisors[i] == 0 for i in range(len(divisors)))

def all_numbers():
    for s in itertools.permutations("0123456789", 10):
        yield ''.join(s)

print(sum(int(s) for s in all_numbers() if has_property(s)))
