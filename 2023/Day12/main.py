import re
from tqdm import tqdm
from collections import deque
with open('input.txt', 'r') as f:
    data = f.read()

test = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""   

def get_part_one(data):
    lines = data.split('\n')

    


    admissible = 0

    for line in tqdm(lines):
        pattern, comb = line.split()
        comb =  tuple(map(int, comb.split(',')))
        #comb = tuple(sorted(comb))
        q = deque()
        q.append(pattern)

        while q:
            scheme = q.popleft()
            if '?' in scheme:
                q.append(scheme.replace('?','#',1))
                q.append(scheme.replace('?','.',1))
            else:
                r = re.compile(r'#+')
                m = r.finditer(scheme)
                if m:
                    this_comb = tuple([match.span()[1] -match.span()[0] for match in m])
                    if this_comb == comb:
                        admissible += 1


    print(admissible)

    

    return admissible

assert get_part_one(test) == 21
#print(f'Part 1: {get_part_one(data)}')



# part 2 
def get_part_two(data):
    lines = data.split('\n')

    admissible = 0

    for line in tqdm(lines):
        pattern, comb = line.split()
        combs =  [comb for _ in range(5)]
        comb = ','.join(combs)
        comb =  tuple(map(int, comb.split(',')))
        #comb = tuple(sorted(comb))

        patts = [pattern for _ in range(5)]

        #  ???.###????.###????.###????.###????.###
        #  ???.###????.###????.###????.###????.###

        pattern = '?'.join(patts)

        q = deque()
        q.append(pattern)

        def check(patt, comb):
            is_ok = True
            num = 0
            in_p = False
            comb_index = 0
            for c in patt:
                if c == '.':
                    if in_p:
                        if comb_index < len(comb) and num == comb[comb_index]:
                            comb_index += 1
                            num = 0
                            in_p = False
                            is_ok = True
                        else:
                            return False
                    in_p = False
                    continue
                elif c == '#':
                    in_p = True
                    num+=1
                elif c == '?':
                    return True

            return is_ok




        while q:
            scheme = q.popleft()
            if '?' in scheme:
                a = check(scheme.replace('?','#',1), comb)
                if a:
                    q.append(scheme.replace('?','#',1))
                
                a = check(scheme.replace('?','.',1), comb)
                if a:
                    q.append(scheme.replace('?','.',1))
            else:
                r = re.compile(r'#+')
                m = r.finditer(scheme)
                if m:
                    this_comb = tuple([match.span()[1] -match.span()[0] for match in m])
                    if this_comb == comb:
                        admissible += 1


    print(admissible)

    

    return admissible

assert get_part_two(test) == 525152
print(f'Part 2: {get_part_two(data)}')

