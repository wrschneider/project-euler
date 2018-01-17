def filtered_set(gen):
    return set(str(n) for n in gen if n >= 1000 and n <= 9999)

triangle = filtered_set(n*(n+1) // 2 for n in range(1, 300))
square = filtered_set(n*n for n in range(1, 100))
penta = filtered_set(n*(3*n-1)//2 for n in range(1, 100))
hexa = filtered_set(n*(2*n-1) for n in range(1, 100))
hepta = filtered_set(n*(5*n-3)//2 for n in range(1, 100))
octa = filtered_set(n*(3*n-2) for n in range(1, 100))

all_sets = [triangle, square, penta, hexa, hepta, octa]

def recurse(sets, answer):
    if not sets:
        # print("testing ", answer)
        if answer[-1][2:] == answer[0][:2]:
            return answer
        else:
            return None

    for i in range(len(sets)):
        for n in sets[i]:
            if not answer or answer[-1][2:] == n[:2]:
                result = recurse(sets[:i] + sets[i+1:], answer + [n])
                if result:
                    return result

answer = recurse(all_sets, [])
print (sum(int(s) for s in answer), answer)


