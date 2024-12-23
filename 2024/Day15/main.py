with open('input.txt', 'r') as f:
    data = f.read()

test = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

def get_block(pos, mappa):
    x , y = int(pos.real), int(pos.imag)
    return  mappa[y][x]

def set_block(pos, mappa, c):
    x , y = int(pos.real), int(pos.imag)
    mappa[y][x] = c




def attempt_move(pos, direction,  mappa):
    robot_pos = pos
    movable = False
    steps = 0
    while True:
        pos += direction
        block =  get_block(pos, mappa)
        if block == 'O':
            steps += 1
            pass
        elif block == '#':
            break
        elif block == '.':
            movable = True
            break

    movedir = -direction
    if movable:
        while steps > 0:
            set_block(pos, mappa, get_block(pos+movedir, mappa))
            steps -=1

        set_block(robot_pos+direction, mappa, '.')

    return movable


def print_map(mappa):
    for l in mappa:
        print(''.join(l))




class Robot:
    def __init__(self, start):
        self.start = start
        self.current_position = start

    def navigate(self, direction, mappa):
        next_step = self.current_position + direction
        block =  get_block(next_step, mappa)
        if block == '.':
            self.current_position = next_step
        elif block == '#':
            pass
        elif block == 'O':
            if attempt_move(self.current_position, direction, mappa):
                self.current_position = next_step   
        else:
            raise ValueError("Unknown block in map")

def get_part_one(data):
    mappa, moves_raw = data.split('\n\n')

    moves_raw = moves_raw.replace('\n', '')

    mappa = list(map(list, mappa.split('\n')))
    moves = []
    for m in moves_raw:
        if m == '<':
            moves.append(-1)
        elif m == '>':
            moves.append(1)
        elif m == '^':
            moves.append(-1j)
        elif m == 'v':
            moves.append(1j)
        else:
            raise ValueError("Unknown direction")
        
    # find start position
    for y, l in enumerate(mappa):
        for x, c in enumerate(l):
            if c == '@':
                start = complex(x, y)
                set_block(start, mappa, '.')
                break

    robot = Robot(start)

    for d in moves:
        robot.navigate(d, mappa)
        #print(robot.current_position)
        #print_map(mappa)
        pass

    res = 0

    for y, l in enumerate(mappa):
        for x , c in enumerate(l):
            if c == 'O':
                r = ((y*100)+x)
                #print(r)
                res += r

    print(res)
        

    return res

assert get_part_one(test) == 2028
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    mappa, moves_raw = data.split('\n\n')

    moves_raw = moves_raw.replace('\n', '')

    mappa = list(map(list, mappa.split('\n')))
    moves = []
    for m in moves_raw:
        if m == '<':
            moves.append(-1)
        elif m == '>':
            moves.append(1)
        elif m == '^':
            moves.append(-1j)
        elif m == 'v':
            moves.append(1j)
        else:
            raise ValueError("Unknown direction")
        
    new_map = []
    for y, l in enumerate(mappa):
        for x, c in enumerate(l):
        
    # find start position
    for y, l in enumerate(mappa):
        for x, c in enumerate(l):
            if c == '@':
                start = complex(x, y)
                set_block(start, mappa, '.')
                break

    return 1

assert get_part_two(test) == 1
print(f'Part 2: {get_part_two(data)}')

