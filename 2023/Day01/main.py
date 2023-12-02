import re


with open('input.txt', 'r') as f:
    data = f.read()

test = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""   

def get_part_one(data):
    lines = data.split('\n')

    total = 0

    for line in lines:

        dig =re.findall(r'(\d)', line)
        dig = list(map(int, dig))
        total += (dig[0]*10+(dig[-1]))

    return total

assert get_part_one(test) == 142
print(f'Part 1: {get_part_one(data)}')


test2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


# part 2 
def get_part_two(data):
    lines = data.split('\n')

    
    total = 0

    for line in lines:

        # this mapping allow overlap such as  'eightwo' -> 82, using re we find only the 8
        for i, n in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            line = line.replace(n, n + str(i+1) + n)

        dig =re.findall(r'(\d)', line)
        total += (int(dig[0])*10+int(dig[-1]))

    return total

assert get_part_two(test2) == 281
print(f'Part 2: {get_part_two(data)}')

