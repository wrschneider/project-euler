from utils import text_to_int_array

s = ""
with open("p067_triangle.txt") as f:
    s = f.read()

arr = text_to_int_array(s)

d = {}
def helper(start_r, start_c):
    if (start_r, start_c) in d:
        return d[(start_r, start_c)]
    start_num = arr[start_r][start_c]
    if start_r == len(arr) - 1:
        return start_num
    d[(start_r, start_c)] = start_num + max(helper(start_r + 1, start_c), helper(start_r + 1, start_c + 1))
    return d[(start_r, start_c)]
    
print (helper(0, 0))