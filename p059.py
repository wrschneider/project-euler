f = open("p059_cipher.txt")
encrypted = [int(n) for n in f.readline().split(',')]

def keys_to_try():
    a = ord('a')
    z = ord('z')
    for p1 in range(a,z):
        for p2 in range(a,z):
            for p3 in range(a,z):
                yield (p1, p2, p3)

high_count = 0
for key in keys_to_try():
    decrypted = [encrypted[i] ^ key[i % 3] for i in range(len(encrypted))]
    space_count = sum(1 for c in decrypted if c == ord(" "))
    if space_count > high_count:
        print(space_count, sum(decrypted), ''.join(chr(c) for c in decrypted))
        high_count = space_count


