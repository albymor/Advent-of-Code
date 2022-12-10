with open('input.txt', 'r') as f:
    data = f.read()

test = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


class CPU:
    def __init__(self, instructions):
        self.instructions = instructions
        self.x = 1
        self.res_clock = 0
        self.cache = 0
        self.current_instruction = None
        pass

    def update_register(self):
        self.x += self.cache

    def load_next_instruction(self):
        if len(self.instructions) > 0:
            tmp = self.instructions.pop(0)
        else:
            tmp = 'noop'

        if 'noop' in tmp:
            self.cache = 0
            self.res_clock = 1
            self.current_instruction = tmp
        elif 'addx' in tmp:
            ins = tmp.split(' ')
            self.cache = int(ins[1])
            self.res_clock = 2
            self.current_instruction = ins[0]

        else:
            raise 'Unknown instruction'

    def execute(self):
        self.res_clock -= 1
        if self.res_clock <= 0:
            self.update_register()
            self.load_next_instruction()

    def has_instruction(self):
        return len(self.instructions) > 0

    def __repr__(self):
        return f'{self.current_instruction} x={self.x} res_clock={self.res_clock} cache={self.cache}'


def get_part_one(data):
    ins = data.split('\n')
    cpu = CPU(ins)

    check_points = [20, 60, 100, 140, 180, 220]

    vals = []

    cycle = 1
    while cpu.has_instruction():
        cpu.execute()
        #print(f"Cycle {cycle}", cpu)
        if cycle in check_points:
            vals.append(cycle*cpu.x)
        cycle += 1

    return sum(vals)


assert get_part_one(test) == 13140
print(f'Part 1: {get_part_one(data)}')

# part 2


def get_part_two(data):
    ins = data.split('\n')
    cpu = CPU(ins)

    checks = [20, 60, 100, 140, 180, 220]

    vals = []
    crt = []
    sprite_position = 0

    cycle = 1
    while cpu.has_instruction():
        cpu.execute()
        #print(f"Cycle {cycle}", cpu)
        sprite_position = cpu.x-1
        sprite_list = list(range(sprite_position, sprite_position+3))
        current_pixel = (cycle-1) % 40
        if current_pixel in list(range(sprite_position, sprite_position+3)):
            crt.append('#')
        else:
            crt.append('.')

        if not (cycle) % 40:
            crt.append('\n')

        cycle += 1

    return ''.join(crt).strip()


test2 = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""

assert get_part_two(test) == test2
print(f'Part 2:\n{get_part_two(data)}')
