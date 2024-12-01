# input = [int(l)*811589153 for l in open("text.txt")]

# buffer = [(idx, i) for idx, i in enumerate(input)]



# print_buffer(buffer)

# for idx, i in enumerate(input):
#     old_idx = buffer.index((idx, i))

#     buffer.remove((idx, i))
#     buffer.insert((old_idx + i + len(input) - 1) %
#                     (len(input) - 1), (-1, i))
#     print_buffer(buffer)

# zero_idx = buffer.index((-1, 0))

# print(sum(buffer[(zero_idx + (i+1) * 1000) % len(buffer)][1]
#         for i in range(3)))



def print_buffer(buffer):
    print(" ".join(str(i[1]) for i in buffer))


input = [int(l) * 811589153 for l in open("text.txt")]

buffer = [(idx, i) for idx, i in enumerate(input)]
print_buffer(buffer)

for _ in range(10):
    for idx, i in enumerate(input):
        old_idx = buffer.index((idx, i))

        buffer.remove((idx, i))
        buffer.insert((old_idx + i + len(input) - 1) %
                        (len(input) - 1), (idx, i))

        print_buffer(buffer)

zero_idx = buffer.index((input.index(0), 0))
print(sum(buffer[(zero_idx + (i+1) * 1000) % len(buffer)][1]
        for i in range(3)))