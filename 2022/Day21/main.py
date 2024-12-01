from collections import deque
from copy import copy
from tqdm import tqdm


with open('input.txt', 'r') as f:
    data = f.read()

test = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""   

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

def get_part_one(data):
    lines = data.split('\n')
    ops = []
    constants = {}
    for line in lines:
        if '+' in line or '*' in line or '/' in line or '-' in line:
            aa = line.replace(':', ' =').split(' ')
            ops.append(Operation(aa[0], aa[2], aa[3], aa[4]))
        else:
            k, v = line.split(': ')
            constants[k] = int(v)


    while len(ops) > 0:
        for op in ops:
            if op.solve(constants):
                constants[op.res] = op.numeric
                ops.remove(op)
                break


    print(ops, constants)


    return int(constants['root'])
#assert get_part_one(test) == 152
#print(f'Part 1: {get_part_one(data)}')


# part 2 

from z3 import *

def get_part_two(data):
    lines = data.split('\n')
    ops = {}
    constants = {}
    for line in lines:
        if '+' in line or '*' in line or '/' in line or '-' in line:
            aa = line.replace(':', ' =').split(' ')
            if 'root' in line:
                root = Operation(aa[0], aa[2], aa[3], aa[4])
            else:
                ops[aa[0]] = Operation(aa[0], aa[2], aa[3], aa[4])
        else:
            if 'humn' in line:
                continue
            k, v = line.split(': ')
            constants[k] = int(v)


    vars_ = {'humn': Real('humn')}
    for x in  list(ops.keys())+list(constants.keys()):
        vars_[x] = Real(x)

    s = Solver()
    for op in ops.values():
        s.add(op.solve2(vars_))

    s.add(vars_[root.a] == vars_[root.b])

    # add constants
    for k, v in constants.items():
        s.add(vars_[k] == v)

    print(s.check())
    return s.model().eval(vars_['humn'])

assert get_part_two(test) == 301
print(f'Part 2: {get_part_two(data)}')

