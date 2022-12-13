from itertools import zip_longest
import functools

with open('input.txt', 'r') as f:
    data = f.read()

test = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def solve(left, right):
    is_ok = 0
    if left == None:
        #run out of left
        is_ok = 1
        return is_ok
    elif right == None:
        #run out of right
        is_ok = -1
        return is_ok

    if type (left) == int and type(right) == int:
        if left > right:
            is_ok = -1
        elif left < right:
            is_ok = 1
        
        return is_ok

    if type(left) != type(right) and (type(left) == list or type(right) == list):
            if type(left) != list:
                left = [left]
            else:
                right = [right]

    if type(left) == list:
        for l, r in zip_longest(left, right):
            is_ok = solve(l, r)
            if is_ok != 0:
                break

    return is_ok
        

def get_part_one(data):
    pairs_raw = data.split('\n\n')

    ok = 0

    for i, pair in enumerate(pairs_raw):
        pair = pair.split('\n')
        right = eval(pair[0])
        left = eval(pair[1])

        res = solve(right, left)
        if res == 1:
            ok += (i+1)

    return ok


assert get_part_one(test) == 13
print(f'Part 1: {get_part_one(data)}')

# part 2


def get_part_two(data):
    packets_raw = data.split('\n')

    ok = 0

    packets = []
    for pkt in packets_raw:
        if len(pkt) == 0:
            continue
        packets.append(eval(pkt))

    packets.append([[6]])
    packets.append([[2]])

    packets.sort(key=functools.cmp_to_key(solve))

    packets = packets[::-1]

    idx6 = packets.index([[6]])+1
    idx2 = packets.index([[2]])+1

    return idx2*idx6

assert get_part_two(test) == 140
print(f'Part 2: {get_part_two(data)}')
