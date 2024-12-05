import numpy as np

rules = {}


def process(file_path, file_path2):
    global rules
    sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            left, right = line.split('|')
            left = int(left)
            right = int(right)
            if left in rules:
                rules[left].append(right)
            else:
                rules[left] = [right]
    # read the page numbers to update
    with open(file_path2, 'r') as file:
        for line in file:
            pages = [int(x) for x in line.split(',')]
            is_ok = True
            for i in range(len(pages)):
                is_ok = check(pages, i)
                if is_ok:
                    continue
                else:
                    break
            if is_ok:
                sum += pages[len(pages) // 2]

    print("-----SUM=", sum)


def check(pages, n):
    global rules
    #if not in rules ok
    nv = pages[n]
    rule = rules.get(nv)
    if rule is None:
        return True
    else:
        for i in range(len(pages)):
            if i == n:
                continue
            if i < n:  # if any number matches in the rule then its not valid
                if pages[i] in rule:
                    return False
    return True


f = "test1.txt"
f1 = "2024-5-input.txt"

ff = "test2.txt"
ff1 = "2024-5-input2.txt"

process(f, ff)
