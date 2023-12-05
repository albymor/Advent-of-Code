import re


with open('input.txt', 'r') as f:
    data = f.read()

test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


def num_to_next(num, maps):
    for _map in maps:
        if num >= _map[1] and num <= (_map[1] +_map[2] -1):
            pos = num - _map[1]
            return _map[0]+pos
    return num



def get_part_one(data):
    lines = data.split('\n')

    seeds = list(map(int,lines[0].split(': ')[1].split(' ')))
    maps = lines[2:]


    map_num = 0
    map_dict ={}

    for m in maps:
        if 'map' in m:
            map_num += 1
            map_dict[map_num] = []
        elif len (m) > 0:
            map_dict[map_num].append(list(map(int,m.split(' '))))


    min_loc = -1

    for s in seeds:
        loc = s
        for m in map_dict:
            loc = num_to_next(loc, map_dict[m])
        if min_loc == -1 or loc < min_loc:
            min_loc = loc



    return min_loc

assert get_part_one(test) == 35
print(f'Part 1: {get_part_one(data)}')




def check(s, map_dict, step=1000000):
    min_loc = -1
    i = 0
    while i < s[1]:
        loc = s[0]+i
        start = loc
        for m in map_dict:
            loc = num_to_next(loc, map_dict[m])
        if min_loc == -1 or loc < min_loc:
            min_loc = loc
            # [[seed start, seed length], location we got for the seed, global min location, seed from what we started]
            min_data = [s,loc,min_loc,start]

        i += step
    return min_data


# part 2 
def get_part_two(data, step):
    lines = data.split('\n')

    # get the seeds
    seeds = list(map(int,lines[0].split(': ')[1].split(' ')))

    # reparese the seeds into pairs (start, length)
    scan = 1
    new_seeds = []
    while scan < len(seeds):
        new_seeds.append([seeds[scan-1],seeds[scan]])
        scan += 2

    seeds = new_seeds

    #get the maps
    maps = lines[2:]

    map_num = 0
    map_dict ={}

    for m in maps:
        if 'map' in m:
            map_num += 1
            map_dict[map_num] = []
        elif len (m) > 0:
            map_dict[map_num].append(list(map(int,m.split(' '))))


    min_data = None

    for s in seeds:

        # for each seed, check the range of values. 
        # with the step size, we can skip over large ranges of values instead of checking each one
        # so we can approximately find the position of the min value
        data = check(s, map_dict, step=step)
        if min_data == None or data[2] < min_data[2]:
            min_data = data



    # now that we have the approximate location of the min value, we can check the range around it
    data = check([min_data[3]-(step//2), step//2], map_dict, step=1)    
    

    return data[2]

assert get_part_two(test, 5) == 46
print(f'Part 2: {get_part_two(data, 1000000)}')

