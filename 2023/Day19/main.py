import re
from collections import OrderedDict
import numpy as np


with open('input.txt', 'r') as f:
    data = f.read()

test = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}""" 

class Rule():
    def __init__(self, symbol, op, qty, dest):
        self.symbol = symbol
        self.op = op
        self.dest = dest
        self.qty = int(qty)


    def __repr__(self):
        return f'{self.symbol} {self.op} {self.qty} -> {self.dest}'


class Workflow():
    def __init__(self, name, rules):
        self.name = name
        r = rules.split(',')
        self.rules = []
        regex = r"(\w+)(<|>)(\d+)\:(\w+)|(A|R|\w+)"
        for rule in r:
            m = re.match(regex, rule)
            if m:
                groups = [g for g in m.groups() if g is not None]
                if len(groups) == 4:
                    self.rules.append(Rule(*groups))
                else:
                    self.rules.append(Rule(None, None, 0, groups[0]))



    def solve(self, rating, workflows):
        print(f'{self.name}', end='->')
        for rule in self.rules:
            if rule.op == None:
                if rule.dest == 'A':
                    return True
                elif rule.dest == 'R':
                    return False
                else:
                    return workflows[rule.dest].solve(rating, workflows)            
            elif rule.op == '<':
                if rating[rule.symbol] < rule.qty:
                    if rule.dest == 'A':
                        return True
                    elif rule.dest == 'R':
                        return False
                    else:
                        return workflows[rule.dest].solve(rating, workflows)
                else:
                    continue
            elif rule.op == '>':
                if rating[rule.symbol] > rule.qty:
                    if rule.dest == 'A':
                        return True
                    elif rule.dest == 'R':
                        return False
                    else:
                        return workflows[rule.dest].solve(rating, workflows)
                else:
                    continue            
            else:
                raise Exception('Unknown operator')
            




def get_part_one(data):
    flows, rat = data.split('\n\n')

    workflows = {}

    for wf in flows.split('\n'):
        name, rules = wf.split('{')
        workflows[name]=Workflow(name, rules[:-1])

    ratings = []

    for rating in rat.split('\n'):
        rating = rating[1:-1]
        r = OrderedDict()
        for kv in rating.split(','):
            k, v = kv.split('=')
            r[k] = int(v)
        ratings.append(r)

    print(workflows)
    print(ratings)

    start = workflows['in']
    total = 0
    for rating in ratings:
        if start.solve(rating, workflows):
            t = 0
            for k, v in rating.items():
                t += v
            print(f'->>> {t}')
            total += t

        else:
            print('->>> R')

    print(total)

    return total

assert get_part_one(test) == 19114
print(f'Part 1: {get_part_one(data)}')

roia = []
class Workflow2():
    def __init__(self, name, rules):
        self.name = name
        r = rules.split(',')
        self.rules = []
        regex = r"(\w+)(<|>)(\d+)\:(\w+)|(A|R|\w+)"
        for rule in r:
            m = re.match(regex, rule)
            if m:
                groups = [g for g in m.groups() if g is not None]
                if len(groups) == 4:
                    self.rules.append(Rule(*groups))
                else:
                    self.rules.append(Rule(None, None, 0, groups[0]))


        self.res = []

    def trap(self, rating, workflows):
        print(rating)
        self.res.append(rating)
        roia.append(rating)
        return True
    

    def bounds(self, bounds, limit, symbol):
        if symbol == '<':
            r = np.arange(bounds[0], bounds[1])
            a = r<limit
            n = np.where(a)[0]
            return [n.min(), n.max() ]
        else:
            r = np.arange(bounds[0], bounds[1])
            a = r>limit
            n = np.where(a)[0]
            return [n.min(), n.max() ]


    def solve(self, rating, workflows):
        print(f'{self.name}', end='->')
        for rule in self.rules:
            if rule.op == None:
                if rule.dest == 'A':
                    self.trap(rating, workflows)
                    continue
                elif rule.dest == 'R':
                    continue
                else:
                    workflows[rule.dest].solve(rating, workflows)            
            elif rule.op == '<':
                #rating[rule.symbol][1] = rule.qty
                rating[rule.symbol]= self.bounds(rating[rule.symbol], rule.qty, rule.op)
                if rule.dest == 'A':
                    self.trap(rating, workflows)
                    continue
                elif rule.dest == 'R':
                    continue
                else:
                    workflows[rule.dest].solve(rating, workflows)
            elif rule.op == '>':
                rating[rule.symbol][0] = rule.qty
                if rule.dest == 'A':
                    self.trap(rating, workflows)
                    continue
                elif rule.dest == 'R':
                    continue
                else:
                    workflows[rule.dest].solve(rating, workflows)           
            else:
                raise Exception('Unknown operator')
            
# part 2 
def get_part_two(data):
    initial_condition_set= {param_name: [0, 4001] for param_name in ("x", "m", "a", "s")}
    print(initial_condition_set)
    flows, rat = data.split('\n\n')

    workflows = {}

    for wf in flows.split('\n'):
        name, rules = wf.split('{')
        workflows[name]=Workflow2(name, rules[:-1])

    ratings = []

    for rating in rat.split('\n'):
        rating = rating[1:-1]
        r = OrderedDict()
        for kv in rating.split(','):
            k, v = kv.split('=')
            r[k] = int(v)
        ratings.append(r)

    print(workflows)
    print(ratings)

    start = workflows['in']
    start.solve(initial_condition_set, workflows)

    print(roia)

    total = 0

    print(total)

    return total

assert get_part_two(test) == 1
print(f'Part 2: {get_part_two(data)}')

