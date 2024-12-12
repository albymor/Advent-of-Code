with open('input.txt', 'r') as f:
    data = f.read()

test = """AAAA
BBCD
BBCC
EEEC"""   


def get_val(mappa, pos):
    x, y = int(pos.real), int(pos.imag)
    x_max = len(mappa[0])-1
    y_max = len(mappa)-1
    if 0 <= x <= x_max and 0 <= y <= y_max:
        return mappa[y][x]
    else:
        return None

class Cluster():
    def __init__(self):
        self.tiles = []
        self.area = 0
        self.perimeter = 0
        self.edges = 0

    def __repr__(self):
        return f"{self.tiles}, A={self.area}, P={self.perimeter}, E={self.edges}"


def find(mm, pos):
    dirs = [1,-1,1j,-1j]
    explored = []
    cluster = Cluster()
    x, y = pos
    pos = complex(pos[0], pos[1]) 
    c = mm[y][x]
    q = set()
    q.add(pos)
    while len(q)> 0:
        now = q.pop()
        explored.append(now)
        cluster.tiles.append(now)
        cluster.area +=1
        cluster.perimeter += 4
        for d in dirs:
            if get_val(mm, now+d) == c:
                cluster.perimeter -= 1
                if now+d not in explored: 
                    q.add(now+d)

        if c == 'C':
            pass
        
        # edge detection
        c1 = get_val(mm, now-1j)
        c2 = get_val(mm, now+1)
        c3 = get_val(mm, now+1-1j)

        # outer corner
        if  c1!= c and c != c2:
            cluster.edges +=1
        # inner corner
        if  c1== c and c == c2 and c3 != c:
            cluster.edges +=1
        
        c1 = get_val(mm, now+1)
        c2 = get_val(mm, now+1j)
        c3 = get_val(mm, now+1+1j)
        if  c1!= c and c != c2:
            cluster.edges +=1
        if  c1== c and c == c2 and c3 != c:
            cluster.edges +=1

        c1 = get_val(mm, now+1j)
        c2 = get_val(mm, now-1)
        c3 = get_val(mm, now-1+1j)
        if  c1!= c and c != c2:
            cluster.edges +=1
        if  c1== c and c == c2 and c3 != c:
            cluster.edges +=1

        c1 = get_val(mm, now-1)
        c2 = get_val(mm, now-1j)
        c3 = get_val(mm, now-1-1j)
        if  c1!= c and c != c2:
            cluster.edges +=1
        if  c1== c and c == c2 and c3 != c:
            cluster.edges +=1

    return cluster



def find_clusters(data):
    lines = data.split('\n')
    lines = [list(line) for line in lines]

    expl = []
    _clusters = {}

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if complex(x,y) in expl:
                continue
            cluster = find(lines, (x,y))
            if not char in _clusters:
                _clusters[char] = []
                
            _clusters[char].append(cluster)
            expl += cluster.tiles

    return _clusters

def get_part_one(data):

    clusters = find_clusters(data)
    

    res = 0

    for k, v in clusters.items():
        for c in v:
            res += (c.area*c.perimeter)

    return res

assert get_part_one(test) == 140
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    clusters = find_clusters(data)
    
    edges = 0
    for k, v in clusters.items():
        for c in v:
            edges += (c.area*c.edges)

    return edges


test2="""EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
assert get_part_two(test) == 80
assert get_part_two(test2) == 236
print(f'Part 2: {get_part_two(data)}')

