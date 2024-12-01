from collections import deque
from copy import copy
from tqdm import tqdm
import re


with open('input.txt', 'r') as f:
    data = f.read()

test = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""   

class Operation:
    def __init__(self, res, a, op, b):
        self.op = op
        self.res = res
        self.a = a
        self.b = b

        self.numeric = 0

    def __repr__(self):
        return f'{self.res} = {self.a} {self.op} {self.b}'

    def solve(self, constants_dict):
        if self.a in constants_dict and self.b in constants_dict:
            if self.op == '+':
                self.numeric = constants_dict[self.a] + constants_dict[self.b]
            elif self.op == '*':
                self.numeric = constants_dict[self.a] * constants_dict[self.b]
            elif self.op == '/':
                self.numeric = constants_dict[self.a] / constants_dict[self.b]
            elif self.op == '-':
                self.numeric = constants_dict[self.a] - constants_dict[self.b]
            return True
        return False


    def solve2(self, vars):
        if self.op == '+':
            return vars[self.res] == vars[self.a] + vars[self.b]
        elif self.op == '*':
            return vars[self.res] == vars[self.a] * vars[self.b]
        elif self.op == '/':
            return vars[self.res] == vars[self.a] / vars[self.b]
        elif self.op == '-':
            return vars[self.res] == vars[self.a] - vars[self.b]


def rotate(lines, pivot,  direction):
    new_lines = []
    for line in lines:
        if direction == 'R':
            new_lines.append(((line[0]-pivot)*complex(0,-1), line[1]))
        elif direction == 'L':
            new_lines.append(((line[0]-pivot)*complex(0,1), line[1]))
        else:
            raise Exception('unknown direction')
    return new_lines
    

def get_part_one(data):
    map_raw, instructions = data.split('\n\n')
    map_raw = map_raw.split('\n')

    has_start = False
    lines = []
    for y, line in enumerate(map_raw):
        for x, c in enumerate(line):
            if c == ' ':
                continue
            elif c == '#':
                lines.append((complex(x, y), True))
            elif c == '.':
                aa = (complex(x, y), False)
                if not has_start:
                    start = aa
                    current_x = x
                    current_y = y
                    has_start = True
                lines.append(aa)
            else:
                raise Exception('unknown char')


    instructions = re.findall(r"(\d+)(\w)", instructions)

    current_pos = start[0]
    dd = 1 
    for ins in instructions:
        for i in range(int(ins[0])+1):
            current_pos += dd
            if (current_pos, True) in lines:
                current_pos -= dd
                if ins[1] == 'R':
                    dd *= complex(0, 1)
                elif ins[1] == 'L':
                    dd *= complex(0, -1)
                break
            elif (current_pos, False) in lines:
                continue
            else:
                #wrap around
                current_pos -= dd
                while (current_pos, False) in lines or (current_pos, True) in lines:
                    current_pos -= dd
                current_pos += dd
        else:
            current_pos -= dd
            if ins[1] == 'R':
                dd *= complex(0, 1)
            elif ins[1] == 'L':
                dd *= complex(0, -1)




    return 0
assert get_part_one(test) == 152
#print(f'Part 1: {get_part_one(data)}')


# part 2 

# from z3 import *

# def get_part_two(data):
#     lines = data.split('\n')
#     ops = {}
#     constants = {}
#     for line in lines:
#         if '+' in line or '*' in line or '/' in line or '-' in line:
#             aa = line.replace(':', ' =').split(' ')
#             if 'root' in line:
#                 root = Operation(aa[0], aa[2], aa[3], aa[4])
#             else:
#                 ops[aa[0]] = Operation(aa[0], aa[2], aa[3], aa[4])
#         else:
#             if 'humn' in line:
#                 continue
#             k, v = line.split(': ')
#             constants[k] = int(v)


#     vars_ = {'humn': Real('humn')}
#     for x in  list(ops.keys())+list(constants.keys()):
#         vars_[x] = Real(x)

#     s = Solver()
#     for op in ops.values():
#         s.add(op.solve2(vars_))

#     s.add(vars_[root.a] == vars_[root.b])

#     # add constants
#     for k, v in constants.items():
#         s.add(vars_[k] == v)

#     print(s.check())
#     return s.model().eval(vars_['humn'])

# assert get_part_two(test) == 301
# print(f'Part 2: {get_part_two(data)}')

