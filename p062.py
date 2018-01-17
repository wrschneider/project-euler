import utils

cubes = set(str(i**3) for i in range(0, 10000))
digit_map = {}
for cube in cubes:
    key = sum(int(ch) for ch in cube)
    if key not in digit_map:
        digit_map[key] = []
    digit_map[key].append(cube)

MIN_LEN = 5
def gen():
    for digit_sum, cubelist in digit_map.items():
        if len(cubelist) < MIN_LEN: continue # not a possible answer so don't bother checking permuts
        for cube in cubelist:
            permuts = [p for p in cubelist if p >= cube and utils.check_permutation(cube, p)]
            if len(permuts) == MIN_LEN: yield min(permuts)

print(min(gen()))
