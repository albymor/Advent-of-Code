import re
from copy import copy
with open('input.txt', 'r') as f:
    data = f.read()

test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    
def get_part_oneb(data):
    tree = ['root']
    file_sizes = []
    resume = {}
    lfs = []
    data = data.split('\n')
    for l in data:
        if "$ cd" in l:
            path = '-'.join(tree)
            if len(lfs) > 0:
                file_sizes.append(lfs)
                resume[path] = copy(file_sizes)
                lfs = []
            l = l.split(' ')
            directory = l[-1]
            if ('/' in directory):
                tree = ['root']
                if len(file_sizes) > 0:
                    file_sizes = file_sizes[0]
            elif ('..' in directory):                
                #if len(tree) == 1:
                file_sizes = [] #file_sizes[:-1]
                tree = tree[:-1]
            else:
                tree.append(directory)
        elif "$ ls" in l:
            pass
        else:
            aa = re.findall(r'(\d+) ', l)
            if len(aa)>0:
                lfs.append(int(aa[0]))

    path = '-'.join(tree)
    if len(lfs) > 0:
        file_sizes.append(lfs)
        resume[path] = copy(file_sizes)

    print(resume)


    sum_resume = {}
    for k in resume:
        sum_resume[k] = sum(resume[k])

    total = 0
    for k in sum_resume:
        if sum_resume[k] < 100000:
            total += sum_resume[k]

    print(total)
    print(sum_resume)

    return total

class Node():
    def __init__(self, name, parent):
        self.name = name
        self.childs = []
        self.sizes = []
        self.parent = parent

    def add_child(self, node):
        self.childs.append(node)

    def get_size(self):
        total = 0
        for c in self.childs:
            total += c.get_size()

        total += sum(self.sizes)

        return total

    def get_parent(self):
        return self.parent

    def has_child(self):
        return len(self.childs) > 0

    
        



def get_part_one(data):
    root = Node('root', None)
    current_node =  root
    file_sizes = []
    resume = {}
    lfs = []
    data = data.split('\n')
    for l in data:
        if "$ cd" in l:
            l = l.split(' ')
            directory = l[-1]
            if ('/' in directory):
                current_node = root
            elif ('..' in directory):                
                current_node = current_node.get_parent()
            else:
                n = Node(directory, current_node)
                current_node.add_child(n)
                current_node = n

        elif "$ ls" in l:
            pass
        else:
            aa = re.findall(r'(\d+) ', l)
            if len(aa)>0:
                current_node.sizes.append(int(aa[0]))


    tt = get_size(root, 0)

    return tt

def get_size(node, total):
    size = node.get_size()
    if size < 100000:
        total += size
    for c in node.childs:
        total = get_size(c, total)

    return total


    
assert get_part_one(test) == 95437
print(f'Part 1: {get_part_one(data)}')

# part 2

import numpy as np
def get_part_two(data):
    root = Node('root', None)
    current_node =  root
    file_sizes = []
    resume = {}
    lfs = []
    data = data.split('\n')
    for l in data:
        if "$ cd" in l:
            l = l.split(' ')
            directory = l[-1]
            if ('/' in directory):
                current_node = root
            elif ('..' in directory):                
                current_node = current_node.get_parent()
            else:
                n = Node(directory, current_node)
                current_node.add_child(n)
                current_node = n

        elif "$ ls" in l:
            pass
        else:
            aa = re.findall(r'(\d+) ', l)
            if len(aa)>0:
                current_node.sizes.append(int(aa[0]))


    tt = get_min(root, [])

    free = 70000000 - tt[0]

    aa = free + np.array(tt)
    aa = aa[aa>30000000]
    idx = np.argmin(aa)


    return aa[idx]-free

def get_min(node, total):
    size = node.get_size()
    total.append(size)
    for c in node.childs:
        total+ get_min(c, total)

    return total

assert get_part_two(test) == 24933642
print(f'Part 1: {get_part_two(data)}')
