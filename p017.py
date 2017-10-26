import re

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

ones_and_teens = ones + ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def spell_num(n):
    if n == 1000: return "one thousand"

    s = ""

    hundreds_place = n // 100
    mod_100 = n % 100
    if hundreds_place:
        s = s + ones[hundreds_place] + " hundred "
        if mod_100: s = s + "and "

    if mod_100 < 20:
        s = s + ones_and_teens[mod_100]
        return s

    tens_place = mod_100 // 10
    mod_10 = mod_100 % 10
    if tens_place:
        s = s + tens[tens_place] 
        if mod_10: s = s + "-"
    if mod_10:
        s = s + ones[mod_10]
    return s

print (sum(len(re.sub('[ \-]', '', spell_num(i))) for i in range(0, 1001)))
