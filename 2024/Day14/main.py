with open('input.txt', 'r') as f:
    data = f.read()

test = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""   


import re

regex = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

class Robot:
    def __init__(self, x, y, vx ,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def point_t(self, t, max_x, max_y):
        x = (self.x +(self.vx*t))%max_x
        y = (self.y + (self.vy*t))%max_y

        return (x, y)
    
    def __repr__(self):
        return f'Robot({self.x}, {self.y}, {self.vx}, {self.vy})'



def get_part_one(data, max_x, max_y):
    lines = data.split('\n')
    robots = []
    for l in lines:
        match = list(map(int, list(re.findall(regex, l)[0])))
        robots.append(Robot(*match))

    finals = {}
    for r in robots:

        pos = r.point_t(100, max_x, max_y)
        if pos in finals:
            finals[pos] += 1
        else:
            finals[pos] = 1

    quad = {}

    
    for k, v in finals.items():
        m_x = max_x//2
        m_y = max_y//2
        if k[0] == m_x or k[1] == m_y:
            continue

        qx = 0 if 0<= k[0] < m_x else 1
        qy = 0 if 0<= k[1] < m_y else 1

        if (qx, qy) in quad:
            quad[(qx, qy)] += v
        else:
            quad[(qx, qy)] = v

    res = 1
    for k, v in quad.items():
        res *= v

    return res


assert get_part_one(test, 11, 7) == 12
print(f'Part 1: {get_part_one(data, 101, 103)}')

def calc_entropy(grid):
    counts = np.bincount(grid.flatten())
    probs = counts[counts > 0] / counts.sum()
    return -np.sum(probs * np.log2(probs))

# part 2 
import numpy as np
from matplotlib import pyplot as plt
def get_part_two(data, max_x, max_y):
    lines = data.split('\n')
    robots = []
    for l in lines:
        match = list(map(int, list(re.findall(regex, l)[0])))
        robots.append(Robot(*match))

    v = []
    for i in range(10000):
        mappa = np.zeros((max_x, max_y)).astype(int)
        for r in robots:
            pos = r.point_t(i, max_x, max_y)
            mappa[pos] += 1

        v.append(calc_entropy(mappa))

    plt.plot(v)
    plt.show()

                    
    return np.array(v).argmin()

#assert get_part_two(test) == 1
print(f'Part 2: {get_part_two(data, 101, 103)}')

