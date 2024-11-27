from collections import OrderedDict

with open('input.txt', 'r') as f:
    data = f.read()

test = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

def hash(string):
    current_value = 0
    for c in string:
        if c == '\n':
            print('new line')
            continue
        current_value = ((current_value+ord(c))*17)%256
    return current_value

def get_part_one(data):
    assert hash("HASH") == 52

    tokens = data.split(',')
    total = 0
    for t in tokens:
        total += hash(t)

    return total


assert get_part_one(test) == 1320
print(f'Part 1: {get_part_one(data)}')


# it can be done without this class and only using an ordered dictionary
# Ii didn't work (for another stupid bug not related to the order of the dictionary) so i made this class...
class Box():
    def __init__(self) -> None:
        self.labels = []
        self.focals = []

    def remove(self, label):
        if label in self.labels:
            index = self.labels.index(label)

            self.labels.pop(index)
            self.focals.pop(index)

    def insert(self, label, focal):
        if label in self.labels:
            index = self.labels.index(label)
            self.focals[index] = focal
        else:
            self.labels.append(label)
            self.focals.append(focal)

    def has(self, label):
        if label in self.labels:
            index = self.labels.index(label)
            return True
        else:
            return False
        
    def values(self):
        return self.focals
        

    def __repr__(self) -> str:
        c = zip(self.labels, self.focals)
        return ','.join([f'{k}-->{v}' for k,v in c])


# part 2 
def get_part_two(data):
    tokens= data.split(',')

    boxes = OrderedDict()
    
    for c in tokens:
        if '=' in c:
            m = c.split('=')
            box_idx = hash(m[0])
            focal = m[1]
            if box_idx in boxes:
                pass
            else:
                boxes[box_idx] = Box()

            if boxes[box_idx].has(m[0]):
                pass
            
            boxes[box_idx].insert(*m)
        
        elif '-' in c:
            m = c.split('-')
            box_idx = hash(m[0])
            if box_idx in boxes:
                boxes[box_idx].remove(m[0]) 
        else:
            print('no op')
            assert False

    total = 0
    for k,v in boxes.items():
        factor = k+1

        for i, vv in enumerate(v.values()): 
            total+= (factor*(i+1)*int(vv))

    return total

assert get_part_two(test) == 145
print(f'Part 2: {get_part_two(data)}')

