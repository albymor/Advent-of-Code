from z3 import *


with open('input.txt', 'r') as f:
    data = f.read()

test = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""   

import re
class Equation:
    def __init__(self):
        self.a = None
        self.b = None
        self.res = None

    def __repr__(self):
        return f"a*{self.a}+b*{self.b}={self.res}"

class System:
    def __init__(self):
        self.eq1 = None
        self.eq2 = None
    
    def __repr__(self):
        return f"{self.eq1}, {self.eq2}"

r_qe =r".*X\+(\d+), Y\+(\d+)"
r_res =r".*X=(\d+), Y=(\d+)"

def get_part_one(data, factor=0):
    lines = data.split('\n\n')

    systems = []

    for s in lines:
        eq1 = Equation()
        eq2 = Equation()
        sys = System()
        sys.eq1 = eq1
        sys.eq2 = eq2
        systems.append(sys)
        s = s.split("\n")
        match1 = re.findall(r_qe, s[0])
        match2 = re.findall(r_qe, s[1])
        match3 = re.findall(r_res, s[2])
        eq1.a = int(match1[0][0])
        eq1.b = int(match2[0][0])
        eq2.a = int(match1[0][1])
        eq2.b = int(match2[0][1])
        eq1.res = int(match3[0][0])
        eq2.res = int(match3[0][1])

    res = 0

    for sys in systems:

        # Declare the variables
        a = Int('a')
        b = Int('b')

        # Define the equations
        eq1 = a * sys.eq1.a + b * sys.eq1.b == (sys.eq1.res+factor)
        eq2 = a * sys.eq2.a + b * sys.eq2.b == (sys.eq2.res+factor)

        # Create a solver
        solver = Solver()

        # Add the equations to the solver
        solver.add(eq1, eq2)

        # Check for solutions
        if solver.check() == sat:
            # If a solution exists, get the model
            model = solver.model()
            res += (model[a].as_long()*3 + model[b].as_long())

    return res

assert get_part_one(test,0) == 480
print(f'Part 1: {get_part_one(data,0)}')



# part 2 
def get_part_two(data):
    return get_part_one(data, 10000000000000)

print(f'Part 2: {get_part_two(data)}')

