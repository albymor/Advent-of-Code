import re

with open('input.txt', 'r') as f:
    data = f.read()

test = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(4* mul(6,9! ?(12,34) mul ( 2 , 4 )"""   
test_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def get_part_one(data):
    data = data.replace('\n', '')
    regex = r"mul\((\d+),(\d+)\)"
    matches = re.finditer(regex, data, re.MULTILINE)

    res = 0    

    for matchNum, match in enumerate(matches, start=1):
        nums = list(map(int,match.groups()))
        res += (nums[0]*nums[1])
        


    return res

assert get_part_one(test) == 161
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    data = data.replace('\n', '')
    regex = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

    res = 0
    

    matches = re.finditer(regex, data, re.MULTILINE)

    coeff = 1

    for matchNum, match in enumerate(matches, start=1):
        
        instruction = match.group()
        if "do()" in instruction:
            coeff = 1
        elif "don't()" in instruction:
            coeff = 0
        elif "mul" in instruction:
            nums = list(map(int,match.groups()))
            res += (coeff*nums[0]*nums[1])   


    return res


assert get_part_two(test_2) == 48
print(f'Part 2: {get_part_two(data)}')

