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


from collections import deque
from copy import deepcopy
def attempt_move(pos, direction,  mappa):
    robot_pos = pos
    if direction == 1 or direction == -1:
        movable = False
        steps = 0
        while True:
            pos += direction
            block =  get_block(pos, mappa)
            if block == 'O' or  block == '[' or block == ']':
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
    else:
        checked = []
        movable = []
        tbc = deque()
        tbc.append(pos+direction)
        while len(tbc) > 0:
            curr = tbc.popleft()
            checked.append(curr)
            if get_block(curr+direction) == '#':
                return False
            if get_block(tbc+direction) == '.':
                movable.append(True)
            if get_block(curr+direction) == '[' or get_block(curr+direction) == ']':
                tbc.append(curr+direction)

            # add neighbour to chack 
            if get_block(curr) == '[':
                tbc.append(curr+1)
            else:
                tbc.append(curr-1)

        if all(movable):
            mc = deepcopy(mappa)

            for p in checked:
                ns = get_block(p, mc)
                set_block(p+direction, mappa, ns)
                set_block(p, mappa, '.')  


        
        return all(movable)


        


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
        elif block == '[' or block == ']' or block == 'O':
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

#assert get_part_one(test) == 2028
#print(f'Part 1: {get_part_one(data)}')



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
        line = []
        for x, c in enumerate(l):
            if c == '.':
               line.append('.')
               line.append('.')
            elif c == '#':
                line.append('#')
                line.append('#')
            elif c == 'O':
                line.append('[')
                line.append(']')
            elif c == '@':
                line.append('@')
                line.append('.')
            else:
                raise ValueError("Unknown symbol")
            
        new_map.append(line)

    mappa = new_map

    start = None 

        
    # find start position
    for y, l in enumerate(mappa):
        for x, c in enumerate(l):
            if c == '@':
                start = complex(x, y)
                set_block(start, mappa, '.')
                break


    robot = Robot(start)
    print_map(mappa)

    for d in moves:
        robot.navigate(d, mappa)
        print(robot.current_position)
        print_map(mappa)
        pass

    res = 0

    for y, l in enumerate(mappa):
        for x , c in enumerate(l):
            if c == '[':
                r = ((y*100)+x)
                #print(r)
                res += r

    print(res)

    print_map(mappa)

    return res


test2 ="""#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

assert get_part_two(test2) == 9021
print(f'Part 2: {get_part_two(data)}')

