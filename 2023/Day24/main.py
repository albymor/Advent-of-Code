import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from itertools import combinations

from z3 import *
x = Real('x')
y = Real('y')
z = Real('z')
t = Real('t')


with open('input.txt', 'r') as f:
    data = f.read()

test = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

class Eq:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def __repr__(self):
        return f'({self.a}, {self.b}, {self.c})'


class Particle:
    def __init__(self, x0, y0, z0, vx0, vy0, vz0):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.vx0 = vx0
        self.vy0 = vy0
        self.vz0 = vz0
        self.position = (x0, y0, z0)
        self.velocity = (vx0, vy0, vz0)

        self.eq = Eq(1, -(vx0/vy0), (vx0*y0/vy0 - x0))

    def __repr__(self):
        return f'Particle({self.position}, {self.velocity})'

    def trajectory_calc(self, t0, t1):
        for t in range(t0, t1):
            x = self.position[0] + t * self.velocity[0]
            y = self.position[1] + t * self.velocity[1]

            self.trajectory.append((x, y))

    def is_in_future(self, x):
        t = (x-self.x0)/self.vx0
        return  t>=0  


def get_part_one(data, _min, _max):
    lines = data.split('\n')

    particles = []

    for line in lines:
        pos, vel = line.split('@')
        pos = list(map(int, pos.split(',')))
        vel = list(map(int, vel.split(',')))
        particles.append(Particle(*pos, *vel))

    total = 0
    for p0, p1 in combinations(particles, 2):

        try:      
            x = (p0.eq.c * p1.eq.b - p1.eq.c * p0.eq.b) / (-p0.eq.a * p1.eq.b + p1.eq.a * p0.eq.b)
            y = (p0.eq.c * p1.eq.a - p1.eq.c * p0.eq.a) / (p0.eq.a * p1.eq.b - p1.eq.a * p0.eq.b)

        except ZeroDivisionError:
            continue

        if p0.is_in_future(x) and p1.is_in_future(x) and _min <= x <= _max and _min <= y <= _max:
            total += 1



    return total


assert get_part_one(test, 7, 27) == 2
print(f'Part 1: {get_part_one(data, 200000000000000, 400000000000000)}')


# part 2
def get_part_two(data):
    lines = data.split('\n')

    particles = []

    for line in lines:
        pos, vel = line.split('@')
        pos = list(map(int, pos.split(',')))
        vel = list(map(int, vel.split(',')))
        particles.append(Particle(*pos, *vel))

    s = Solver()
    vx, vy, vz = Ints('vx vy vz')
    x, y, z = Ints('x y z')

    for i, p in enumerate(particles):
        t = Int(f't_{i}')
        s.add(vx*t+x == p.vx0*t+p.x0)
        s.add(vy*t+y == p.vy0*t+p.y0)
        s.add(vz*t+z == p.vz0*t+p.z0)
        s.add(t>=0)

    assert s.check() == sat
    m = s.model()
    total = s.model().eval(x+y+z)

    return total


assert get_part_two(test) == 47
print(f'Part 2: {get_part_two(data)}')
