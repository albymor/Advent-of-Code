with open('input.txt', 'r') as f:
    data = f.read()

test = """123"""
test2 = """1
10
100
2024"""   

def procedure(secret, iterations):
    for i in range(iterations):
        secret = ((secret*64) ^ secret)%16777216
        secret = ((secret//32)^ secret) %16777216
        secret = ((secret*2048)^ secret) %16777216

    return secret


def get_part_one(data):
    lines = list(map(int, data.split('\n')))

    res = sum(list(map(lambda x: procedure(x, 2000), lines)))

    return res

assert get_part_one(test2) == 37327623
print(f'Part 1: {get_part_one(data)}')

from collections import defaultdict, deque


def procedure2(secret, iterations, seq):
    seen = set()
    prev = secret%10
    s = deque([], maxlen=4)
    for _ in range(iterations):
        secret = ((secret*64) ^ secret)%16777216
        secret = ((secret//32)^ secret) %16777216
        secret = ((secret*2048)^ secret) %16777216

        if prev != None:
            diff = (secret%10) - prev
            s.append(diff)
        prev = secret%10

        if len(s) == 4:
            if tuple(s) not in seen:
                seq[tuple(s)] += secret%10

            seen.add(tuple(s))


    return seq


test3 = """1
2
3
2024"""
# part 2 
def get_part_two(data):
    lines = list(map(int, data.split('\n')))

    seq = defaultdict(lambda: 0)

    for l in lines:
        seq = procedure2(l, 2000, seq)

    return max(seq.values())

assert get_part_two(test3) == 23
print(f'Part 2: {get_part_two(data)}')

