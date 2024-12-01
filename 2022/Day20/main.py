from collections import deque
from copy import copy
from tqdm import tqdm


with open('input.txt', 'r') as f:
    data = f.read()

test = """1
2
-3
3
-2
0
4"""   

class Digit:
    def __init__(self, value, is_):
        self.value = value
        self.is_ = is_
        self.was = is_
    
    def __repr__(self):
        return f'{self.value}'

    def __lt__(self, other):
        return self.is_ < other.is_

    def __le__(self, other):
        return self.is_ <= other.is_

    def __eq__(self, other):
        return self.is_ == other.is_

    def __ne__(self, other):
        return self.is_ != other.is_

    def __gt__(self, other):
        return self.is_ > other.is_

    def __ge__(self, other):
        return self.is_ >= other.is_


def print_digits(digits):
    dd = copy(digits)
    dd.sort()
    print(dd)

def get_part_one(data):
    lines = data.split('\n')

    seq = list(map(int, lines))

    # map to digits
    digits = []
    digits_dict = {}
    for i in range(len(seq)):
        digits.append(Digit(seq[i], i))
        if seq[i] == 0:
            zero = digits[i]
        digits_dict[i] = digits[i]

    print_digits(digits)

    for k in tqdm(digits_dict):
        now = digits_dict[k]
        idx = digits.index(digits_dict[k])
        digits.remove(digits_dict[k])
        new_pos = (idx + digits_dict[k].value) % (len(digits))
        digits.insert(new_pos, digits_dict[k])
        
    idx = digits.index(zero)

    gg = list(map(lambda x: (x+idx)%(len(digits)), [1000, 2000, 3000]))

    print(sum(digits[i].value for i in gg))


    return 0
# assert get_part_one(test) == 0
# print(f'Part 1: {get_part_one(data)}')


# part 2 

import itertools
def get_part_two(data):
    lines = data.split('\n')

    seq = list(map(int, lines))

    # map to digits
    digits = []
    digits_dict = {}
    for i in range(len(seq)):
        digits.append(Digit(seq[i]*811589153, i))
        if seq[i] == 0:
            zero = digits[i]
        digits_dict[i] = digits[i]

    print_digits(digits)

    keys = itertools.cycle(list(digits_dict.keys()))

    for _ in tqdm(range(10)):
        for k in digits_dict:
        #print(k)
            now = digits_dict[k]
            idx = digits.index(digits_dict[k])
            digits.remove(digits_dict[k])
            new_pos = (idx + digits_dict[k].value) % (len(digits))
            digits.insert(new_pos, digits_dict[k])
            #print(digits)
        
    idx = digits.index(zero)

    gg = list(map(lambda x: (x+idx)%(len(digits)), [1000, 2000, 3000]))

    print(sum(digits[i].value for i in gg))


    return 0
assert get_part_two(test) == 0
print(f'Part 1: {get_part_two(data)}')

