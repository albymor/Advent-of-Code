with open('input.txt', 'r') as f:
    data = f.read()


letters = [chr(x+ord('a')) for x in range(26)] + \
    [chr(x+ord('a')).upper() for x in range(26)]


def get_w(c):
    return letters.index(c) + 1


assert get_w('a') == 1
assert get_w('A') == 27


sum_prio = 0

data = data.split('\n')

for d in data:

    h = d[:len(d)//2]
    l = d[len(d)//2:]

    common = set(l) & set(h)
    sum_prio += get_w(list(common)[0])

    assert len(h) == len(l)
    assert len(common) == 1

print(f'Part 1: {sum_prio}')


# part 2

data_u = [set(d) for d in data]

sum_prio = 0
for i in range(len(data_u)//3):
    chunk = data_u[(i*3):(i*3)+3]
    common = chunk[0].intersection(*chunk[1:])

    assert len(common) == 1

    sum_prio += get_w(list(common)[0])

print(f'Part 2: {sum_prio}')
