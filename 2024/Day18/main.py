with open('input.txt', 'r') as f:
    data = f.read()

test = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""


class Node:
    def __init__(self, pos: complex, distance: float = float('inf'), root: bool =False):
        self.pos = pos
        self.x = int(pos.real)
        self.y = int(pos.imag)
        self.distance = distance
        self.visited = False
        self.parent = None
        self.root = root

    def __repr__(self):
        return f'{self.x},{self.y} {self.distance}'
    
    def __lt__(self, other):
        return self.distance < other.distance
    

def get_neighbors(pos: complex, blocks: list[complex], dim:int):
    n = []
    np = pos+1
    if np not in blocks and 0<=int(np.real)<=dim and 0<=int(np.imag)<=dim:
        n.append(np)
    np = pos-1
    if np not in blocks and 0<=int(np.real)<=dim and 0<=int(np.imag)<=dim:
        n.append(np)
    np = pos+1j
    if np not in blocks and 0<=int(np.real)<=dim and 0<=int(np.imag)<=dim:
        n.append(np)
    np = pos-1j
    if np not in blocks and 0<=int(np.real)<=dim and 0<=int(np.imag)<=dim:
        n.append(np)

    return n



   
import heapq
def get_part_one(data, dimension, steps):
    lines = data.split('\n')
    blocks = [complex(*list(map(int,line.split(',')))) for line in lines]
    step = 1

    nodes = {}
    root  = Node(complex(0,0), 0)
    root.distance = 0
    root.root = True
    nodes[root.pos] = root

    hq = [root]
    heapq.heapify(hq)

    visited = set()

    while hq:
        current = heapq.heappop(hq)
        current.visited = True
        visited.add(current.pos)

        if current.pos ==  complex(6,0):
            pass

        if current.pos == complex(dimension, dimension):
            continue
        
        obstacles = blocks[:steps]
        neighbors = get_neighbors(current.pos, obstacles, dimension)

        for n in neighbors:
            if n not in visited:

                node = nodes.get(n, Node(n))
                if node.distance > current.distance+1:
                    node.distance = current.distance+1
                    node.parent = current

                nodes[n] = node
                if not node in hq:
                    heapq.heappush(hq, node)

    parents = []
    node = nodes[complex(dimension, dimension)] 
    while not node.root:
        node = node.parent
        parents.append(node.pos)

   

    return nodes[complex(dimension, dimension)].distance


assert get_part_one(test, 6, 12) == 22
print(f'Part 1: {get_part_one(data, 70, 1024)}')

from tqdm import tqdm 

# part 2 
def get_part_two(data, dimension, _steps):
    lines = data.split('\n')
    blocks = [complex(*list(map(int,line.split(',')))) for line in lines]

    for steps in tqdm(range(_steps, len(blocks))):
        nodes = {}
        root  = Node(complex(0,0), 0)
        root.distance = 0
        root.root = True
        nodes[root.pos] = root

        hq = [root]
        heapq.heapify(hq)

        visited = set()

        while hq:
            
            current = heapq.heappop(hq)
            current.visited = True
            visited.add(current.pos)

            if current.pos ==  complex(6,0):
                pass

            if current.pos == complex(dimension, dimension):
                continue
            
            obstacles = blocks[:steps]
            neighbors = get_neighbors(current.pos, obstacles, dimension)

            for n in neighbors:
                if n not in visited:

                    node = nodes.get(n, Node(n))
                    if node.distance > current.distance+1:
                        node.distance = current.distance+1
                        node.parent = current

                    nodes[n] = node
                    if not node in hq:
                        heapq.heappush(hq, node)

        if complex(dimension, dimension) in nodes:
            continue
        else:
            return blocks[steps-1]
            break 

        

   

    return nodes[complex(dimension, dimension)].distance

assert get_part_two(test, 6, 12) == complex(6,1)
print(f'Part 2: {get_part_two(data, 70, 1024)}')

