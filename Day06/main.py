with open('input.txt', 'r') as f:
    data = f.read()



def get_part_one(signal):
    counter = 4
    while True:
        mark = set(signal[0:4])
        if len(mark) == 4:
            break
        else:
            signal = signal[1:]
            counter +=1
    
    return counter





assert get_part_one('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
assert get_part_one("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert get_part_one('nppdvjthqldpwncqszvftbrmjlhg') == 6
assert get_part_one('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert get_part_one('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
print(f'Part 1: {get_part_one(data)}')

# # part 2

def get_part_two(signal):
    counter = 14
    while True:
        mark = set(signal[0:14])
        if len(mark) == 14:
            break
        else:
            signal = signal[1:]
            counter +=1
    
    return counter


assert get_part_two('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
assert get_part_two("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
assert get_part_two('nppdvjthqldpwncqszvftbrmjlhg') == 23
assert get_part_two('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
assert get_part_two('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26
print(f'Part 2: {get_part_two(data)}')
