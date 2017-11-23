from utils import is_pandigital

def pandigital_multiples():
    for base in range(1, 99999):
        l = len(str(base))
        for n in range(2, 9 // l + 1):
            result = ''.join(str(base * i) for i in range(1, n + 1))
            if is_pandigital(result): 
                yield result

print(max(p for p in pandigital_multiples()))