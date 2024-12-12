from aoc.utils import timeit

with open('input.txt', 'r') as f:
    data = f.read()

test = """125 17"""   
from tqdm import tqdm

@timeit
def get_part_one(data):
    data = list(map(int, data.split(' ')))

    for i in tqdm(range(25)):
        tmp = []
        for el in data:
            if el == 0:
                tmp.append(1)
            elif len(str(el))%2 == 0:
                a = int(str(el)[:len(str(el))//2])
                b = int(str(el)[len(str(el))//2:])
                tmp.append(a)
                tmp.append(b)
            else:
                tmp.append(el*2024)

        data = tmp

    return len(data)

assert get_part_one(test) == 55312
print(f'Part 1: {get_part_one(data)}')

from functools import cache

@cache
def splitter(stones, step):
    res = 0
    if step == -1:
        return 1
    
    for stone in stones:
        tmp=[]
         
        if stone == 0:
            tmp.append(1)
        elif len(str(stone))%2 == 0:
            a = int(str(stone)[:len(str(stone))//2])
            b = int(str(stone)[len(str(stone))//2:])
            tmp.append(a)
            tmp.append(b)
        else:
            tmp.append(stone*2024)

        res += splitter(tuple(tmp), step-1)

    return res



# part 2 
@timeit
def get_part_two(data):
    data = tuple(map(int, data.split(' ')))

    return splitter(data, 75)

print(f'Part 2: {get_part_two(data)}')

