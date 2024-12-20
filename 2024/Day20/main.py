with open('input.txt', 'r') as f:
    data = f.read()

test = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""  

from heapq import *
from collections import defaultdict 

def get_neighbors(pos: complex, mappa):
    x_max = len(mappa[0])-1
    y_max = len(mappa)-1
    n = []

    np = pos+1
    if 0<=int(np.real)<=x_max and 0<=int(np.imag)<=y_max:
        if mappa[int(np.imag)][int(np.real)] != '#':
            n.append(np)

    np = pos-1
    if 0<=int(np.real)<=x_max and 0<=int(np.imag)<=y_max:
        if mappa[int(np.imag)][int(np.real)] != '#':
            n.append(np)

    np = pos+1j
    if 0<=int(np.real)<=x_max and 0<=int(np.imag)<=y_max:
        if mappa[int(np.imag)][int(np.real)] != '#':
            n.append(np)

    np = pos-1j
    if 0<=int(np.real)<=x_max and 0<=int(np.imag)<=y_max:
            if mappa[int(np.imag)][int(np.real)] != '#':
                n.append(np)


    return n


def get_block(pos, mappa):
    x, y = int(pos.real), int(pos.imag)
    x_max = len(mappa[0])-1
    y_max = len(mappa)-1
    if 0<=x<=x_max and 0<=y<=y_max:
        return mappa[y][x]
    else:
        return None

from copy import deepcopy
def print_map(mappa, poss):
    m = deepcopy(mappa)
    for p in poss:
        x, y = int(p.real), int(p.imag)
        m[y][x] = '*'
    
    for line in m:
        print(''.join(line))




class Node:
    def __init__(self, pos=None, cost=float('inf'), parent=None):
        self.pos = pos
        self.cost = cost
        self.parent = parent


    def __repr__(self):
        return f"{self.pos}"

    def __lt__(self, other):
        return self.cost < other.cost


def find_cheat(path, mappa, th=0):
    path = path[::-1]
    node_pos = [p.pos for p in path]
    nodes_dict = {}
    total_cost = len(path)
    saved = {}
    for p in path:
        nodes_dict[p.pos] = p

    dirs = [1,-1, 1j, -1j]

    for p in path:
        for d in dirs:
            np = p.pos+d
            block = get_block(np, mappa)
            if block == '#' and np+d in nodes_dict:
                s =  nodes_dict[np+d].cost - p.cost - 2
                if s > 0:
                    #print_map(mappa, [p.pos, np, np+d])
                    if s in saved:
                        saved[s] += 1
                    else:
                        saved[s] = 1

    res = 0
    for k , v in saved.items():
        if k >= th:
            res += v

    return res


                


def get_part_one(data, th=0):
    mappa = list(map(list,data.split('\n')))


    start, end = None, None

    for y, l in enumerate(mappa):
        for x, c in enumerate(l):
            if c == 'S':
                start = complex(x, y)
            if c == 'E':
                end = complex(x, y) 

    nodes = defaultdict(lambda: Node())
    start_node = Node(start, cost=0)
    nodes[start] = start_node
    visited = set()
    hq =[start_node]
    heapify(hq)

    while len(hq):
        cn = heappop(hq)
        cc, cp = cn.cost, cn.pos
        visited.add(cp)

        if cp == end:
            continue


        cost = cc+1        

        for n in get_neighbors(cp, mappa):
            if nodes[n].cost > cost:
                nodes[n].pos = n
                nodes[n].cost = cost
                nodes[n].parent = cn
            if n not in visited:
                heappush(hq, nodes[n])

        


    parents = [nodes[end]]

    cn = nodes[end]
    while cn.parent != None:
        parents.append(cn.parent)
        cn = cn.parent


    return find_cheat(parents, mappa, th)


    print(start,end)
    

    return 0

assert get_part_one(test) == 44
print(f'Part 1: {get_part_one(data, th=100)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    return 1

assert get_part_two(test) == 1
print(f'Part 2: {get_part_two(data)}')

