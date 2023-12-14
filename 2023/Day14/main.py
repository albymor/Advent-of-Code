import numpy as np

with open('input.txt', 'r') as f:
    data = f.read()

test = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""



def get_part_one(data):
    lines = data.split('\n')
    lines = np.array([list(line) for line in lines])

    lines = np.rot90(lines)

    for line in lines:
        for i, el in enumerate(line):
            if el == 'O':
                index = i
                while index > 0:
                    if line[index-1] == '.':
                        line[index-1] = 'O'
                        line[index] = '.'
                        index -= 1
                    else:
                        break
    lines = np.rot90(lines, 3)

    total = 0

    for i, line in enumerate(lines[::-1], start=1):
        unique, counts = np.unique(line, return_counts=True)
        d = dict(zip(unique, counts))
        if 'O' in d.keys():
            aa = d['O'] * i
            total += aa

    return total 

assert get_part_one(test) == 136
print(f'Part 1: {get_part_one(data)}')


def find_period(data):
    d = np.array(data)
    m = d.min()
    mins = np.where(d==m)
    print(mins)
    period = np.diff(mins[0]).max()
    return period

# part 2 
def get_part_two(data):
    lines = data.split('\n')
    lines = np.array([list(line) for line in lines])
    lines = np.rot90(lines)

    cache = {}
    window = []
    hit = 0

    samples = 100

    for j in range(1000000000):
        total = 0

        # apply the rotation
        for i in range(4):
            for line in lines:
                if ''.join(line) in cache.keys():
                    line = cache[''.join(line)]
                    continue
                for i, el in enumerate(line):
                    if el == 'O':
                        index = i
                        while index > 0:
                            if line[index-1] == '.':
                                line[index-1] = 'O'
                                line[index] = '.'
                                index -= 1
                            else:
                                break

                cache[''.join(line)] = line

            lines = np.rot90(lines, k=-1)

        lines = np.rot90(lines, k=3)

        #calculate the weight
        for i, line in enumerate(lines[::-1], start=1):
            unique, counts = np.unique(line, return_counts=True)
            d = dict(zip(unique, counts))
            if 'O' in d.keys():
                aa = d['O'] * i
                total += aa

        lines = np.rot90(lines, k=1)

        # need to find if results a re period 
        if total in window:
            #if we already seen this result but hit==o we are probably at the beginning of a period
            if hit == 0:
                # store the index where the period starts
                idx = j
            hit += 1
        else:
            # result never seen, so reset the watching window
            hit = 0
        window.append(total)

        # if we have seen the same result more than 100 times, we probably found the period
        if hit > samples:
            # find the period
            period = find_period(window[idx:])

            # remove the unperiodic part (+ one period) and  wind the index of the result
            p = (1000000000-idx) % period


            
            return window[p+idx-1] 

assert get_part_two(test) == 64
print(f'Part 2: {get_part_two(data)}')

