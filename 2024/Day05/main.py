with open('input.txt', 'r') as f:
    data = f.read()

test = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""" 


def check(rule,page, fix=False):
    try:
        a = page.index(rule[0])
        b = page.index(rule[1])
    except ValueError:
        # print("[+] Rule don't apply")
        return (page, True)
    
    if a<=b:
        return (page, True)
    else:
        if fix:
            tmp = page[a]
            page[a] = page[b]
            page[b] = tmp

        return (page,False)
    

def checker(rules, page, fix=False):

    if not fix:
        for r in rules:
            if not check(r, page)[1]:
                return (page,False)
        
        return (page, True)
    else:
        fixed = False
        while not fixed:
            for r in rules:
                page, ok = check(r, page, fix=True)
                if not ok:
                    break
            else:
                return (page, True)

def get_part_one(data):
    rules, pages = data.split('\n\n')
    res = 0

    rules = [list(map(int, x.split("|"))) for x in rules.split('\n')]
    pages = [list(map(int, x.split(","))) for x in pages.split('\n')]

    for page in pages:

        if checker(rules, page)[1]:
            res += page[len(page)//2]  

    return res

assert get_part_one(test) == 143
print(f'Part 1: {get_part_one(data)}')


# part 2 
def get_part_two(data):
    rules, pages = data.split('\n\n')
    res = 0

    rules = [list(map(int, x.split("|"))) for x in rules.split('\n')]
    pages = [list(map(int, x.split(","))) for x in pages.split('\n')]

    for page in pages:
        if not checker(rules, page)[1]:
                p, r = checker(rules, page, fix=True)

                res += p[len(p)//2]   




    return res

assert get_part_two(test) == 123
print(f'Part 2: {get_part_two(data)}')

