from collections import Counter

with open('input.txt', 'r') as f:
    data = f.read()

test = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""   


           
def transpose(x):
	return list(map(list, zip(*x)))

def match(lines):
    reflection_points = []
    for i in range(len(lines)-1):
        if lines[i] == lines[i+1]:
            reflection_points.append(i)


    for i in reflection_points:
        index = i
        a = i
        b = i+1

        while a > 0 and b < len(lines)-1:
            a -= 1
            b += 1
            if lines[a] != lines[b]:
                break
        else:
            return index+1
            
    
    return None


def get_part_one(data):
    _sum = 0
    patterns = data.split('\n\n')

    for p_i, pattern in enumerate(patterns):

        pattern = pattern.split('\n')

        lines = transpose(pattern)

        res = match(lines)

        if res is not None:
            _sum += res
        else:
            
            lines = pattern
            res = match(lines)
            if res is not None:
                _sum += (res*100)
            else:
                assert False
    return _sum

assert get_part_one(test) == 405
print(f'Part 1: {get_part_one(data)}')


def hamming_distance(x, y):
    if len(x) != len(y):
        print('Not same length')

    distance = 0
    for c in zip(x, y):
        if c[0] != c[1]:
            distance += 1

    return distance   

def match_2(lines):
    reflection_points = []
    for i in range(len(lines)-1):
        distance = hamming_distance(lines[i],lines[i+1])
        if 0 <= distance <=1:
            reflection_points.append(i)


    for i in reflection_points:
        index = i
        a = i
        b = i+1

        smudge = 0

        while a >= 0 and b <= len(lines)-1:
            distance = hamming_distance(lines[a], lines[b])
            if distance > 1:
                break
            elif distance == 1:
                smudge += 1

            a -= 1
            b += 1
        else:
            if smudge == 1:
                return index+1
            
    
    return None



# part 2 
def get_part_two(data):
    _sum = 0
    patterns = data.split('\n\n')

    for p_i, pattern in enumerate(patterns):

        pattern = pattern.split('\n')

        lines = transpose(pattern)

        res = match_2(lines)

        if res is not None:
            _sum += res
        else:
            
            lines = pattern
            res = match_2(lines)
            if res is not None:
                _sum += (res*100)
            else:
                assert False
    return _sum

assert get_part_two(test) == 400
print(f'Part 2: {get_part_two(data)}')

