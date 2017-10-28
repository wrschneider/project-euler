days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(y, m):
    days = days_in_months[m]
    if m == 1 and (y % 400 == 0 or y % 4 == 0 and y % 100 != 0):
        days += 1
    return days

def gen():
    day = 1
    for y in range(1900, 2001):
        for m in range(0, len(days_in_months)):
            day = (day + days_in_month(y, m)) % 7
            yield (y, m, day)

print(sum(1 for (y,m,d) in gen() if d == 0 and y >= 1901 and y < 2001))