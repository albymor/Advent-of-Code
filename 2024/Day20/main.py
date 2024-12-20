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
    x_max = len(mappa[0])-2
    y_max = len(mappa)-2
    n = []

    np = pos+1
    if 1<=int(np.real)<=x_max and 1<=int(np.imag)<=y_max:
        if mappa[int(np.imag)][int(np.real)] != '#':
            n.append(np)

    np = pos-1
    if 1<=int(np.real)<=x_max and 1<=int(np.imag)<=y_max:
        if mappa[int(np.imag)][int(np.real)] != '#':
            n.append(np)

    np = pos+1j
    if 1<=int(np.real)<=x_max and 1<=int(np.imag)<=y_max:
        if mappa[int(np.imag)][int(np.real)] != '#':
            n.append(np)

    np = pos-1j
    if 1<=int(np.real)<=x_max and 0<=int(np.imag)<=y_max:
            if mappa[int(np.imag)][int(np.real)] != '#':
                n.append(np)


    return n

def get_surrounding(pos: complex, mappa):
    x_max = len(mappa[0])-1
    y_max = len(mappa)-1
    n = {}

    np = pos+1
    if 0<=int(np.real)<=x_max and 0<=int(np.imag)<=y_max:
            n[np] = mappa[int(np.imag)][int(np.real)]

    np = pos-1
    if 0<=int(np.real)<=x_max and 0<=int(np.imag)<=y_max:
            n[np] = mappa[int(np.imag)][int(np.real)]

    np = pos+1j
    if 0<=int(np.real)<=x_max and 0<=int(np.imag)<=y_max:
            n[np] = mappa[int(np.imag)][int(np.real)]

    np = pos-1j
    if 0<=int(np.real)<=x_max and 0<=int(np.imag)<=y_max:
            n[np] = mappa[int(np.imag)][int(np.real)]


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
    

from collections import deque
def DFS(start, path, target_depth, mappa):
    if start ==  complex(7,7):
        pass
    explored = set()
    depth = 0
    q = deque()
    q.append((start, 0))
    saved = {}
    done = set()             


    while len(q)>0:
        c, depth = q.popleft()
        if depth > target_depth or c in explored:
            continue
        explored.add(c)
        s = get_surrounding(c, mappa)

        for k,v in s.items():
            if k == complex(5,7):
                pass
            if k in path and depth != 0:
                #dist_saved =  path[k].cost - path[start].cost - 2
                dist_saved =  path[k].cost - path[start].cost - depth-1
                if dist_saved > 0:
                    if (start, k) not in done:
                        if dist_saved in saved:
                            saved[dist_saved] += 1
                        else:
                            saved[dist_saved] = 1
                    done.add((start, k))

            if v == '#' and depth+1 <= target_depth and k not in explored:
                q.append((k, depth+1))
            

    return saved


    


def find_cheat2(path, mappa, th=0, depth=1):
    print(depth, th)
    path = path[::-1]
    nodes_dict = {}
    for p in path:
        nodes_dict[p.pos] = p

    saved = {}

    for k, v in nodes_dict.items():
        ss = DFS(k, nodes_dict, depth, mappa )
        for k, v in ss.items():
            if k >= th:
                if k in saved:
                    saved[k] += v
                else:
                    saved[k] = v

    res = 0
    for k , v in saved.items():
        if k >= th:
            res += v

    print(saved, res)

    return res


# def find_cheat(path, mappa, th=0):
#     path = path[::-1]
#     node_pos = [p.pos for p in path]
#     nodes_dict = {}
#     total_cost = len(path)
#     saved = {}
#     saved2 = {}
#     for p in path:
#         nodes_dict[p.pos] = p

#     dirs = [1,-1, 1j, -1j]

#     for p in path:
#         if p.pos == complex(7,7):
#             pass
#         for d in dirs:
#             np = p.pos+d
#             block = get_block(np, mappa)
#             if block == '#' and np+d in nodes_dict:
#                 s =  nodes_dict[np+d].cost - p.cost - 2
#                 if s > 0:
#                     #print_map(mappa, [p.pos, np, np+d])
#                     if s in saved:
#                         saved[s] += 1
#                     else:
#                         saved[s] = 1

#         ss = DFS(p.pos, nodes_dict, 1, mappa )
#         for k, v in ss.items():
#             if k in saved2:
#                 saved2[k] += v
#             else:
#                 saved2[k] = v

#         pass

#     res = 0
#     for k , v in saved.items():
#         if k >= th:
#             res += v

#     return res


                


def get_part_one(data, th=0, depth=1):
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



    return find_cheat2(parents, mappa, th, depth)


    print(start,end)
    

    return 0

assert get_part_one(test) == 44
print(f'Part 1: {get_part_one(data, th=100, depth=1)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    return 1

assert get_part_one(test, depth=19, th=50) == 285
print(f'Part 2: {get_part_one(data, th=100, depth=20)}')

