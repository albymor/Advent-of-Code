import numpy as np
import re
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


class Node():
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.sizes = []
        self.parent = parent

    def add_child(self, node):
        self.children.append(node)

    def get_size(self):
        total = 0
        for c in self.children:
            total += c.get_size()

        total += sum(self.sizes)

        return total

    def get_parent(self):
        return self.parent

    def has_child(self):
        return len(self.children) > 0


def get_fs(data):
    root = Node('root', None)
    current_node = root
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
            dir_size = re.findall(r'(\d+) ', l)
            if len(dir_size) > 0:
                current_node.sizes.append(int(dir_size[0]))

    return root


def get_size(node, total):
    size = node.get_size()
    if size < 100000:
        total += size
    for c in node.children:
        total = get_size(c, total)

    return total


def get_part_one(data):
    root = get_fs(data)
    return get_size(root, 0)


assert get_part_one(test) == 95437
print(f'Part 1: {get_part_one(data)}')

# part 2


def get_part_two(data):
    root = get_fs(data)

    sizes = get_min(root, [])

    free = 70000000 - sizes[0]

    expected_free = free + np.array(sizes)
    expected_free = expected_free[expected_free > 30000000]
    idx = np.argmin(expected_free)

    return expected_free[idx]-free


def get_min(node, total):
    size = node.get_size()
    total.append(size)
    for c in node.children:
        total + get_min(c, total)

    return total


assert get_part_two(test) == 24933642
print(f'Part 1: {get_part_two(data)}')
