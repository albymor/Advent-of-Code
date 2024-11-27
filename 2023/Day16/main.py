with open('input.txt', 'r') as f:
    data = f.read()

test = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|...."""   

class Beam():
    def __init__(self, position, direction) -> None:
        self.position = position
        self.direction = direction
        self.cache = [(position, direction)]
        self.previous_position = None
        self.born_point = self.born()

    def navigate(self):
        self.position += self.direction
        if self.previous_position != None:
            self.cache.append(self.previous_position)
        self.previous_position = (self.position, self.direction)

    def get_coordinates(self):
        return int(self.position.real), int(self.position.imag)
    
    def looping(self):
        return (self.position, self.direction) in self.cache
    
    def born(self):
        self.born_point = (self.position, self.direction)

    
    def __repr__(self) -> str:
        return f"x={int(self.position.real)} y={int(self.position.imag)} dir={self.direction}"
    
def visualize(mappa):
    print('\n'.join(list(map(lambda x: ''.join(x), mappa))))

def score(mappa):
    return sum(row.count('#') for row in mappa)



from collections import deque
import copy

    

def get_part_one(data):

    deads = []

    beams = deque([Beam(0+0j, 1)])   

    lines = data.split('\n')
    mappa = list(map(list, lines))
    energized = copy.deepcopy(mappa)

    while len(beams) > 0:

        b = beams.popleft()
        x, y = b.get_coordinates()
        if 0 <= x < len(mappa[0]) and 0 <= y < len(mappa):
            energized[y][x] = '#'
        else:
            # dead beam
            deads.append(b.born_point)
            continue

        step = mappa[y][x]

        if step == '\\':
            pass
        
        if step == '.':
            pass
        elif b.direction == 1:
            if step == '-':
                pass
            elif step == '/':
                b.direction = -1j
            elif step == '\\':
                b.direction = 1j
            elif step == '|':
                b.direction = 1j
                bn = copy.deepcopy(b)
                bn.direction = -1j
                bn.born()
                if bn.born_point not in deads:
                    beams.append(bn)
            else:
                assert False
        elif b.direction == -1:
            if step == '-':
                pass
            elif step == '/':
                b.direction = 1j
            elif step == '\\':
                b.direction = -1j
            elif step == '|':
                b.direction = 1j
                bn = copy.deepcopy(b)
                bn.direction = -1j
                bn.born()
                if bn.born_point not in deads:
                    beams.append(bn)
            else:
                assert False

        elif b.direction == -1j:
            if step == '-':
                b.direction = 1
                bn = copy.deepcopy(b)
                bn.direction = -1
                bn.born()
                if bn.born_point not in deads:
                    beams.append(bn)
            elif step == '/':
                b.direction = 1
            elif step == '\\':
                b.direction = -1
            elif step == '|':
                pass
            else:
                assert False

        elif b.direction == 1j:
            if step == '-':
                b.direction = 1
                bn = copy.deepcopy(b)
                bn.direction = -1
                bn.born()
                if bn.born_point not in deads:
                    beams.append(bn)
            elif step == '/':
                b.direction = -1
            elif step == '\\':
                b.direction = 1
            elif step == '|':
                pass
            else:
                assert False

        b.navigate()

        if not b.looping() and (b.born_point not in deads):
            beams.append(b)
        else:
            deads.append(b.born_point)

    return score(energized)

assert get_part_one(test) == 46
print(f'Part 1: {get_part_one(data)}')

from tqdm import tqdm

# part 2 
def get_part_two(data):
    lines = data.split('\n')
    mappa = list(map(list, lines))

    

    max_y = len(mappa)-1
    max_x = len(mappa[0])-1

    startpoint = [
        Beam(0+0j, 1), # up left
        Beam(0+0j, 1j), # up left
        Beam(max_x+0j, -1), # up right
        Beam(max_x+0j, 1j), # up right
        Beam(complex(0, max_y), 1), # low left
        Beam(complex(0, max_y), -1j), # low left
        Beam(complex(max_x, max_y), -1), # low right
        Beam(complex(max_x, max_y), -1j), # low right
    ]

    up = [Beam(x+0j, 1j) for x in range(1, max_x)]
    low = [Beam(complex(x, max_y), -1j) for x in range(1, max_x)]
    left = [Beam(complex(0, x), 1) for x in range(1, max_y)]
    right = [Beam(complex(max_x, x), 1) for x in range(1, max_y)]

    startpoint = startpoint + up +low+right+ left

    scores = []


    for lol in tqdm(startpoint):
        beams = deque([lol])  

        deads = [] 


        energized = copy.deepcopy(mappa)

        while len(beams) > 0:

            b = beams.popleft()
            x, y = b.get_coordinates()
            if 0 <= x < len(mappa[0]) and 0 <= y < len(mappa):
                energized[y][x] = '#'
            else:
                # dead beam
                deads.append(b.born_point)
                continue


            step = mappa[y][x]

            if step == '\\':
                pass
            
            if step == '.':
                pass
            elif b.direction == 1:
                if step == '-':
                    pass
                elif step == '/':
                    b.direction = -1j
                elif step == '\\':
                    b.direction = 1j
                elif step == '|':
                    b.direction = 1j
                    bn = copy.deepcopy(b)
                    bn.direction = -1j
                    bn.born()
                    if bn.born_point not in deads:
                        beams.append(bn)
                else:
                    assert False
            elif b.direction == -1:
                if step == '-':
                    pass
                elif step == '/':
                    b.direction = 1j
                elif step == '\\':
                    b.direction = -1j
                elif step == '|':
                    b.direction = 1j
                    bn = copy.deepcopy(b)
                    bn.direction = -1j
                    bn.born()
                    if bn.born_point not in deads:
                        beams.append(bn)
                else:
                    assert False

            elif b.direction == -1j:
                if step == '-':
                    b.direction = 1
                    bn = copy.deepcopy(b)
                    bn.direction = -1
                    bn.born()
                    if bn.born_point not in deads:
                        beams.append(bn)
                elif step == '/':
                    b.direction = 1
                elif step == '\\':
                    b.direction = -1
                elif step == '|':
                    pass
                else:
                    assert False

            elif b.direction == 1j:
                if step == '-':
                    b.direction = 1
                    bn = copy.deepcopy(b)
                    bn.direction = -1
                    bn.born()
                    if bn.born_point not in deads:
                        beams.append(bn)
                elif step == '/':
                    b.direction = -1
                elif step == '\\':
                    b.direction = 1
                elif step == '|':
                    pass
                else:
                    assert False

            b.navigate()

            if not b.looping() and (b.born_point not in deads):
                beams.append(b)
            else:
                deads.append(b.born_point)

        scores.append(score(energized))

    return max(scores)

assert get_part_two(test) == 51
print(f'Part 2: {get_part_two(data)}')

