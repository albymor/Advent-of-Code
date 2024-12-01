with open('input.txt', 'r') as f:
    data = f.read()

test = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

from collections import deque

class Node():
    def __init__(self, weight) -> None:
        self.weight = weight
        self.visited = False

    def __repr__(self) -> str:
        return str(self.weight)
        

def get_part_one(data):
    lines = data.split('\n')

    mappa = [list(map(Node,x)) for x in lines]

    print(mappa)

    nodes = deque([mappa[0][0]])

    while len(nodes)> 0:
        sorted(nodes, lambda x: x.weight)
        n = nodes.popleft()

        


    return None

assert get_part_one(test) == 0
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    return 1

assert get_part_two(test) == 1
print(f'Part 2: {get_part_two(data)}')

