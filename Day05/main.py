with open('input.txt', 'r') as f:
    data = f.read()


test = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def parser(raw_input):
    raw_stacks , raw_moves = raw_input.split('\n\n')

    stacks_d = {}
    # stacks
    for line in raw_stacks.split('\n'):
        for i, el in enumerate(line):
            if el.isalpha():
                idx = (i-1)//4
                if idx in stacks_d:
                    stacks_d[idx].append(el)
                else:
                    stacks_d[idx] = [el]

    stacks = []
    for k in sorted(stacks_d):
        a = stacks_d[k]
        a.reverse()
        stacks.append(a)

    
    instruction = []
    moves = raw_moves.split('\n')
    for move in moves:
        move = move.split(' ')
        move = [move[1], move[3], move[5]]
        move = list(map(int, move))
        instruction.append(move)

    return stacks, instruction


def get_part_one(stacks, instruction):
    for l in instruction:
        for i in range(l[0]):
            el = stacks[l[1]-1].pop()
            stacks[l[2]-1].append(el)

    final = ""
    for s in stacks:
        final += s[-1]

    return final 



assert get_part_one(*parser(test)) == 'CMZ'
print(f'Part 1: {get_part_one(*parser(data))}')

# part 2

def get_part_two(stacks, instruction):
    for l in instruction:
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


assert get_part_two(*parser(test)) == 'MCD'
print(f'Part 2: {get_part_two(*parser(data))}')
