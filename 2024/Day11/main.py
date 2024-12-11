with open('input.txt', 'r') as f:
    data = f.read()

test = """125 17"""   
from tqdm import tqdm
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
        print(data)

    print(len(data))

    return 0

assert get_part_one(test) == 0
#print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    return 1

assert get_part_two(test) == 1
print(f'Part 2: {get_part_two(data)}')

