with open('input.txt', 'r') as f:
    data = f.read()

test = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def diff(data):
    d = []
    for i in range(1, len(data)):
        d.append(data[i]-data[i-1])

    return d


from copy import deepcopy


def get_part_one(data):
    lines = data.split('\n')
    data = [list(map(int, x.split(' '))) for x in lines]

    res = 0
    for d in data:
        d1 =diff(d)
        res += (all( -3 <= x <= -1 for x in d1) or all( 1 <= x <= 3 for x in d1))

    return res

assert get_part_one(test) == 2
print(f'Part 1: {get_part_one(data)}')


def check2(data, depth = 0):
    c_depth = depth+1
    if c_depth > 2:
        return False
    der = diff(data)
    if (all( -3 <= x <= -1 for x in der) or all( 1 <= x <= 3 for x in der)):
        return True

    for i, d in enumerate(data):
        dx = deepcopy(data)
        dx.pop(i)
        res = check2(dx, c_depth)
        if res:
            return True
        
    return False



# part 2 
def get_part_two(data):
    lines = data.split('\n')
    data = [list(map(int, x.split(' '))) for x in lines]

    res = 0
    for d in data:
        d1 =diff(d)
        res += check2(d)

    return res

assert get_part_two(test) == 4
print(f'Part 2: {get_part_two(data)}')

