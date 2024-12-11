from collections import deque

with open('input.txt', 'r') as f:
    data = f.read()

test = """0123
1234
8765
9876"""

test2 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

def next_pos(current_pos, x_max, y_max):
    dirs = [1, -1, 1j, -1j]

    pos = []

    for d in dirs:
        np = current_pos+d
        if 0<=np.real<=x_max and 0<=np.imag<=y_max:
            pos.append(np)

    return pos

     
class Bag:
    def __init__(self):
        self.goals = set()
        self.fork = 0    

    def append(self, el):
        self.goals.add(el)

def solve(data):
    lines = data.split('\n')
    topo = [list(map(int , list(x))) for x in lines]
    res = 0

    x_max = len(topo[0])-1
    y_max = len(topo)-1

    #  find start
    to_visit = deque()
    start_points = []
    for i, row in enumerate(topo):
        for j, val in enumerate(row):
            if val == 0:
                b = Bag()
                to_visit.append((complex(j, i), b))
                start_points.append((complex(j, i), b))
                

    while len(to_visit) > 0:
        n = to_visit.popleft()
        p=n[0]

        if topo[int(p.imag)][int(p.real)] == 9:
            n[1].append(p)
            # this path lead to a goal so increment the number of valid forks
            n[1].fork += 1
            continue

        next_positions = next_pos(p, x_max, y_max)
        for np in next_positions:
            q = topo[int(np.imag)][int(np.real)]-topo[int(p.imag)][int(p.real)]
            if q == 1:
                to_visit.append((np, n[1]))

    goals = 0
    unique_paths = 0


    for p in start_points:
        goals += len(p[1].goals)
        unique_paths += p[1].fork
    return (goals, unique_paths)


def get_part_one(data):
    res, _ = solve(data)
    return res


assert get_part_one(test) == 1
assert get_part_one(test2) == 36
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    _, res = solve(data)
    return res

assert get_part_two(test2) == 81
print(f'Part 2: {get_part_two(data)}')

