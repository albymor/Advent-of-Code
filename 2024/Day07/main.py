with open('input.txt', 'r') as f:
    data = f.read()

test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


class OP:
    def __init__(self, raw):
        res, nums = raw.split(':')
       
        self.res = int(res)
        self.nums = list(map(int, nums.strip().split(' ')))

    def __repr__(self):
        return f"{self.res}: {self.nums}"
    
from copy import deepcopy
def resolve(c_num, q, res, cop=None):
    if len(q) == 0:
        return False
    
    if c_num == None:
        c_num = q.popleft()
    
    num = q.popleft()

    # try with the addition 
    if (c_num + num == res):
        return True
    
    if c_num * num == res:
        return True
    
    else:
        return resolve(c_num+num, deepcopy(q), res, '+') or resolve(c_num*num, deepcopy(q), res, '*')

def resolve2(c_num, q, res, cop=None):
    if len(q) == 0:
        return False
    
    if c_num == None:
        c_num = q.popleft()
    
    num = q.popleft()

    # try with the addition 
    if (c_num + num == res):
        return True
    
    if c_num * num == res:
        return True

    if int(str(c_num)+str(num)) == res:
        return True
    
    else:
        return resolve2(c_num+num, deepcopy(q), res, '+') or resolve2(c_num*num, deepcopy(q), res, '*') or resolve2(int(str(c_num)+str(num)), deepcopy(q), res, '||')
    

from collections import deque
from tqdm import tqdm
        
def get_part_one(data):
    lines = data.split('\n')

    ops = [OP(l) for l in lines]

    ops = [(p.nums, p.res) for p in ops]

    res = 0

    for op in tqdm(ops):
        q = deque(op[0])
        if op[1] == 292:
            pass
        if resolve(None, q, op[1]):
            res += op[1]

    return res

assert get_part_one(test) == 3749
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    ops = [OP(l) for l in lines]

    ops = [(p.nums, p.res) for p in ops]

    res = 0

    for op in tqdm(ops):
        q = deque(op[0])
        if op[1] == 292:
            pass
        if resolve2(None, q, op[1]):
            res += op[1]

    return res

assert get_part_two(test) == 11387
print(f'Part 2: {get_part_two(data)}')

