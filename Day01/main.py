with open('input.txt') as f:
    data = f.readlines()

elfs = []

s = 0
for d in data:
    d = d.strip()
    if len(d) == 0:
        elfs.append(s)
        s = 0
        continue
    s += int(d)

elfs.append(s)

elfs.sort()


print(f'Part 1: {elfs[-1]}')

#part 2

top3 = elfs[-3:]
print(f'Part 1: {sum(top3)}')