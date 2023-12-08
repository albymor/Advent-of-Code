from itertools import cycle

with open('input.txt', 'r') as f:
    data = f.read()

test = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
        self.visited = False

    def __str__(self):
        return f'{self.name} = {self.left}, {self.right}'

    def __repr__(self):
        return f'{self.name} = {self.left}, {self.right}'

def get_part_one(data):
    lines = data.split('\n')

    procedure = cycle(lines[0])
    steps = lines[2:]

    nodes = {}

    for step in steps:
        name = step[0:3]
        left = step[7:10]
        right = step[12:15]
        nodes[name] = Node(name, left, right)


    n = nodes['AAA']

    steps = 0

    while n.name != 'ZZZ':
        if next(procedure) == 'R':
            n = nodes[n.right]
        else:
            n = nodes[n.left]

        steps += 1

    return steps

assert get_part_one(test) == 2
assert get_part_one(test2) == 6
print(f'Part 1: {get_part_one(data)}')


test3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

import numpy as np

# part 2 
def get_part_two(data):
    lines = data.split('\n')

    procedure = cycle(lines[0])
    steps = lines[2:]

    nodes = {}

    for step in steps:
        name = step[0:3]
        left = step[7:10]
        right = step[12:15]
        nodes[name] = Node(name, left, right)

    starting = []

    for n in nodes:
        if 'A' in n:
            starting.append(nodes[n])

    lengths = []

    # we probably have loops. Calculate the number of steps for 
    # each starting point and then find the LCM of all of them
    for n in starting:
        steps = 0
        while not ('Z' in n.name):
            if next(procedure) == 'R':
                n = nodes[n.right]
            else:
                n = nodes[n.left]

            steps += 1

        lengths.append(steps)

    lcm_result = np.lcm.reduce(np.array(lengths))

    return lcm_result

assert get_part_two(test3) == 6
print(f'Part 2: {get_part_two(data)}')

