from tqdm import tqdm
from functools import cache

with open('input.txt', 'r') as f:
    data = f.read()

test = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


@cache
def decompose(pattern, towels):
    res = 0
    if len(pattern) == 0:
        return True
    
    s = pattern[0]

    possible = [x for x in towels if x.startswith(s)]
    for p in possible:
        
        red = pattern[len(p):] 
        if len(pattern) >=  len(p):
            sub = pattern[:len(p)]
            if sub == p:
                ret = decompose(red, towels)
                if ret:
                    res += ret
                    continue
                else: continue
            else: 
                continue
    
    return res


def get_part_one(data):
    towels, patters = data.split('\n\n')
    towels = towels.split(', ')
    patters = patters.split('\n')

    p1 = 0
    p2 = 0

    for p in tqdm(patters):
        ret = decompose(p, tuple(towels))
        if ret:
            p2 += ret
            p1 += 1

    return p1

assert get_part_one(test) == 6
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    towels, patters = data.split('\n\n')
    towels = towels.split(', ')
    patters = patters.split('\n')

    p1 = 0
    p2 = 0

    for p in tqdm(patters):
        ret = decompose(p, tuple(towels))
        if ret:
            p2 += ret
            p1 += 1

    return p2

assert get_part_two(test) == 16
print(f'Part 2: {get_part_two(data)}')

