n = 100

sum_of_squares = sum(i*i for i in range(1, n+1))
_sum = sum(i for i in range(1, n+1))
square_of_sum = _sum * _sum
print(square_of_sum - sum_of_squares)
