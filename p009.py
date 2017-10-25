def check(i, j, k):
    return i < j and j < k and i**2 + j**2 == k**2    

def find(n):
    for i in range(1, n):
        for j in range(i, n - i):
            k = n - i - j
            if check(i, j, k): 
                return i * j * k
                
print (find(1000))