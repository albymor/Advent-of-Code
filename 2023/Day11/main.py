with open('input.txt', 'r') as f:
    data = f.read()

test = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""  


import numpy as np
from itertools import combinations

def get_part_one(data):
    lines = data.split('\n')

    lines = [list(line) for line in lines]
    lines = np.array(lines)

    expanded_map = []

    # expand vertically    
    for line in lines:
        if np.sum(line == '#') == 0:
            # only dots
            expanded_map.append(line)
            
        expanded_map.append(line)

    expanded_map = np.array(expanded_map)

    lines = expanded_map.copy()
    lines = lines.T

    expanded_map = []

    # expand vertically    
    for line in lines:
        if np.sum(line == '#') == 0:
            # only dots
            expanded_map.append(line)
            
        expanded_map.append(line)

    expanded_map = np.array(expanded_map).T

    galaxy_coordinates = []
    for i, line in enumerate(expanded_map):
        for j, char in enumerate(line):
            if char == '#':
                galaxy_coordinates.append((i, j))


    pairs = list(combinations(galaxy_coordinates, 2)) 

    total_dist = 0

    for pair in pairs:
        dist = np.abs(pair[0][0] - pair[1][0]) + np.abs(pair[0][1] - pair[1][1])
        total_dist += dist
            

    return total_dist

assert get_part_one(test) == 374
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data, factor):
    lines = data.split('\n')

    lines = [list(line) for line in lines]
    lines = np.array(lines)
    print(lines)

    expanded_map = []

    empty_x = []

    for i, line in enumerate(lines):
        if np.sum(line == '#') == 0:
            # only dots
            empty_x.append(i)
            
    empty_y = []

    for i, line in enumerate(lines.T):
        if np.sum(line == '#') == 0:
            # only dots
            empty_y.append(i)


    galaxy_coordinates = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                galaxy_coordinates.append((i, j))

    pairs = list(combinations(galaxy_coordinates, 2)) 

    total_dist = 0

    for pair in pairs:
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        dist = np.abs(x1 - x2) + np.abs(y1 - y2)
        total_dist += dist

        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])

        for i in empty_x:
            if x1 < i < x2:
                total_dist -= 1
                total_dist += factor

        for i in empty_y:
            if y1 < i < y2:
                total_dist -= 1
                total_dist += factor
            

    return total_dist

assert get_part_two(test, 2) == 374
assert get_part_two(test, 10) == 1030
assert get_part_two(test, 100) == 8410
print(f'Part 2: {get_part_two(data, 1000000)}')

