def sum_power_digits(n, pow):
    return sum(int(ch) ** pow for ch in str(n))

# Cannot be seven digits because 9**5 * 7 is only a six-digit number 
#  the digits won't add up to enough 
print(sum(i for i in range(2, 9**5 * 7) if i == sum_power_digits(i, 5)))