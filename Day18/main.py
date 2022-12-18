from collections import deque


with open('input.txt', 'r') as f:
    data = f.read()

test = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""   

def get_part_one(data):
    lines = data.split('\n')

    blocks = set()

    visible = 0

    for line in lines:
        x,y,z = tuple(map(int, line.split(',')))
        faces = 6

        if (x-1,y,z) in blocks:
            faces -= 2
        if (x+1,y,z) in blocks:
            faces -= 2
        if (x,y-1,z) in blocks:
            faces -= 2
        if (x,y+1,z) in blocks:
            faces -= 2
        if (x,y,z-1) in blocks:
            faces -= 2
        if (x,y,z+1) in blocks:
            faces -= 2

        visible += faces
        blocks.add((x,y,z))

    return visible

assert get_part_one(test) == 64
print(f'Part 1: {get_part_one(data)}')


# part 2 

def get_part_two(data):
    lines = data.split('\n')

    blocks = set()

    for line in lines:
        x,y,z = tuple(map(int, line.split(',')))
        blocks.add((x,y,z))

    # find min and max
    min_x = min(blocks, key=lambda x: x[0])[0]
    min_y = min(blocks, key=lambda x: x[1])[1]
    min_z = min(blocks, key=lambda x: x[2])[2]

    # find max
    max_x = max(blocks, key=lambda x: x[0])[0]
    max_y = max(blocks, key=lambda x: x[1])[1]
    max_z = max(blocks, key=lambda x: x[2])[2]

    # bfs to find external air
    visited = set()
    queue = deque()
    queue.append(((min_x-1, min_y-1, min_z-1)))

    while len(queue) > 0:
        x,y,z = queue.popleft()
        if (x,y,z) in visited:
            continue
        visited.add((x,y,z))

        if (x-1,y,z) not in blocks and (x-1,y,z) not in visited and x-1 >= min_x-1:
            queue.append((x-1,y,z))
        if (x+1,y,z) not in blocks and (x+1,y,z) not in visited and x+1 <= max_x+1:
            queue.append((x+1,y,z))
        if (x,y-1,z) not in blocks and (x,y-1,z) not in visited and y-1 >= min_y-1:
            queue.append((x,y-1,z))
        if (x,y+1,z) not in blocks and (x,y+1,z) not in visited and y+1 <= max_y+1:
            queue.append((x,y+1,z))
        if (x,y,z-1) not in blocks and (x,y,z-1) not in visited and z-1 >= min_z-1:
            queue.append((x,y,z-1))
        if (x,y,z+1) not in blocks and (x,y,z+1) not in visited and z+1 <= max_z+1:
            queue.append((x,y,z+1))

    # count touches
    touches = 0
    for x,y,z  in visited:
        if (x-1,y,z) in blocks:
            touches += 1
        if (x+1,y,z) in blocks:
            touches += 1
        if (x,y-1,z) in blocks:
            touches += 1
        if (x,y+1,z) in blocks:
            touches += 1
        if (x,y,z-1) in blocks:
            touches += 1
        if (x,y,z+1) in blocks:
            touches += 1

    return touches

assert get_part_two(test) == 58
print(f'Part 2: {get_part_two(data)}')

