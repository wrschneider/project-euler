import math

n = 20
# solve recurrence
# T(m, n) = 1 if m=0 or n=0
# T(m-1, n) + T(m, n-1) otherwise
# Maybe there is closed form for this? (feels like Pascal's triangle on its side)

arr = [[1 for i in range (0, n+1)] for i in range(0, n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

print(arr[n][n])

# via combinations

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

print (nCr(40,20))