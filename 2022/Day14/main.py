from itertools import zip_longest, tee
import functools
import numpy as np

with open('input.txt', 'r') as f:
    data = f.read()

test = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))


def print_map(rocks, sand):
    tmp = rocks.union(sand)
    rocks = np.array(list(rocks)).T
    sand = np.array(list(sand)).T
    tmp = np.array(list(tmp)).T
    offset = tmp[0].min()
    rocks[0] = rocks[0] - offset
    tmp[0] = tmp[0] - offset

    mp = np.zeros((tmp[1].max()+1, tmp[0].max()+1)).astype('<U1')
    mp[:] = '.'


    for x, y in zip(rocks[0], rocks[1]):
        mp[y, x] = '#'
    
    if sand.size:
        sand[0] = sand[0] - offset
        for x, y in zip(sand[0], sand[1]):
            mp[y, x] = 'o'

    for i, line in enumerate(mp):
        print(f"{i:<5}{''.join(line)}")
    
    
def get_part_one(data):
    lines = data.split('\n')

    rocks = set({})

    for line in lines:
        line = line.split(' -> ')
        scans = []
        for c in line:
            scans.append(list(map(int, c.split(','))))

        mm = pairwise(scans)

        for m in mm:
            if m[0][0] == m[1][0]:
                x = m[0][0]
                if m[0][1] > m[1][1]:
                    y = list(range(m[1][1], m[0][1]+1))
                else:
                    y = list(range(m[0][1], m[1][1]+1))
                for yy in y:
                    rocks.add((x, yy))
            elif m[0][1] == m[1][1]:
                y = m[0][1]
                if m[0][0] > m[1][0]:
                    x = list(range(m[1][0], m[0][0]+1))
                else:
                    x = list(range(m[0][0], m[1][0]+1))
                for xx in x:
                    rocks.add((xx, y))

    cave_floor = max([r[1] for r in rocks])+1

    start_pos = (500,0)
    counter = 0
    not_in_abyss = True
    sand = set({})
    while not_in_abyss:
        #print_map(rocks, sand)

        not_in_abyss, rocks, sand = solve(start_pos, rocks, sand, cave_floor)

        counter += 1

    return counter-1


def solve(start_pos, rocks, sand, cave_floor):
    next_y = start_pos[1]
    while True:
        next_y += 1
        current_pos = (start_pos[0], next_y)

        if next_y >= cave_floor:  #------------
            return (0, rocks, sand)
        if current_pos not in rocks and current_pos not in sand:
            continue
        elif current_pos in rocks or current_pos in sand:
            if (start_pos[0]-1, next_y) not in rocks and (start_pos[0]-1, next_y) not in sand:
                res = solve((start_pos[0]-1, next_y), rocks, sand, cave_floor)

                return res

            elif (start_pos[0]+1, next_y) not in rocks and (start_pos[0]+1, next_y) not in sand:
                res = solve((start_pos[0]+1, next_y), rocks, sand, cave_floor)

                return res

            else:
                sand.add((start_pos[0], next_y-1))
                return (1, rocks, sand)

assert get_part_one(test) == 24
print(f'Part 1: {get_part_one(data)}')


# part 2    
    
def get_part_two(data):
    lines = data.split('\n')

    rocks = set({})

    for line in lines:
        line = line.split(' -> ')
        scans = []
        for c in line:
            scans.append(list(map(int, c.split(','))))

        mm = pairwise(scans)

        for m in mm:
            if m[0][0] == m[1][0]:
                x = m[0][0]
                if m[0][1] > m[1][1]:
                    y = list(range(m[1][1], m[0][1]+1))
                else:
                    y = list(range(m[0][1], m[1][1]+1))
                for yy in y:
                    rocks.add((x, yy))
            elif m[0][1] == m[1][1]:
                y = m[0][1]
                if m[0][0] > m[1][0]:
                    x = list(range(m[1][0], m[0][0]+1))
                else:
                    x = list(range(m[0][0], m[1][0]+1))
                for xx in x:
                    rocks.add((xx, y))

    cave_floor = max([r[1] for r in rocks])

    rocks.add((500, cave_floor+2))
    cave_floor += 2


    start_pos = (500,0)
    counter = 0
    not_in_abiss = True
    sand = set({})
    while not_in_abiss:
        #print_map(rocks, sand)

        not_in_abiss, rocks, sand = solve2(start_pos, rocks, sand, cave_floor)

        counter += 1


    return counter-1


def solve2(start_pos, rocks, sand, cave_floor):
    next_y = start_pos[1]
    while True:

        if (start_pos[0], next_y) in rocks or (start_pos[0], next_y) in sand:
            return (0, rocks, sand)

        next_y += 1
        current_pos = (start_pos[0], next_y)

        
        if next_y >= cave_floor+1:  #------------
            next_y = cave_floor
            #return (0, rocks, sand)
        if current_pos not in rocks and current_pos not in sand and next_y < cave_floor:
            continue
        elif current_pos in rocks or current_pos in sand or next_y == cave_floor:
            if (start_pos[0]-1, next_y) not in rocks and (start_pos[0]-1, next_y) not in sand and next_y != cave_floor:
                res = solve2((start_pos[0]-1, next_y), rocks, sand, cave_floor)

                return res

            elif (start_pos[0]+1, next_y) not in rocks and (start_pos[0]+1, next_y) not in sand and next_y != cave_floor:
                res = solve2((start_pos[0]+1, next_y), rocks, sand, cave_floor)

                return res

            else:
                sand.add((start_pos[0], next_y-1))
                return (1, rocks, sand)

assert get_part_two(test) == 93
print(f'Part 2: {get_part_two(data)}')

