with open('input.txt', 'r') as f:
    data = f.read()

test = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""" 


import networkx as nx
from collections import defaultdict, deque

def get_part_one(data):
    lines = data.split('\n')
    G = nx.Graph()

    for line in lines:
        a, b = line.split('-')
        G.add_node(a)
        G.add_node(b)
        G.add_edge(a, b)

    graph = defaultdict(lambda: [])
    for line in lines:
        a, b = line.split('-')
        graph[a].append(b)
        graph[b].append(a)

    triangles = set()
    for el in graph:
        q = deque([(el, [el], 0)])
        while q:
            e, tri, depth = q.popleft()
            if depth > 2: continue
            for n in graph[e]:
                if n == el and depth==2:                    
                    triangles.add(tuple(sorted(tri)))
                    continue
                if n not in tri:
                    q.append((n, tri+ [n], depth+1))
        
    res = 0
    for t in triangles:
        for node in t:
            if node.startswith('t'):
                res += 1
                break
    return res

assert get_part_one(test) == 7
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')
    G = nx.Graph()

    for line in lines:
        a, b = line.split('-')
        G.add_node(a)
        G.add_node(b)
        G.add_edge(a, b)


    cliques = nx.find_cliques(G)


    res = ','.join(sorted(max(list(cliques), key=len)))
    print(res)


    return res 

assert get_part_two(test) == 'co,de,ka,ta'
print(f'Part 2: {get_part_two(data)}')

