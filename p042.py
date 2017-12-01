import math

def is_triangle(n):
    # 8n + 1 is a perfect square
    # by applying b^2-4ac to formula n^2/2 + n/2 = c
    square = 8*n + 1
    rt = int(math.sqrt(square))
    if rt * rt == square: return True
    return False

def coded(s):
    return sum(ord(ch) - ord('A') + 1 for ch in s)

with open('p042_words.txt') as f:
    words = [word.strip('"') for word in f.readline().split(',')]
    print(sum(1 for word in words if is_triangle(coded(word))))