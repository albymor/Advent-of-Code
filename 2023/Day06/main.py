import math

with open('input.txt', 'r') as f:
    data = f.read()

test = """Time:      7  15   30
Distance:  9  40  200"""   

def get_part_one(data):
    lines = data.split('\n')

    time = list(map(int, lines[0].split(':')[-1].split()))
    distance = list(map(int, lines[1].split(':')[-1].split()))

    prod = 1

    for t, d in zip(time, distance):
        a = (-t + math.sqrt(t**2 - 4*d))/(-2)
        b = (-t - math.sqrt(t**2 - 4*d))/(-2)

        a1 = math.floor(a)
        b1 = math.ceil(b)

        l = len(range(a1+1, b1))

        prod *= l

    return prod

assert get_part_one(test) == 288
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    time = int(''.join(lines[0].split(':')[-1].split()))
    distance = int(''.join(lines[1].split(':')[-1].split()))

    t = time
    d = distance
    a = (-t + math.sqrt(t**2 - 4*d))/(-2)
    b = (-t - math.sqrt(t**2 - 4*d))/(-2)

    a1 = math.floor(a)
    b1 = math.ceil(b)

    l = len(range(a1, b1+1)[1:-1])


    return l

assert get_part_two(test) == 71503
print(f'Part 2: {get_part_two(data)}')

