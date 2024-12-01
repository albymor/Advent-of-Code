import numpy as np
# A: Rock
# B: Paper
# C: Scissors

point_mapping = {
    'A': 1,
    'B': 2,
    'C': 3,
}


class Move:
    def __init__(self, move):
        self.move = move
        self.point = point_mapping[move]

    def __eq__(self, __o: object) -> bool:
        return self.move == __o.move

    def __gt__(self, other):
        if self.move == 'A':
            return other.move == 'C'
        if self.move == 'C':
            return other.move == 'B'
        if self.move == 'B':
            return other.move == 'A'

    def __repr__(self) -> str:
        return self.move

#test 
rock = Move('A')
paper = Move('B')
scissors = Move('C')

assert rock > scissors  # TRUE
assert scissors > paper  # TRUE
assert paper > rock  # TRUE
assert not(rock > rock)  # FALSE
assert not(scissors > rock)  # FALSE
assert not(scissors == rock)  # FALSE
assert scissors == scissors  # TRUE




mine_mapping = {
    'X' :'A',
    'Y' :'B',
    'Z' :'C'
}

elf = []
mine = []

with open('input.txt', 'r') as f:
    all_moves = f.read().splitlines()

for moves in all_moves:
    moves = moves.split(' ')
    elf.append(Move(moves[0]))
    mine.append(Move(mine_mapping[moves[1]]))


score = 0
for m,e in zip(mine, elf):
    if m == e:
        score += (3+m.point)
    elif m > e:
        score += (6+m.point)
    else:
        score += (0+m.point)


print(f'Part 1: {score}')


# part 2


def get_result(m, e):
    if m == e:
        return 3
    elif m > e:
        return 6
    else:
        return 0

outcomes = []
for moves in all_moves:
    moves = moves.split(' ')
    outcomes.append(moves[1])

score = 0

possible_moves = [Move(a) for a in ['A', 'B', 'C']]

for e, o in zip(elf,outcomes):
    possible_outcomes = np.array([get_result(m, e) for m in possible_moves])
    if o == 'Y': # draw
        score += (3+e.point)
    elif o == 'Z': # win
        score += (6+possible_moves[np.argmax(possible_outcomes)].point)
    else:          # win
        score += (0+possible_moves[np.argmin(possible_outcomes)].point)


print(f'Part 2: {score}')



