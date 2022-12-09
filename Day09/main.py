import numpy as np
with open('input.txt', 'r') as f:
    data = f.read()

test = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


initial_grid = """......
......
......
......
H....."""


class Node:
    def __init__(self, x, y, max_x, max_y):
        self.x = x
        self.y = y
        self.max_x = max_x - 1
        self.max_y = max_y - 1
        self.has_moved = False
        self.x_old = x
        self.y_old = y

    def __repr__(self):
        return f'x={self.x}, y={self.y}, moved={self.has_moved}'

    def move(self, direction):
        self.x_old = self.x
        self.y_old = self.y
        self.has_moved = True
        if direction == 'R':
            self.x += 1
        elif direction == 'L':
            self.x -= 1
        elif direction == 'U':
            self.y -= 1
        elif direction == 'D':
            self.y += 1
        else:
            raise "Invalid move"

    def move_by_coordinates(self, x, y):
        self.has_moved = True
        self.x_old = self.x
        self.y_old = self.y
        self.x = x
        self.y = y

    def increment(self):
        self.has_moved = True
        self.x += 1
        self.y += 1
        self.x_old += 1
        self.y_old += 1


def get_initial_grid(aa):
    gg = []
    line = aa.split('\n')
    for l in line:
        gg.append([0 if x == '.' else 1 for x in l])

    return np.array(gg)


def get_distance(a, b):
    x = abs(a.x-b.x)
    y = abs(a.y-b.y)

    return x, y


def get_part_one(data):

    grid = get_initial_grid(initial_grid)

    initial_position = np.unravel_index(grid.argmax(), grid.shape)
    head = Node(*initial_position[::-1], *list(grid.shape)[::-1])
    tail = Node(*initial_position[::-1], *list(grid.shape)[::-1])

    data = data.split('\n')

    for el in data:
        ins = el.split(' ')
        direction = ins[0]
        steps = int(ins[1])
        for s in range(steps):
            head.move(direction)
            dis_x, dis_y = get_distance(head, tail)
            distance = max(dis_x, dis_y)
            if distance > 1:
                if dis_y > 1 and dis_x > 0:
                    # diagonal move
                    if head.y < tail.y:
                        new_y = tail.y-1
                    else:
                        new_y = tail.y+1
                    tail.move_by_coordinates(head.x, new_y)

                elif dis_x > 1 and dis_y > 0:
                    # diagonal move
                    if head.x < tail.x:
                        new_x = tail.x-1
                    else:
                        new_x = tail.x+1
                    tail.move_by_coordinates(new_x, head.y)

                else:
                    tail.move(direction)

            max_y, max_x = np.array(grid.shape)-1
            if (tail.y > max_y) or (tail.x > max_x):
                grid = np.vstack([grid, np.zeros((1, grid.shape[1]))])
                grid = np.hstack([grid, np.zeros((grid.shape[0], 1))])

            if (tail.y < 0) or (tail.x < 0):
                grid = np.vstack([np.zeros((1, grid.shape[1])), grid])
                grid = np.hstack([np.zeros((grid.shape[0], 1)), grid])
                head.increment()
                tail.increment()

            grid[tail.y, tail.x] = 1

    return (int(np.sum(grid)))


assert get_part_one(test) == 13
print(f'Part 1: {get_part_one(data)}')

# part 2

def get_part_two(data):

    grid = get_initial_grid(initial_grid2)

    initial_position = np.unravel_index(grid.argmax(), grid.shape)
    head = Node(*initial_position[::-1], *list(grid.shape)[::-1])
    nodes = [Node(*initial_position[::-1], *list(grid.shape)[::-1])
             for _ in range(9)]

    data = data.split('\n')

    for el in data:
        ins = el.split(' ')
        direction = ins[0]
        steps = int(ins[1])
        for s in range(steps):
            head.move(direction)
            current_head = head
            for idx, tail in enumerate(nodes):
                dis_x, dis_y = get_distance(current_head, tail)
                distance = max(dis_x, dis_y)
                if distance > 1:
                    if dis_x > 1 and dis_y > 1:

                        if current_head.y < tail.y:
                            new_y = tail.y-1
                        else:
                            new_y = tail.y+1

                        if current_head.x < tail.x:
                            new_x = tail.x-1
                        else:
                            new_x = tail.x+1
                        tail.move_by_coordinates(new_x, new_y)

                    elif dis_y > 1 and dis_x >= 0:
                        # diagonal move
                        if current_head.y < tail.y:
                            new_y = tail.y-1
                        else:
                            new_y = tail.y+1
                        tail.move_by_coordinates(current_head.x, new_y)

                    elif dis_x > 1 and dis_y >= 0:
                        # diagonal move
                        if current_head.x < tail.x:
                            new_x = tail.x-1
                        else:
                            new_x = tail.x+1
                        tail.move_by_coordinates(new_x, current_head.y)

                    else:
                        tail.move(direction)

                # check if the grid needs to be resized
                max_y, max_x = np.array(grid.shape)-1
                if (tail.y > max_y) or (tail.x > max_x) or (head.y > max_y) or (head.x > max_x):
                    grid = np.vstack([grid, np.zeros((1, grid.shape[1]))])
                    grid = np.hstack([grid, np.zeros((grid.shape[0], 1))])

                if (tail.y < 0) or (tail.x < 0):
                    grid = np.vstack([np.zeros((1, grid.shape[1])), grid])
                    grid = np.hstack([np.zeros((grid.shape[0], 1)), grid])
                    head.increment()
                    for t in nodes:
                        t.increment()

                current_head = tail
            grid[nodes[-1].y, nodes[-1].x] = 1

    return (int(np.sum(grid)))


test2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


initial_grid2 = """..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
...........H..............
..........................
..........................
..........................
..........................
.........................."""

assert get_part_two(test2) == 36
print(f'Part 2: {get_part_two(data)}')
