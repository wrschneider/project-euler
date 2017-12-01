# Brute force works because D scales with n 
# P(n+1) - P(n) = 3n+1
# because they get further apart as you go up, you can't get a smaller 
# difference by going higher in the sequence

sequence = [n * (3*n - 1) // 2 for n in range(1, 10000)]
seq_set = set(sequence)

def gen():
    for i in range(len(sequence)):
     for j in range(i + 1, len(sequence)):
        d = (sequence[j] - sequence[i])
        # print(sequence[i], sequence[j], d)
        if d in seq_set and sequence[j] + sequence[i] in seq_set:
            yield(d)

print(min(d for d in gen()))
