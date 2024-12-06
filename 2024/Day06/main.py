with open('input.txt', 'r') as f:
    data = f.read()

test = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""   

def find_start(mappa):
    for i, l in enumerate(mappa):
        try:
            j = l.index('^')
            return (j,i)
            
        except: 
            pass
    else:
        assert False

def get_part_one(data):
    mappa = list(map(list, data.split('\n')))

    x_max = len(mappa[0])-1
    y_max = len(mappa)-1

    start = find_start(mappa)

    start = complex(start[0], start[1])

    direction = -1j

    visited = set()

    pos = start

    while True:
        visited.add(pos)

        next_pos = pos + direction
        if next_pos.real<0 or next_pos.real>x_max or next_pos.imag<0 or next_pos.imag > y_max:
            print("dead")
            return len(visited)
        
        if mappa[int(next_pos.imag)][int(next_pos.real)] == "#":
            direction *= 1j

        else:
            pos = next_pos

assert get_part_one(test) == 41
print(f'Part 1: {get_part_one(data)}')


def two(mappa):
    x_max = len(mappa[0])-1
    y_max = len(mappa)-1

    start = find_start(mappa)

    start = complex(start[0], start[1])
    direction = -1j

    visited = set()

    pos = start

    while True:
        if (pos.real, pos.imag, direction) in visited:
            #loop
            return True
        visited.add((pos.real, pos.imag, direction))

        next_pos = pos + direction
        if next_pos.real<0 or next_pos.real>x_max or next_pos.imag<0 or next_pos.imag > y_max:
            return False
        
        if mappa[int(next_pos.imag)][int(next_pos.real)] == "#":
            direction *= 1j

        else:
            pos = next_pos

import copy
from tqdm import tqdm

# part 2 
def get_part_two(data):
    mappa = list(map(list, data.split('\n')))

    comb = 0

# Brute Force Solution ======== 1min 43sec

#    for y in tqdm(range(len(mappa))):
#        for x in range(len(mappa[0])):
#            if mappa[y][x] == '.':
#                m = copy.deepcopy(mappa)
#                m[y][x] = '#'
#                comb += two(m)
#                
#    return comb

# ========================================

# Surrounding check solution  ======== 1min 04sec, 10423 positions to check

    # x_max = len(mappa[0])-1
    # y_max = len(mappa)-1

    # start = find_start(mappa)

    # start = complex(start[0], start[1])

    # direction = -1j

    # visited = set()

    # pos = start

    # while True:
    #     visited.add(pos)

    #     next_pos = pos + direction
    #     if next_pos.real<0 or next_pos.real>x_max or next_pos.imag<0 or next_pos.imag > y_max:
    #         #print("dead")
    #         break
        
    #     if mappa[int(next_pos.imag)][int(next_pos.real)] == "#":
    #         direction *= 1j

    #     else:
    #         pos = next_pos

    # # remove the start from visited as we cannot hava an obstacle in the starting position
    # visited.remove(start)

    # # now the ideas is to try to place obstacles only on the surrounding of the previous path avoiding to check point that 
    # # are never visited

    # obstacles = set()
    # for el in visited:
    #     obstacles.add(el+1)
    #     obstacles.add(el-1)
    #     obstacles.add(el+1j)
    #     obstacles.add(el-1j)

    # # remove the start from visited as we cannot hava an obstacle in the starting position
    # obstacles.remove(start)

    # # remove el that are outside the map

    # obstacles = set(filter(lambda x: 0<=x.real<=x_max and 0<=x.imag<=y_max, obstacles))

    # for o in tqdm(obstacles):
    #     if mappa[int(o.imag)][int(o.real)] == '.':
    #         m = copy.deepcopy(mappa)
    #         m[int(o.imag)][int(o.real)] = '#'
    #         comb += two(m)

    
    # ========================================

# Ahead obstacle solution  ======== 28sec, 5040 positions to check
# the idea is to check if we enter a loop by placing an obstacle in each of the ahead position in the original path

    x_max = len(mappa[0])-1
    y_max = len(mappa)-1

    start = find_start(mappa)

    start = complex(start[0], start[1])

    direction = -1j

    visited = set()
    vis_dir = set() # as in part one, but this time save also position and direction

    pos = start

    while True:
        visited.add(pos)
        vis_dir.add((pos, direction))

        next_pos = pos + direction
        if next_pos.real<0 or next_pos.real>x_max or next_pos.imag<0 or next_pos.imag > y_max:
            #print("dead")
            break
        
        if mappa[int(next_pos.imag)][int(next_pos.real)] == "#":
            direction *= 1j

        else:
            pos = next_pos

    # remove the start from visited as we cannot hava an obstacle in the starting position
    visited.remove(start)

    # now the ideas is to try to place obstacles only on the surrounding of the previous path avoiding to check point that 
    # are never visited

    obstacles = set()
    for el, d in vis_dir:
        obstacles.add(el+d)

    # remove the start from visited as we cannot hava an obstacle in the starting position
    #obstacles.remove(start)

    # remove el that are outside the map

    obstacles = set(filter(lambda x: 0<=x.real<=x_max and 0<=x.imag<=y_max, obstacles))

    for o in tqdm(obstacles):
        if mappa[int(o.imag)][int(o.real)] == '.':
            m = copy.deepcopy(mappa)
            m[int(o.imag)][int(o.real)] = '#'
            comb += two(m)

    return comb

assert get_part_two(test) == 6
print(f'Part 2: {get_part_two(data)}')

