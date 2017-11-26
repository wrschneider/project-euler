# solve a + b + c = p AND a^2 + b^2 = c^2 
# AND maybe a + b > c
from collections import defaultdict, Counter
from functools import reduce

max_p = 1000

# reverse lookup of perfect squares
square_reverse_lookup = dict((i ** 2, i) for i in range(0, max_p))

# find all triples
def triples(upper_bound):
    for a in range(1, upper_bound):
        for b in range(a, upper_bound):
            c2 = a ** 2 + b ** 2
            if c2 in square_reverse_lookup:  
                yield(a, b, square_reverse_lookup[c2])

solutions = Counter(sum(t) for t in triples(max_p // 2) if sum(t) <= max_p)

print(solutions.most_common(1))
