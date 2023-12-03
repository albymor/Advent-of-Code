import re


with open('input.txt', 'r') as f:
    data = f.read()

test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


test2 = "..............................314../......692.214.718.............762*461.....844*.....&.............973.675...80.................*143......"



def get_part_one(data):
    lines = data.split('\n')

    res = []

    for i, line in enumerate(lines):
        # find all symbols in the current line

        r = re.compile("[^0-9.]")
        m = r.finditer(line)

        symbols_pos = [match.start() for match in m]

        if len(symbols_pos) >= 0:
            # find numbers in the current line
            r = re.compile("[0-9]+")
            m = r.finditer(line)

            for match in m:
                # if the number is between two symbols, add it to the result
                for pos in symbols_pos:
                    if match.start()-1 == pos:
                        res.append(int(match.group()))
                    
                    if match.end() == pos:
                        res.append(int(match.group()))


            # if possible, check for match in the previous line
            if i > 0:
                r = re.compile("[0-9]+")
                m = r.finditer(lines[i-1])

                for match in m:
                    # if the number is between two symbols, add it to the result
                    span = range(match.start()-1, match.end()+1)
                    for pos in symbols_pos:
                        if pos in span:
                            res.append(int(match.group()))


            # if possible, check for match in the next line
            if i < len(lines)-1:
                r = re.compile("[0-9]+")
                m = r.finditer(lines[i+1])

                for match in m:
                    # if the number is between two symbols, add it to the result
                    span = range(match.start()-1, match.end()+1)
                    for pos in symbols_pos:
                        if pos in span:
                            res.append(int(match.group()))




        pass

    res = sum(res)
    return res

assert get_part_one(test) == 4361

assert get_part_one(test2) == 762+461+844+143

print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    res = {}

    def add_to_dict(d, key, value):
        if key in d:
            d[key].append(value)
        else:
            d[key] = [value]

    for i, line in enumerate(lines):
        # find all symbols in the current line

        r = re.compile("\*")
        m = r.finditer(line)

        symbols_pos = [match.start() for match in m]

        if len(symbols_pos) >= 0:
            # find numbers in the current line
            r = re.compile("[0-9]+")
            m = r.finditer(line)

            for match in m:
                # if the number is between two symbols, add it to the result
                for pos in symbols_pos:
                    if match.start()-1 == pos:
                        add_to_dict(res, (pos, i), int(match.group()))
                    
                    if match.end() == pos:
                        add_to_dict(res, (pos, i), int(match.group()))


            # if possible, check for match in the previous line
            if i > 0:
                r = re.compile("[0-9]+")
                m = r.finditer(lines[i-1])

                for match in m:
                    # if the number is between two symbols, add it to the result
                    span = range(match.start()-1, match.end()+1)
                    for pos in symbols_pos:
                        if pos in span:
                            add_to_dict(res, (pos, i), int(match.group()))


            # if possible, check for match in the next line
            if i < len(lines)-1:
                r = re.compile("[0-9]+")
                m = r.finditer(lines[i+1])

                for match in m:
                    # if the number is between two symbols, add it to the result
                    span = range(match.start()-1, match.end()+1)
                    for pos in symbols_pos:
                        if pos in span:
                            add_to_dict(res, (pos, i), int(match.group()))




        pass


    total = 0

    for key, value in res.items():
        if len(value) == 2:
            total += (value[0] * value[1])
        elif len(value) > 2:
            raise Exception('More than 2 values for a key')
        else:
            pass
    return total

assert get_part_two(test) == 467835
print(f'Part 2: {get_part_two(data)}')

