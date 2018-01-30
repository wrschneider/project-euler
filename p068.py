import itertools

N = 5

digits = set(range(1,2*N+1))

def recurse(remaining_digits, i, answer, solutions):
    # print(remaining_digits, i, answer)
    if i == len(answer):
        # done, check candidate solution
        s = sum(answer[0:3])
        
        if (all(answer[k:] + answer[0:k] not in solutions for k in range(0, 3*N, 3))
            and sum(answer[-3:]) == s
            ):
            print(answer)
            solutions.append(answer)
        return
        
    if answer[i] != 0:
        recurse(remaining_digits, i + 1, answer, solutions)
        return

    for digit in remaining_digits:
        new_answer = list(answer)
        new_answer[i] = digit
        if i == 1: 
            # middle of this group is last of last group
            new_answer[len(answer) - 1] = digit
        if i % 3 == 2:
            # last of this group is middle of next group 
            new_answer[i + 2] = digit
        # prune - is it a dead end?
        if i >= 3 and i % 3 == 2:
            s = sum(new_answer[0:3])
            t = sum(new_answer[i-2:i+1])
            if t != s:
                continue

        recurse(remaining_digits - set([digit]), i + 1, new_answer, solutions)
        
solutions = []
recurse(digits, 0, [0] * (N*3), solutions)

sol_strs = ["".join(str(n) for n in sol) for sol in solutions]
print(max(s for s in sol_strs if len(s) == 16))