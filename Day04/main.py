with open('input.txt', 'r') as f:
    data = f.read()

test="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def get_range(r):
    r = r.split('-')
    r = list(range(int(r[0]),int(r[1])+1))
    return r


def get_part_one(data):
    data = data.split('\n')
    overlap = 0
    for d in data:
        r1 , r2 = d.split(',')
        r1 = get_range(r1)
        r2 = get_range(r2)
        if len(set(r1)-set(r2)) == 0  or  len(set(r2)-set(r1)) == 0:
            overlap += 1

    return overlap

assert get_part_one(test) == 2
print(f'Part 1: {get_part_one(data)}')

# part 2


test = """5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


def get_part_two(data):
    data = data.split('\n')
    overlap = 0
    for d in data:
        r1 , r2 = d.split(',')
        r1 = get_range(r1)
        r2 = get_range(r2)
        if len(set(r1)&set(r2)) > 0:
            overlap += 1

    return overlap

assert get_part_two(test) == 4
print(f'Part 2: {get_part_two(data)}')
