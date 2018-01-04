def expand(limit):
    (n, d) = (1, 2)
    for i in range(limit):
        n_plus1 = n + d
        yield(n_plus1, d)
        (n, d) = (d, 2*d + n)

print(sum(1 for (n, d) in expand(1000) if len(str(n)) > len(str(d))))