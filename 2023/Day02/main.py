import re


with open('input.txt', 'r') as f:
    data = f.read()

test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""" 

max_cubes = {'red':12 , 'green': 13, 'blue':14}

def get_part_one(data):
    lines = data.split('\n')

    total = 0

    for line in lines:

        a = line.split(':')
        game = int(a[0].split()[1])

        turns = a[1].split(';')


        def is_valid(turns):

            for turn in turns:
                b = turn.split(',')
                for cube in b:
                    cube = cube.strip().split()
                    if int(cube[0]) > max_cubes[cube[1]]:
                        return False
            
            return True
        
        if is_valid(turns):
            total += game 


    return total

assert get_part_one(test) == 8

print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    total = 0


    for line in lines:

        local_max = {'red':0 , 'green': 0, 'blue':0}
        a = line.split(':')

        turns = a[1].split(';')

        for turn in turns:
            b = turn.split(',')
            for cube in b:
                gino = cube.strip().split()
                if int(gino[0]) > local_max[gino[1]]:
                    local_max[gino[1]] = int(gino[0])

        pr = 1
        for key in local_max:
            if local_max[key] == 0:
                raise Exception('no max', local_max)
            pr *= local_max[key]

        total += pr 


    return total

assert get_part_two(test) == 2286
print(f'Part 2: {get_part_two(data)}')

