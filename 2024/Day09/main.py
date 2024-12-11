with open('input.txt', 'r') as f:
    data = f.read()

test = """2333133121414131402"""   

class Loc:
    def __init__(self, id, free):
        self.id = id
        self.free = free

    def __repr__(self):
        if self.free:
            return '.'
        else:
            return str(self.id)

class Disk:
    def __init__(self):
        self.locations = []


    def add(self, location):
        self.locations.append(location)


    def __repr__(self):
        r = ""
        for l in self.locations:
            if l.free:
                r += '.'
            else:
                r += str(l.id)

        return r
    

    def defrag(self):
        free_i = 0
        file_i = len(self.locations)-1

        while free_i < file_i:
            # search free loc
            while not self.locations[free_i].free:
                free_i +=1

            # find file
            while self.locations[file_i].free:
                file_i -=1
            
            if free_i < file_i:
            # swap
                tmp = self.locations[free_i]
                self.locations[free_i] = self.locations[file_i]
                self.locations[file_i] = tmp

            else:
                break


def get_part_one(data):
    data = list(data.strip())

    disk = Disk()

    id = 0
    for i, d in enumerate(data):
        if i % 2 == 0:
            for _ in range(int(d)):
                disk.add(Loc(id, False))
            id += 1
        else:
            for _ in range(int(d)):
                disk.add(Loc(None, True))

    disk.defrag()

    res = 0

    for i, l in enumerate(disk.locations):
        if not l.free:
            res += (int(l.id)*i)

    return res

assert get_part_one(test) == 1928
print(f'Part 1: {get_part_one(data)}')

class Loc2:
    def __init__(self, id, free, len):
        self.id = id
        self.free = free
        self.len = len

    def __repr__(self):
        if self.free:
            return '.'*self.len
        else:
            return str(self.id)*self.len

class Disk2:
    def __init__(self):
        self.locations = []


    def add(self, location):
        self.locations.append(location)


    def __repr__(self):
        r = ""
        for l in self.locations:
            r += str(l)

        return r
    

    def defrag(self):
        file_i = len(self.locations)-1
        

        while file_i>0:
            # search free loc
            free_i = 0


                # find file
            while self.locations[file_i].free:
                file_i -=1

            while True:

                while not self.locations[free_i].free:
                    free_i +=1               
                
                if free_i < file_i:

                    free, file = self.locations[free_i], self.locations[file_i]

                    if free.len >= file.len:
                        diff = free.len - file.len
                        if diff == 0:
                            free.id = file.id
                            free.free = False
                            file.id = None
                            file.free = True
                        else:
                            free.id = file.id
                            free.free = False
                            free.len = file.len
                            self.locations.insert(free_i+1,Loc2(None, True, diff)) 
                            file.id = None
                            file.free = True
                        break
                    else:
                        free_i +=1   

                else:
                    file_i -=1
                    break

# part 2 
def get_part_two(data):
    data = list(data.strip())

    disk = Disk2()

    res = 0
    id = 0
    for i, d in enumerate(data):
        if i % 2 == 0:
            disk.add(Loc2(id, False, int(d)))
            id += 1
        else:
            disk.add(Loc2(None, True, int(d)))

    disk.defrag()

    pos = 0
    for i, l in enumerate(disk.locations):
        if not l.free:
            for _ in range(l.len):
                res += (pos*int(l.id))
                pos += 1
        else:
            pos += l.len

    return res

assert get_part_two(test) == 2858
print(f'Part 2: {get_part_two(data)}')

