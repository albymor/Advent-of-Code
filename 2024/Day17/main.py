with open("input.txt", "r") as f:
    data = f.read()

test = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""


class CPU:
    def __init__(self, A, B, C, program):
        self.A = A
        self.B = B
        self.C = C
        self.IP = 0
        self.program = list(zip(program[::2], program[1::2]))
        self.out = []
        self.op_log = []

    def execute(self):
        if self.IP >= len(self.program):
            return False

        op, val = self.program[self.IP]
        skip_ip = False

        combo = None
        comb_repr = ''

        match val:
            case 0 | 1 | 2 | 3:
                combo = val
                comb_repr = str(val)
            case 4:
                combo = self.A
                comb_repr = 'A'
            case 5:
                combo = self.B
                comb_repr = 'B'
            case 6:
                combo = self.C
                comb_repr = 'C'
            case 7:
                pass
                #raise ValueError("INVALID OPERAND")
            case _:
                raise ValueError("UNKNOWN OPERAND")

        match op:
            case 0:
                self.A = self.A // 2**combo
                self.op_log.append("A=A//2**"+comb_repr)
            case 1:
                self.B = self.B ^ val
                self.op_log.append("B=B^"+str(val))
            case 2:
                self.B = combo % 8
                self.op_log.append(f"B={comb_repr}%8")
            case 3:
                if self.A == 0:
                    pass
                else:
                    self.IP = val
                    skip_ip = True
                    self.op_log.append(f"IP={val} if A!=0")
            case 4:
                self.B = self.B ^ self.C
                self.op_log.append("B=B^C")
            case 5:
                self.out.append(combo % 8)
                self.op_log.append(f"out={comb_repr}%8")
            case 6:
                self.B = self.A // 2**combo
                self.op_log.append("B=A//2**"+comb_repr)
            case 7:
                self.C = self.A // 2**combo
                self.op_log.append("C=A//2**"+comb_repr)
            case _:
                raise ValueError("INVALID OP")

        if not skip_ip:
            self.IP += 1

        return True


def get_part_one(data):
    regs, prog = data.split("\n\n")

    regs = regs.split("\n")
    A = int(regs[0].split(":")[1])
    B = int(regs[1].split(":")[1])
    C = int(regs[2].split(":")[1])

    prog = list(map(int,prog.split(":")[1].split(",")))

    cpu = CPU(A, B, C, prog)

    running = True
    while running:
        running = cpu.execute()

    res = ','.join(list(map(str,cpu.out)))

    print(cpu.op_log)

    return res 


assert get_part_one(test) == '4,6,3,5,6,3,5,2,1,0'
print(f"Part 1: {get_part_one(data)}")

test2 = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""


# part 2
def get_part_two(data):
    # looking at the op log what the program does is repeat these operations 
    # 'B=A%8', 'B=B^7', 'C=A//2**B', 'A=A//2**3', 'B=B^C', 'B=B^7', 'out=B%8'
    # we see that, at some point, the value of A is shifted right by 3 bits and the rest of the operations works only on the first 3 bits of A
    # the equation is this one ((((A%8)^7)^(A//2**((A%8)^7)))^7) % 8 or (((b^7)^(A//2**(b^7)))^7) % 8 with b = A%8 i.e. the first 3 bits of A
    # so since A is shifted, the last value of the program depends only on the first 3 bits of A and b = A. So we can build A in reverse 3 bits at a time

    def program(current_A, prog):
        if len(prog) == 0: return current_A
        target = prog[-1]
        for i in range(0,8):
            B = 0
            C = 0
            A = (current_A << 3) + i
            B=A%8
            B=B^7
            C=A//2**B
            #A=A//2**3
            B=B^C
            B=B^7
            out=B%8

            if out == target:
                sub = program(A,prog[:-1])
                if sub is None: continue
                return sub
        
    expected = [2,4,1,7,7,5,0,3,4,0,1,7,5,5,3,0]
    A = 0
    A = program(A,expected)
    return A


#get_part_two(test2) 
print(f"Part 2: {get_part_two(data)}")
