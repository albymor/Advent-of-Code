with open('input.txt', 'r') as f:
    data = f.read()

import time
import numpy as np


test = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

mp = []


class Node():
    def __init__(self, name):
        self.name = name
        self.is_visited = False
        self.height = ord(name)
        self.is_finish = False
        if name == 'S':
            self.height = 999999
        elif name == 'E':
            self.height = ord('z')
            self.is_finish = True

        self.children = []

    def get_non_visited_children(self):
        return list(filter(lambda x: not x.is_visited, self.children))

    def __repr__(self):
        return self.name if not self.is_visited else "\033[1;31m" + self.name + "\033[0;0m"


def solve(node, depth=0):

    new_nodes = []
    for n in node:
        n.is_visited = True
        if n.is_finish:
            return depth
    
    for n in node:
        children = n.get_non_visited_children()
        for c in children:
            if c.height - n.height < 2:
                new_nodes.append(c)

    new_nodes = list(set(new_nodes))

    #print_map()

    #time.sleep(0.1)
    
    return solve(new_nodes, depth+1)

    
def print_map():
    print('\n'.join([''.join([str(cell) for cell in row]) for row in mp])) 


def get_part_one(data):
    lines = data.split('\n')
    global mp

    mp = []
    

    for line in lines:
        mp.append(list(map(Node, list(line))))

    mp = np.array(mp)

    root = None
    for y in range(len(mp)):
        for x in range(len(mp[y])):
            if mp[y][x].name == 'S':
                root = mp[y][x]
            
            if y > 0:
                mp[y][x].children.append(mp[y-1][x])
            if y < len(mp) - 1:
                mp[y][x].children.append(mp[y+1][x])
            if x > 0:
                mp[y][x].children.append(mp[y][x-1])
            if x < len(mp[y]) - 1:
                mp[y][x].children.append(mp[y][x+1])

    return solve([root])


assert get_part_one(test) == 31
print(f'Part 1: {get_part_one(data)}')

# part 2


def get_part_two(data):
    lines = data.split('\n')
    global mp

    mp = []

    roots = []
    

    for line in lines:
        mp.append(list(map(Node, list(line))))

    mp = np.array(mp)

    root = None
    for y in range(len(mp)):
        for x in range(len(mp[y])):
            if mp[y][x].name == 'a':
                roots.append(mp[y][x])
            
            if y > 0:
                mp[y][x].children.append(mp[y-1][x])
            if y < len(mp) - 1:
                mp[y][x].children.append(mp[y+1][x])
            if x > 0:
                mp[y][x].children.append(mp[y][x-1])
            if x < len(mp[y]) - 1:
                mp[y][x].children.append(mp[y][x+1])

    return solve(roots)


assert get_part_two(test) == 29
print(f'Part 2: {get_part_two(data)}')
