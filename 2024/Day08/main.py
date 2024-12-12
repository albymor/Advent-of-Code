with open('input.txt', 'r') as f:
    data = f.read()

test = """..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
.........."""


test2 ="""..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......#...
..........
.........."""

test3 = """..........
...#......
#.........
....a.....
........a.
.....a....
..#.......
......A...
..........
.........."""

test4 = """......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#."""

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

class Antenna:
    def __init__(self, c, x, y):
        self.c = c
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.c} @ ({self.x},{self.y})"


import math

def point_on_line(x1, y1, m, d):
    # Calculate direction components
    dx = d / math.sqrt(1 + m**2)
    dy = m * dx

    # Two possible points
    x2_pos = x1 + dx
    y2_pos = y1 + dy

    x2_neg = x1 - dx
    y2_neg = y1 - dy

    return (x2_pos, y2_pos), (x2_neg, y2_neg)

def calc_anti(pairs, x_max, y_max):
    anti = []
    for pair in pairs:
        a1 = pair[0]
        a2 = pair[1]

        dx = (a1.x-a2.x)
        dy = (a1.y-a2.y)

        if dy == 0: #vertical
            anti.append((dx+min([a1.x, a2.x]), a1.y))
            continue

        max_x = max([a1.x, a2.x])
        min_x = min([a1.x, a2.x])
        max_y = max([a1.y, a2.y])
        min_y = min([a1.y, a2.y])        


        m = dx/dy

        dx =abs(dx)
        dy=abs(dy)

        if m>0:
            anti.append((max_x+dx, max_y+dy))
            anti.append((min_x-dx, min_y-dy))
        else:
            anti.append((max_x+dx, min_y-dy))
            anti.append((min_x-dx, max_y+dy))

    anti_clean = []

    for a in anti:
        if 0<= a[0] <= x_max and 0<= a[1] <= y_max:
            anti_clean.append(a) 
    
    return anti_clean


from itertools import combinations

def get_part_one(data):
    lines = data.split('\n')

    x_max = len(lines[0])-1
    y_max= len(lines)-1

    antennas = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in chars:
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append(Antenna(c, x, y))
    
    un = set()

    for t in antennas:
        ant_list = antennas[t]
        pairs = list(combinations(ant_list, 2))
        anti = calc_anti(pairs, x_max, y_max)
        for a in anti:
            un.add(a)

    return len(un)

assert get_part_one(test) == 2
assert get_part_one(test2) == 4
assert get_part_one(test3) == 4
assert get_part_one(test4) == 14
print(f'Part 1: {get_part_one(data)}')



def calc_anti2(pairs, x_max, y_max):
    anti = []
    for pair in pairs:
        a1 = pair[0]
        a2 = pair[1]

        dx = (a1.x-a2.x)
        dy = (a1.y-a2.y)

        if dy == 0: #vertical
            anti.append((dx+min([a1.x, a2.x]), a1.y))
            continue

        max_x = max([a1.x, a2.x])
        min_x = min([a1.x, a2.x])
        max_y = max([a1.y, a2.y])
        min_y = min([a1.y, a2.y])        


        m = dx/dy

        dx =abs(dx)
        dy=abs(dy)

        if m>0:
            anti_pos = (max_x, max_y)
            while (0,0) <= anti_pos <= (x_max, y_max):
                anti.append(anti_pos)
                anti_pos = tuple(map(sum, zip(anti_pos, (dx, dy))))
            anti_pos = (min_x, min_y)
            while (0,0) <= anti_pos <= (x_max, y_max):
                anti.append(anti_pos)
                anti_pos = tuple(map(sum, zip(anti_pos, (-dx, -dy))))
        else:
            anti_pos = (max_x, min_y)
            while (0,0) <= anti_pos <= (x_max, y_max):
                anti.append(anti_pos)
                anti_pos = tuple(map(sum, zip(anti_pos, (dx, -dy))))
            anti_pos = (min_x, max_y)
            while (0,0) <= anti_pos <= (x_max, y_max):
                anti.append(anti_pos)
                anti_pos = tuple(map(sum, zip(anti_pos, (-dx, dy))))

    anti_clean = []

    for a in anti:
        if 0<= a[0] <= x_max and 0<= a[1] <= y_max:
            anti_clean.append(a) 
    
    return anti_clean

# part 2 
def get_part_two(data):
    lines = data.split('\n')

    x_max = len(lines[0])-1
    y_max= len(lines)-1

    antennas = {}

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in chars:
                if c not in antennas:
                    antennas[c] = []
                antennas[c].append(Antenna(c, x, y))
    
    un = set()

    for t in antennas:
        ant_list = antennas[t]
        pairs = list(combinations(ant_list, 2))
        anti = calc_anti2(pairs, x_max, y_max)
        for a in anti:
            un.add(a)

    return len(un)


test4 = """T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
.........."""

assert get_part_two(test4) == 9
print(f'Part 2: {get_part_two(data)}')

