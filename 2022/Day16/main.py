import re
from copy import copy
from tqdm import tqdm


with open('input.txt', 'r') as f:
    data = f.read()

test = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


class Node:
    def __init__(self, name, flow_rate):
        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = []
        self.distances = None

    def add_tunnel(self, tunnel):
        self.tunnels.append(tunnel)

    def __repr__(self):
        return f'{self.name}'


cache = set()


def get_part_one(data):
    lines = data.split('\n')

    nodes = {}
    for line in lines:
        aa = re.findall(
            r"Valve (\w\w) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (.*)", line)
        nodes[aa[0][0]] = {'flow_rate': int(
            aa[0][1]), 'tunnels': aa[0][2].split(', ')}

    nodes_objs = {}

    for node in nodes:
        nodes_objs[node] = Node(node, nodes[node]['flow_rate'])

    for node in nodes:
        for tunnel in nodes[node]['tunnels']:
            nodes_objs[node].add_tunnel(tunnel)

    for node in nodes:
        distances = get_distance(nodes_objs[node], nodes_objs)
        nodes_objs[node].distances = distances

    current_node = nodes_objs['AA']

    visit_mask = {k: False for k in nodes_objs}

    return search(current_node, 30, nodes_objs, 0, visit_mask)


def search(current_node, time, nodes, score, visit_mask):

    if (current_node, time, tuple(visit_mask.values())) in cache:
        return score

    visit_mask = copy(visit_mask)

    if time <= 0:
        return score

    scores = []

    score += current_node.flow_rate*time
    visit_mask[current_node.name] = True
    scores.append(score)

    for k in current_node.distances:
        if visit_mask[k] == False:
            scores.append(
                search(nodes[k], time-(current_node.distances[k]+1), nodes, score, visit_mask))

    cache.add((current_node, time, tuple(visit_mask.values())))
    return max(scores)


def get_distance(current_node, nodes):
    distance = 1
    distances = {}

    nn = [current_node.name]
    while len(distances) < len(nodes):
        tmp = []
        for n in nn:
            tmp = tmp + nodes[n].tunnels

        nn = list(set(tmp))
        for n in nn:
            if n not in distances:
                distances[n] = distance
        distance += 1
    distances = {k: v for k, v in distances.items(
    ) if nodes[k].flow_rate != 0 and k != current_node.name}
    return distances


assert get_part_one(test) == 1651
print(f'Part 1: {get_part_one(data)}')

# part 2


def int_to_visit_mask(n, nodes, bit_wise_not=False):
    mask = {}
    for i, node in enumerate(nodes):
        a = bool(n & (1 << i))
        if bit_wise_not:
            a = not a
        mask[node] = a
    return mask


def get_part_two(data):
    lines = data.split('\n')

    nodes = {}
    for line in lines:
        aa = re.findall(
            r"Valve (\w\w) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (.*)", line)
        nodes[aa[0][0]] = {'flow_rate': int(
            aa[0][1]), 'tunnels': aa[0][2].split(', ')}

    nodes_objs = {}

    for node in nodes:
        nodes_objs[node] = Node(node, nodes[node]['flow_rate'])

    for node in nodes:
        for tunnel in nodes[node]['tunnels']:
            nodes_objs[node].add_tunnel(tunnel)

    for node in nodes:
        distances = get_distance(nodes_objs[node], nodes_objs)
        nodes_objs[node].distances = distances

    current_node = nodes_objs['AA']

    tbd = [k for k in nodes_objs if nodes_objs[k].flow_rate != 0 or k == 'AA']

    max_ = 0

    for i in tqdm(range(2**(len(tbd)))):
        mask = int_to_visit_mask(i, tbd)
        not_mask = int_to_visit_mask(i, tbd, bit_wise_not=True)
        l = search(current_node, 26, nodes_objs, 0, mask)
        r = search(current_node, 26, nodes_objs, 0, not_mask)
        max_ = max(max_, l + r)

    return max_


assert get_part_two(test) == 1707
print(f'Part 2: {get_part_two(data)}')
