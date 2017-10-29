def fraction(d):
    dividend = 10
    lst = []
    # s = ''
    while dividend > 0 and dividend not in lst:
        lst.append(dividend)
    #    s += str(dividend // d)
        dividend = dividend % d
        if dividend < d: dividend *= 10 # bring down a zero        
    # print(d, s, lst)
    if dividend in lst:
        return len(lst) - lst.index(dividend)
    else: 
        return 0

gen = (d for d in range(1, 1000))
print (max(gen, key = lambda d: fraction(d)))