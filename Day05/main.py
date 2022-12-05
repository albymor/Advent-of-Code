with open('input.txt', 'r') as f:
    data = f.read()


test_stack = [['N', 'Z'],
              ['D', 'C', 'M'],
              ['P']]

test_moves = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

input_stacks = [['R','W','F','H','T','S'],
['W','Q','D','G','S'],
['W','T','B'],
['J','Z','Q','N','T','W','R','D'],
['Z','T','V','L','G','H','B','F'],
['G','S','B','V','C','T','P','L'],
['P','G','W','T','R','B','Z'],
['R','J','C','T','M','G','N'],
['W','B','G','L']]




def get_part_one(stacks, moves):
    rev = []
    for s in stacks:
        s.reverse()
        rev.append(s)

    stacks = rev

    ins = []
    moves = moves.split('\n')
    for l in moves:
        l = list(map(int, l.replace('move', '').replace(
            'from', ',').replace('to', ',').split(',')))
        ins.append(l)

    for l in ins:
        for i in range(l[0]):
            el = stacks[l[1]-1].pop()
            stacks[l[2]-1].append(el)

    final = ""
    for s in stacks:
        final += s[-1]

    return final 



assert get_part_one(test_stack, test_moves) == 'CMZ'
print(f'Part 1: {get_part_one(input_stacks,data)}')

# part 2

def get_part_two(stacks, moves):
    rev = []
    for s in stacks:
        s.reverse()
        rev.append(s)

    stacks = rev

    ins = []
    moves = moves.split('\n')
    for l in moves:
        l = list(map(int, l.replace('move', '').replace(
            'from', ',').replace('to', ',').split(',')))
        ins.append(l)

    for l in ins:
        removed = []
        for i in range(l[0]):
            removed.append(stacks[l[1]-1].pop())

        removed.reverse()
        for el in removed:
            stacks[l[2]-1].append(el)

    final = ""
    for s in stacks:
        final += s[-1]

    return final 



test_stack = [['N', 'Z'],
              ['D', 'C', 'M'],
              ['P']]

test_moves = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

input_stacks = [['R','W','F','H','T','S'],
['W','Q','D','G','S'],
['W','T','B'],
['J','Z','Q','N','T','W','R','D'],
['Z','T','V','L','G','H','B','F'],
['G','S','B','V','C','T','P','L'],
['P','G','W','T','R','B','Z'],
['R','J','C','T','M','G','N'],
['W','B','G','L']]


assert get_part_two(test_stack, test_moves) == 'MCD'
print(f'Part 2: {get_part_two(input_stacks,data)}')
