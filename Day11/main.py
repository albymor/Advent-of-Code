with open('input.txt', 'r') as f:
    data = f.read()


from copy import copy
from itertools import accumulate

test = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


class Monkey:
    def __init__(self, items, op, test, test_true, test_false):
        self.items = items
        self.op = op
        self.test = test
        self.tt = test_true
        self.tf = test_false
        self.inspected = 0

    def execute(self, other_monkeys):
        temp = copy(self.items)
        for old in temp:
            new = eval(self.op)
            new = new // 3
            rem = new % self.test
            if rem == 0:
                other_monkeys[self.tt].items.append(new)
            else:
                other_monkeys[self.tf].items.append(new)

            self.inspected += 1

            self.items.pop(0)

    def __repr__(self):
        return f'Items: {",".join(list(map(str, self.items))):<25} Operation: {self.op:<10} Test: {self.test:<5} Test True: {self.tt:<5} Test False: {self.tf:<5} Inspected: {self.inspected:<5}'


def get_part_one(data):
    monkeys = []
    monkeys_raw = data.split('\n\n')

    for monkey_raw in monkeys_raw:
        lines = monkey_raw.split('\n')
        items = list(map(int, lines[1].split(':')[1].split(',')))
        op = lines[2].split('=')[1].strip()
        t = int(lines[3].split(' ')[-1])
        tt = int(lines[4].split(' ')[-1])
        tf = int(lines[5].split(' ')[-1])

        mon = Monkey(items, op, t, tt, tf)
        monkeys.append(mon)

    for r in range(20):
        for mon in monkeys:
            mon.execute(monkeys)

    act = []
    for mon in monkeys:
        act.append(mon.inspected)

    act.sort()

    act = act[-2:]

    prod = 1

    for a in act:
        prod *= a

    return prod


assert get_part_one(test) == 10605
print(f'Part 1: {get_part_one(data)}')

# part 2


class Monkey2:
    def __init__(self, items, op, test, test_true, test_false):
        self.items = items
        self.op = op
        self.test = test
        self.tt = test_true
        self.tf = test_false
        self.inspected = 0
        self.lcm = None

    def execute(self, other_monkeys):
        temp = copy(self.items)
        for old in temp:
            new = eval(self.op)
            new = new % self.lcm
            rem = new % self.test
            if rem == 0:
                other_monkeys[self.tt].items.append(new)
            else:
                other_monkeys[self.tf].items.append(new)

            self.inspected += 1

            self.items.pop(0)

    def __repr__(self):
        return f'Items: {",".join(list(map(str, self.items))):<25} Operation: {self.op:<10} Test: {self.test:<5} Test True: {self.tt:<5} Test False: {self.tf:<5} Inspected: {self.inspected:<5}'


def get_part_two(data):
    monkeys = []
    monkeys_raw = data.split('\n\n')

    lcm = 1

    for monkey_raw in monkeys_raw:
        lines = monkey_raw.split('\n')
        items = list(map(int, lines[1].split(':')[1].split(',')))
        op = lines[2].split('=')[1].strip()
        t = int(lines[3].split(' ')[-1])
        tt = int(lines[4].split(' ')[-1])
        tf = int(lines[5].split(' ')[-1])
        lcm *= t

        mon = Monkey2(items, op, t, tt, tf)
        monkeys.append(mon)

    for mon in monkeys:
        mon.lcm = lcm

    for r in range(10000):
        for mon in monkeys:
            mon.execute(monkeys)

    act = []
    for mon in monkeys:
        act.append(mon.inspected)

    act.sort()

    act = act[-2:]

    prod = 1

    for a in act:
        prod *= a

    return prod


assert get_part_two(test) == 2713310158
print(f'Part 2: {get_part_two(data)}')
