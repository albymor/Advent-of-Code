import numpy as np
with open('input.txt', 'r') as f:
    data = f.read()

test = """30373
25512
65332
33549
35390"""


def rot(*arr, k=1):
    tmp = []
    for a in arr:
        tmp.append(np.rot90(a, k=k))

    return (tuple(tmp))


def get_seen_grid(data):
    data = data.split('\n')
    grid = []
    for d in data:
        grid.append(list(map(int, list(d))))

    grid = np.array(grid)
    seen_grid = np.zeros(grid.shape)

    compute_visibility(grid, seen_grid)

    grid, seen_grid = rot(grid, seen_grid)
    compute_visibility(grid, seen_grid)

    grid, seen_grid = rot(grid, seen_grid)
    compute_visibility(grid, seen_grid)

    grid, seen_grid = rot(grid, seen_grid)
    compute_visibility(grid, seen_grid)

    # back to the original rotation
    grid, seen_grid = rot(grid, seen_grid)

    return grid, seen_grid


def compute_visibility(grid, seen_grid):
    for r, line in enumerate(grid):
        l_max = -1
        for i, l in enumerate(line):
            if l > l_max:
                l_max = l
                seen_grid[r, i] = 1


def get_part_one(data):

    _, seen_grid = get_seen_grid(data)
    count = seen_grid.sum()

    return int(count)


assert get_part_one(test) == 21
print(f'Part 1: {get_part_one(data)}')

# part 2


def get_scores_matrix(grid, score_matrix):
    for r, line in enumerate(grid):
        for i in range(line.size):
            chunk = line[:i+1]
            chunk = np.flip(chunk)
            height = 10
            vis = 0
            if len(chunk) != 1:
                for aa, c in enumerate(chunk):
                    if aa == 0:
                        height = c
                        continue
                    vis += 1
                    if (c >= height):
                        break
            else:
                vis = 0

            score_matrix[r, i] = vis


def get_part_two(data):

    scores = []

    grid, _ = get_seen_grid(data)

    weight_grid = np.zeros(grid.shape)

    count = 0
    get_scores_matrix(grid, weight_grid)
    scores.append(weight_grid.copy())

    grid, weight_grid = rot(grid, weight_grid)
    get_scores_matrix(grid, weight_grid)
    scores.append(weight_grid.copy())

    grid, weight_grid = rot(grid, weight_grid)
    get_scores_matrix(grid, weight_grid)
    scores.append(weight_grid.copy())

    grid, weight_grid = rot(grid, weight_grid)
    get_scores_matrix(grid, weight_grid)
    scores.append(weight_grid.copy())

    score_matrix = np.ones(grid.shape)

    for i, m in enumerate(scores):
        score_matrix = score_matrix*rot(m, k=-i)

    return int(score_matrix.max())


assert get_part_two(test) == 8
print(f'Part 2: {get_part_two(data)}')
