from aoc.utils import timeit
with open('input.txt', 'r') as f:
    data = f.read()

test = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""" 


test2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

test3 ="""#######E#######
#...#...#######
#.#...#.......#
#.###########.#
#S............#
###############"""

from collections import deque
from copy import deepcopy, copy

def get_block(mm, pos):
    x, y = int(pos.real), int(pos.imag)
    return mm[y][x]

def set_block(mm, pos, c):
    x, y = int(pos.real), int(pos.imag)
    mm[y][x] = c


class Path:
    def __init__(self):
        self.position = None
        self.direction = 1
        self.score = 0
        self.visited = []
        self.tile = 0


    def copy(self, p):
        self.position = p.position
        self.direction = p.direction
        self.score = p.score
        self.visited = copy(p.visited)
        self.tile = p.tile


    def __repr__(self):
        return f"{self.position}, {self.direction}, {self.score}, {self.tile}"


@timeit
def get_part_one(data):
    lines = data.split('\n')
    mappa = list(map(list, lines))

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "S":
                start = complex(x, y)
                break


    goals = []

    visited = {}

    vis = deepcopy(mappa)

    q = deque()
    s = Path()
    s.position = start
    q.append(s)

    while len(q)> 0:
        print(len(q), end="\r")
        p = q.popleft()

        p.visited.append(p.position)
        p.tile += 1
        visited[(p.position, p.direction)] = p.score

        if p.position == complex(5, 4):
            pass
        
        #straight
        if get_block(mappa, p.position+p.direction) == '.':
            np = Path()
            np.copy(p)
            np.score +=1
            np.position = np.position+np.direction
            if (np.position, np.direction) not in visited:
                q.append(np)
        elif get_block(mappa, p.position+p.direction) == 'E':
            g = Path()
            g.copy(p)
            goals.append(g)

        #-90
        if get_block(mappa, p.position+(p.direction*-1j)) == '.':
            np = Path()
            np.copy(p)
            np.score += 1001
            np.position = np.position+(np.direction*-1j)
            np.direction *= -1j
            if (np.position, np.direction) not in visited:
                q.append(np)
        elif get_block(mappa, p.position+p.direction) == 'E':
            g = Path()
            g.copy(p)
            goals.append(g)

        #+90
        if get_block(mappa, p.position+(p.direction*1j)) == '.':
            np = Path()
            np.copy(p)
            np.score += 1001
            np.position = np.position+(np.direction*1j)
            np.direction *= 1j
            if (np.position, np.direction) not in visited:
                q.append(np)            
        elif get_block(mappa, p.position+p.direction) == 'E':
            g = Path()
            g.copy(p)
            goals.append(g)
        
        if len(q)> 0:
            q = deque(sorted(q, key=lambda x: x.score))
        else:
            break

    m = min(goals, key=lambda x: x.score)

    vis = deepcopy(mappa)
    for p in m.visited:
        set_block(vis, p, '█')


    for l in vis:
        print(''.join(l))

    bests = []
    b_score = m.score
    for g in goals:
        if g.score == b_score:
            bests += g.visited

    print('Part 2:', len(set(bests))+1)

    return m.score+1

assert get_part_one(test) == 7036
assert get_part_one(test2) == 11048
assert get_part_one(test3) == 3022

test4 = """#########
#####E..#
#####.#.#
#.......#
#.###.###
#.###.###
#S....###
#########"""

test5 = """#########
#####...#
#####.#.#
#......E#
#.###.###
#.###.###
#S....###
#########"""

test6 ="""##############
#...########E#
#.#.##.......#
#.#.##.#####.#
#.#..........#
#.####.#######
#.####.......#
#.##########.#
#S...........#
##############"""

assert get_part_one(test4) == 1009
assert get_part_one(test5) == 2009
assert get_part_one(test6) == 5024

print(f'Part 1: {get_part_one(data)}')


