import utils
from collections import Counter

def candidates():
    bound = 10000
    primes = utils.primes_up_to(bound)
    for p in primes:
        for i in range(1, bound - p):
            triple = (p, p + i, p + 2*i)
            if all(q in primes for q in triple): 
                yield triple

def check_permutation(triple):
    c = Counter(str(triple[0]))
    return all(Counter(str(t)) == c for t in triple)

for c in candidates():
    if check_permutation(c): 
        print(c, "".join(str(n) for n in c))