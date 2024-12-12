with open('input.txt', 'r') as f:
    data = f.read()

test = """.....
.S-7.
.|.|.
.L-J.
....."""

test2="""..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

class Pipe:
    def __init__(self, x, y, pipe_type):
        self.x = x
        self.y = y
        self.pipe_type = pipe_type
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.visited = False
        self.steps = 0
        
    def get_connections(self):
        connections = []
        if self.north != None:
            connections.append(self.north)
        if self.south != None:
            connections.append(self.south)
        if self.east != None:
            connections.append(self.east)
        if self.west != None:
            connections.append(self.west)
        return connections
    

    def __repr__(self):
        return f'Pipe({self.x}, {self.y}, {self.pipe_type}, {self.north.pipe_type if self.north != None else None}, {self.south.pipe_type if self.south != None else None}, {self.east.pipe_type if self.east != None else None}, {self.west.pipe_type if self.west != None else None})'
    


def get_part_one(data):
    lines = data.split('\n')

    # parse the pipes

    pipes = []

    for y, line in enumerate(lines):
        p =[]
        for x, pipe_type in enumerate(line):
            p.append(Pipe(x, y, pipe_type))
        pipes.append(p)


    start = None

    # link the pipes
    for y, line in enumerate(pipes):
        for x, pipe in enumerate(line):
            if pipe.pipe_type == '.':
                continue
            if pipe.pipe_type == 'S':
                start = pipe
                if y > 0 and pipes[y-1][x].pipe_type != '.':
                    pipe.north = pipes[y-1][x]
                if y < len(pipes)-1 and pipes[y+1][x].pipe_type != '.':
                    pipe.south = pipes[y+1][x]
                if x > 0 and pipes[y][x-1].pipe_type != '.':
                    pipe.west = pipes[y][x-1]
                if x < len(line)-1 and pipes[y][x+1].pipe_type != '.':
                    pipe.east = pipes[y][x+1]

            if pipe.pipe_type == '|':
                if y > 0 and pipes[y-1][x].pipe_type != '.':
                    pipe.north = pipes[y-1][x]
                if y < len(pipes)-1 and pipes[y+1][x].pipe_type != '.':
                    pipe.south = pipes[y+1][x]

            if pipe.pipe_type == '-':
                if x > 0 and pipes[y][x-1].pipe_type != '.':
                    pipe.west = pipes[y][x-1]
                if x < len(line)-1 and pipes[y][x+1].pipe_type != '.':
                    pipe.east = pipes[y][x+1]

            if pipe.pipe_type == 'L':
                if y > 0 and pipes[y-1][x].pipe_type != '.':
                    pipe.north = pipes[y-1][x]
                if x < len(line)-1 and pipes[y][x+1].pipe_type != '.':
                    pipe.east = pipes[y][x+1]

            if pipe.pipe_type == 'J':
                if y > 0 and pipes[y-1][x].pipe_type != '.':
                    pipe.north = pipes[y-1][x]
                if x > 0 and pipes[y][x-1].pipe_type != '.':
                    pipe.west = pipes[y][x-1]

            if pipe.pipe_type == 'F':
                if y < len(pipes)-1 and pipes[y+1][x].pipe_type != '.':
                    pipe.south = pipes[y+1][x]
                if x < len(line)-1 and pipes[y][x+1].pipe_type != '.':
                    pipe.east = pipes[y][x+1]

            if pipe.pipe_type == '7':
                if y < len(pipes)-1 and pipes[y+1][x].pipe_type != '.':
                    pipe.south = pipes[y+1][x]
                if x > 0 and pipes[y][x-1].pipe_type != '.':
                    pipe.west = pipes[y][x-1]


    from collections import deque

    # TODO
    #start.east = None
    #start.south = None

    admissible_east = ['-', '7', 'J']
    admissible_south = ['|', 'L', 'J']
    admissible_west = ['-', 'L', 'F']
    admissible_north = ['|', 'F', '7']

    start.east = start.east if  start.east != None and start.east.pipe_type in admissible_east else None
    start.south = start.south if start.south!= None and  start.south.pipe_type in admissible_south else None
    start.west = start.west if  start.west != None and start.west.pipe_type in admissible_west else None
    start.north = start.north if start.north!= None and  start.north.pipe_type in admissible_north else None

    print(start)



    q = deque()

    q.append(start)

    steps = 0

    while len(q) > 0:
        pipe = q.popleft()
        # if pipe.visited:
        #     break
        pipe.visited = True

        connections = pipe.get_connections()

        for p in pipe.get_connections():
            if not p.visited:
                p.steps = pipe.steps + 1
                q.append(p)

        steps = max(steps, pipe.steps)

    return steps

assert get_part_one(test) == 4
assert get_part_one(test2) == 8
assert get_part_one(data) == 7030
print(f'Part 1: {get_part_one(data)}')

import numpy as np

# part 2 
def get_part_two(data):
    lines = data.split('\n')

    # parse the pipes

    pipes = []

    for y, line in enumerate(lines):
        p =[]
        for x, pipe_type in enumerate(line):
            p.append(Pipe(x, y, pipe_type))
        pipes.append(p)


    start = None

    # link the pipes
    for y, line in enumerate(pipes):
        for x, pipe in enumerate(line):
            if pipe.pipe_type == '.':
                continue
            if pipe.pipe_type == 'S':
                start = pipe
                if y > 0 and pipes[y-1][x].pipe_type != '.':
                    pipe.north = pipes[y-1][x]
                if y < len(pipes)-1 and pipes[y+1][x].pipe_type != '.':
                    pipe.south = pipes[y+1][x]
                if x > 0 and pipes[y][x-1].pipe_type != '.':
                    pipe.west = pipes[y][x-1]
                if x < len(line)-1 and pipes[y][x+1].pipe_type != '.':
                    pipe.east = pipes[y][x+1]

            if pipe.pipe_type == '|':
                if y > 0 and pipes[y-1][x].pipe_type != '.':
                    pipe.north = pipes[y-1][x]
                if y < len(pipes)-1 and pipes[y+1][x].pipe_type != '.':
                    pipe.south = pipes[y+1][x]

            if pipe.pipe_type == '-':
                if x > 0 and pipes[y][x-1].pipe_type != '.':
                    pipe.west = pipes[y][x-1]
                if x < len(line)-1 and pipes[y][x+1].pipe_type != '.':
                    pipe.east = pipes[y][x+1]

            if pipe.pipe_type == 'L':
                if y > 0 and pipes[y-1][x].pipe_type != '.':
                    pipe.north = pipes[y-1][x]
                if x < len(line)-1 and pipes[y][x+1].pipe_type != '.':
                    pipe.east = pipes[y][x+1]

            if pipe.pipe_type == 'J':
                if y > 0 and pipes[y-1][x].pipe_type != '.':
                    pipe.north = pipes[y-1][x]
                if x > 0 and pipes[y][x-1].pipe_type != '.':
                    pipe.west = pipes[y][x-1]

            if pipe.pipe_type == 'F':
                if y < len(pipes)-1 and pipes[y+1][x].pipe_type != '.':
                    pipe.south = pipes[y+1][x]
                if x < len(line)-1 and pipes[y][x+1].pipe_type != '.':
                    pipe.east = pipes[y][x+1]

            if pipe.pipe_type == '7':
                if y < len(pipes)-1 and pipes[y+1][x].pipe_type != '.':
                    pipe.south = pipes[y+1][x]
                if x > 0 and pipes[y][x-1].pipe_type != '.':
                    pipe.west = pipes[y][x-1]


    from collections import deque

    admissible_east = ['-', '7', 'J']
    admissible_south = ['|', 'L', 'J']
    admissible_west = ['-', 'L', 'F']
    admissible_north = ['|', 'F', '7']

    start.east = start.east if  start.east != None and start.east.pipe_type in admissible_east else None
    start.south = start.south if start.south!= None and  start.south.pipe_type in admissible_south else None
    start.west = start.west if  start.west != None and start.west.pipe_type in admissible_west else None
    start.north = start.north if start.north!= None and  start.north.pipe_type in admissible_north else None

    q = deque()

    q.append(start)

    steps = 0

    while len(q) > 0:
        pipe = q.popleft()
        # if pipe.visited:
        #     break
        pipe.visited = True

        connections = pipe.get_connections()

        for p in pipe.get_connections():
            if not p.visited:
                p.steps = pipe.steps + 1
                q.append(p)

        steps = max(steps, pipe.steps)


    in_ = 0

    for y, line in enumerate(pipes):
        for x, pipe in enumerate(line):

            if pipe.visited:
                continue

            cross = 0
            x2,y2 = x,y

            while x2 < len(line) and y2 < len(pipes):
                p = pipes[y2][x2]
                if p.visited and p.pipe_type != 'L' and p.pipe_type != '7':
                    cross += 1
                x2 += 1
                y2 += 1


            if cross % 2 == 1:

                in_ += 1


    




    

    return in_


test3="""...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

test4="""..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""

test5=""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

test6="""FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""



assert get_part_two(test3) == 4
#assert get_part_two(test4) == 4
assert get_part_two(test5) == 8
#assert get_part_two(test6) == 10
print(f'Part 2: {get_part_two(data)}')

