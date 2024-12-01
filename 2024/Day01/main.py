with open('input.txt', 'r') as f:
    data = f.read()

test = """3   4
4   3
2   5
1   3
3   9
3   3"""   

def get_part_one(data):
    lines = data.split('\n')
    vec = []
    for line in lines:
        vec.append(list(map(int, line.split('   '))))

    vec =  list(map(list,list(zip(*vec))))
    dx = vec[0]
    sx = vec[1]
    dx.sort()
    sx.sort()

    res = 0
    for el in zip(dx,sx):
        res += abs(el[0]-el[1])

    return res

assert get_part_one(test) == 11
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')
    vec = []
    for line in lines:
        vec.append(list(map(int, line.split('   '))))

    vec =  list(map(list,list(zip(*vec))))
    dx = vec[0]
    sx = vec[1]

    res = 0
    for el in dx:
        res += (el*sx.count(el))

    return res

assert get_part_two(test) == 31
print(f'Part 2: {get_part_two(data)}')

