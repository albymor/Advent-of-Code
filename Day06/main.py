with open('input.txt', 'r') as f:
    data = f.read()

    
def get_result(signal, window_length):

    for i in range(len(signal)-window_length):
        if len(set(signal[i:i+window_length])) == window_length:
            break
    return i+window_length


assert get_result('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4) == 7
assert get_result("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
assert get_result('nppdvjthqldpwncqszvftbrmjlhg', 4) == 6
assert get_result('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4) == 10
assert get_result('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4) == 11
print(f'Part 1: {get_result(data, 4)}')

# part 2


assert get_result('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
assert get_result("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
assert get_result('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
assert get_result('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
assert get_result('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26
print(f'Part 2: {get_result(data,14)}')
