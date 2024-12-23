from aoc.utils import timeit

with open('input.txt', 'r') as f:
    data = f.read()

test = """029A
980A
179A
456A
379A"""

import networkx as nx

#cache = {}


class NumericKeypad:
    def __init__(self):
        self.state = 'A'
        self.keys = {'7': (0,0), '8': (1,0), '9': (2, 0),
                     '4': (0,1), '5': (1,1), '6': (2, 1),
                     '1': (0,2), '2': (1,2), '3': (2, 2),
                                 '0': (1,3), 'A': (2,3)}

        self.adjacent_matrix = {'7': ['4', '8'], '8': ['7', '9', '5'], '9': ['8', '6'],
                                '4': ['1', '7', '5'], '5': ['2', '8', '4', '6'], '6': ['3', '9', '5'],
                                '1': ['2', '4'], '2': ['1', '3', '5', '0'], '3': ['2', '6', 'A'],
                                '0': ['2', 'A'], 'A': ['0', '3']}
        
        self.graph = nx.Graph()
        self.graph.add_nodes_from(self.keys.keys())
        for key, value in self.adjacent_matrix.items():
            for v in value:
                self.graph.add_edge(key, v)
        
    def shortest_path(self, end):
        sp = nx.all_shortest_paths(self.graph, self.state, end)
        dirs = []
        for path in sp:
            tmp = ''
            for s in list(zip(path, path[1:])):
                p1 = self.keys[s[0]]
                p2 = self.keys[s[1]]
                dx, dy = p2[0] - p1[0], p2[1] - p1[1]

                if dx < 0 and dy == 0:
                    tmp+= '<'
                elif dx > 0 and dy == 0:
                    tmp+= '>'
                elif dx == 0 and dy < 0:
                    tmp+= '^'
                elif dx == 0 and dy > 0:
                    tmp+= 'v'
                else:
                    raise ValueError(f'Invalid direction form {self.state} to {end} through {sp}')
            tmp+= 'A'
            dirs.append(tmp)

        self.state = end

        return sp, dirs
    
from functools import cache
class DirectionalKeypad:
    def __init__(self):
        self.state = 'A'
        self.keys = {'^': (1,0), 'A': (2,0), 'v': (1,1), '<': (0,1), '>': (2,1)}

        self.adjacent_matrix = {'^': ['v', 'A'], 'A': ['^', '>'], 'v': ['<', '>', '^'], '<': ['v'], '>': ['v', 'A']}

        self.graph = nx.Graph()
        self.graph.add_nodes_from(self.keys.keys())
        for key, value in self.adjacent_matrix.items():
            for v in value:
                self.graph.add_edge(key, v)

        
    @cache
    def shortest_path(self, end):
        # if (self.state, end) in cache:
        #     return cache[(self.state, end)]
        sp = nx.all_shortest_paths(self.graph, self.state, end)
        dirs = []
        for path in sp:
            tmp = ''
            for s in list(zip(path, path[1:])):
                p1 = self.keys[s[0]]
                p2 = self.keys[s[1]]
                dx, dy = p2[0] - p1[0], p2[1] - p1[1]

                if dx < 0 and dy == 0:
                    tmp += '<'
                elif dx > 0 and dy == 0:
                    tmp += '>'
                elif dx == 0 and dy < 0:
                    tmp += '^'
                elif dx == 0 and dy > 0:
                    tmp += 'v'
                else:
                    raise ValueError(f'Invalid direction form {self.state} to {end} through {sp}')
            tmp += 'A'
            dirs.append(tmp)

        #cache[(self.state, end)] = (sp, dirs)
        
        self.state = end


        return sp, dirs
    
import itertools
from tqdm import tqdm

@timeit
def get_part_one(data):
    lines = data.split('\n')

    

    
    

    total = 0

    for line in tqdm(lines):
        np = NumericKeypad()
        keys0 = []
        for i, c in enumerate(line):
            path, keys = np.shortest_path(c)
            keys0.append(keys)
        keys0 = list(map(lambda x: ''.join(x), list(itertools.product(*keys0))))
        for k in keys0:
            print(''.join(k), len(k))

        keys1 = {}
        for i, k in tqdm(enumerate(keys0)):
            keys1[i] = []
            dk1 = DirectionalKeypad()
            for c in k:
                path, keys = dk1.shortest_path(c)
                keys1[i].append(keys)

        tmp = []
        for k,v in keys1.items():
            tmp.append(list(map(lambda x: ''.join(x), list(itertools.product(*v)))))
        keys1 = [item for sublist in tmp for item in sublist]
        print(len(keys1))


        keys2 = {}
        for i, k in tqdm(enumerate(keys1)):
            keys2[i] = []
            dk2 = DirectionalKeypad()
            for c in k:
                path, keys = dk2.shortest_path(c)
                keys2[i].append(keys)

        tmp = []
        for k,v in keys2.items():
            tmp.append(list(map(lambda x: ''.join(x), list(itertools.product(*v)))))
        keys2 = [item for sublist in tmp for item in sublist]
        print(len(keys2))

        l = list(map(len, keys2))
        ll = min(l)


        total += (ll*int(line[:-1]))
    print(total)
    return total

assert get_part_one(test) == 126384
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    return 1

assert get_part_two(test) == 1
print(f'Part 2: {get_part_two(data)}')

