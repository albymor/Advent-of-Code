with open('input.txt', 'r') as f:
    data = f.read()

test = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""" 


def derivate(data):
    d_data = []
    for i in range(len(data)-1):
        d_data.append(data[i+1] - data[i])

    if sum(d_data) != 0:
        pred = derivate(d_data)
    else:
        return data[-1]
    
    return pred + data[-1]


def get_part_one(data):
    lines = data.split('\n')

    total = 0

    for line in lines:
        total += derivate(list(map(int, line.split(' '))))

    return total

assert get_part_one(test) == 114
print(f'Part 1: {get_part_one(data)}')


# part 2 
test2 = "10 13 16 21 30 45"

def derivate2(data):
    d_data = []
    for i in range(len(data)-1):
        d_data.append(data[i+1] - data[i])

    if sum(d_data) != 0:
        pred = derivate2(d_data)
    else:
        return data[0]
    
    return data[0] - pred


def get_part_two(data):
    lines = data.split('\n')

    total = 0

    for line in lines:
        total += derivate2(list(map(int, line.split(' '))))

    return total

assert get_part_two(test) == 2
assert get_part_two(test2) == 5
print(f'Part 2: {get_part_two(data)}')

