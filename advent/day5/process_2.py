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
            is_ok = False
            ctr = 0
            while not is_ok:
                is_ok = main_check(pages)
                ctr += 1
            if ctr > 1:
                sum += pages[len(pages) // 2]
    print("-----SUM=", sum)

def main_check(pages):
    is_ok = True
    for i in range(len(pages)):
        is_ok, bad = check(pages, i)
        if is_ok:
            continue
        else:
            temp = pages[i]
            pages[i] = pages[bad]
            pages[bad] = temp
            break
    return is_ok


def check(pages, n):
    global rules
    rule = rules.get(pages[n])
    if rule is None:
        return True, 0
    else:
        for i in range(len(pages)):
            if i == n:
                continue
            if i < n:  # if any number matches in the rule then its not valid
                if pages[i] in rule:
                    return False, i
    return True, 0


f = "test1.txt"
f1 = "2024-5-input.txt"

ff = "test2.txt"
ff1 = "2024-5-input2.txt"

process(f1, ff1)
