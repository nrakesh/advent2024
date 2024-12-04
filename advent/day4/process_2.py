import numpy as np

max_rows = 0
max_cols = 0
data = []


def process(file_path):
    global data
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            arr = np.array(list(line))
            data.append(arr)
    #print(data)
    global max_rows, max_cols
    max_rows = len(data)
    max_cols = max(len(row) for row in data)
    #print(max_rows, ", ", max_cols)

    count = 0
    for i in range(max_rows):
        for j in range(max_cols):
            ch = data[i][j]
            if ch == 'M':
                # M.S
                # .A.
                # M.S
                if chk(i, j + 2, 'S') and chk(i + 1, j + 1, 'A') and chk(i + 2, j, 'M') and chk(i + 2, j + 2, 'S'):
                    count += 1

                # S.M
                # .A.
                # S.M
                if chk(i, j - 2, 'S') and chk(i + 1, j - 1, 'A') and chk(i + 2, j - 2, 'S') and chk(i + 2, j, 'M'):
                    count += 1

                # S.S
                # .A.
                # M.M
                if chk(i, j + 2, 'M') and chk(i - 1, j + 1, 'A') and chk(i - 2, j, 'S') and chk(i - 2, j + 2, 'S'):
                    count += 1

                # M.M
                # .A.
                # S.S
                if chk(i, j + 2, 'M') and chk(i + 1, j + 1, 'A') and chk(i + 2, j, 'S') and chk(i + 2, j + 2, 'S'):
                    count += 1

    print("count=", count)

    # across


def chk(i, j, ch):
    if i >= max_rows or j >= max_cols or i < 0 or j < 0:
        return False
    if data[i][j] == ch:
        return True
    return False


f = "test.txt"
f1 = "2024-4-input.txt"

process(f1)
