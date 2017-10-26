chains = {1: 1}

def chain_length(n):
    if n in chains: return chains[n]
    if n % 2:
        next = 3*n + 1
    else:
        next = n // 2
    chains[n] = 1 + chain_length(next)
    return chains[n]

print (max(range(1, 1000000), key = lambda i: chain_length(i)))
