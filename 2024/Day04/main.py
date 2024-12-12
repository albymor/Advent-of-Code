with open('input.txt', 'r') as f:
    data = f.read()

test = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""" 


def search(x, y, dir_x, dir_y, lines, pattern, length):
    x_max = len(lines[0])
    y_max = len(lines)

    steps_x = [((i*dir_x+x)) for i in range(length)]
    steps_y = [((i*dir_y+y)) for i in range(length)]

    steps_x = [x for x in steps_x if 0<=x<x_max]
    steps_y = [y for y in steps_y if 0<=y<y_max]


    pos = list(zip(steps_x, steps_y))

    word = ''

    for x, y in pos:
        word += lines[y][x]

    if pattern in word or pattern in word[::-1]:
        return True
    else:
        return False


def get_part_one(data):
    lines = list(map(list, data.split('\n')))

    res = 0

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if 'X' in c:
                res += search(x, y, 1, 0, lines, 'XMAS', 4)
                res += search(x, y, 1, -1, lines, 'XMAS', 4)
                res += search(x, y, 0, -1, lines, 'XMAS', 4)
                res += search(x, y, -1, -1, lines, 'XMAS', 4)
                res += search(x, y, -1, 0, lines, 'XMAS', 4)
                res += search(x, y, -1, 1, lines, 'XMAS', 4)
                res += search(x, y, 0, 1, lines, 'XMAS', 4)
                res += search(x, y, 1, 1, lines, 'XMAS', 4)

    return res

assert get_part_one(test) == 18
print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = list(map(list, data.split('\n')))

    res = 0

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if 'A' in c:
                res += search(x-1, y+1, 1, -1, lines, 'MAS', 3) and search(x-1, y-1, 1, 1, lines, 'MAS', 3)

    return res

assert get_part_two(test) == 9
print(f'Part 2: {get_part_two(data)}')

