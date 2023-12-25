import networkx as nx
import matplotlib.pyplot as plt

with open('input.txt', 'r') as f:
    data = f.read()

test = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""





def get_part_one(data):
    lines = data.split('\n')

    g = nx.Graph()

    for line in lines:
        parent, child = line.split(': ')
        child = child.split(' ')
        for c in child:
            g.add_edge(parent, c)

    to_disconnect = nx.minimum_edge_cut(g)

    g.remove_edges_from(to_disconnect)

    prod = 1

    a= list(nx.connected_components(g))
    for i in a:
        prod *= len(i)
     

    return prod

assert get_part_one(test) == 54
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    return 1

assert get_part_two(test) == 1
print(f'Part 2: {get_part_two(data)}')

