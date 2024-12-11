with open('input.txt', 'r') as f:
    data = f.read()

test = """125 17"""

cache = {}

from aoc.utils import timeit
from functools import lru_cache

def compute(tok, iterations=75):
    if (tok, iterations) in cache:
        print('hit', tok, end='\r')
        return cache[(tok, iterations)]
    
    el = tok

    res = []
    if iterations == 0:
        res.append(tok)
        return res
    #for i in range(iterations):
    tmp = []
    if el == 0:
        tmp.append(1)
    elif len(str(el))%2 == 0:
        a = int(str(el)[:len(str(el))//2])
        b = int(str(el)[len(str(el))//2:])
        tmp.append(a)
        tmp.append(b)
    else:
        tmp.append(el*2024)

    for el in tmp:
        res += compute(el, iterations-1)

    cache[(tok, iterations)] = res

    return res


from tqdm import tqdm

@timeit
def get_part_one(data):
    data = list(map(int, data.split(' ')))

    res = []

    for el in tqdm(data):
        r = compute(el)
        cache[el] = r
        for e in r:
            res.append(e)
    print(len(res))

    return len(res)

assert get_part_one(test) == 55312
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    return 1

assert get_part_two(test) == 1
print(f'Part 2: {get_part_two(data)}')

