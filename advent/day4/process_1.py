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
            if ch == 'X':
                # Across Forward:  i,j+1 = M , i,j+2 = A, i,j+3 = S
                if chk(i, j + 1, 'M') and chk(i, j + 2, 'A') and chk(i, j + 3, 'S'):
                    count += 1
                # Across Backward: i,j-1 = M , i,j-2 = A, i,j-3 = S
                if chk(i, j - 1, 'M') and chk(i, j - 2, 'A') and chk(i, j - 3, 'S'):
                    count += 1

                # Down: i+1,j = M, i+2,j = A, i+3,j = S
                if chk(i + 1, j, 'M') and chk(i + 2, j, 'A') and chk(i + 3, j, 'S'):
                    count += 1

                # Up: i-1,j = M, i-2,j = A, i-3,j = S
                if chk(i - 1, j, 'M') and chk(i - 2, j, 'A') and chk(i - 3, j, 'S'):
                    count += 1

                # Diag up-right: i-1,j+1 = M, i-2,j+2 = A, i-3,j+3 = S
                if chk(i - 1, j + 1, 'M') and chk(i - 2, j + 2, 'A') and chk(i - 3, j + 3, 'S'):
                    count += 1

                # Diag up-left: i-1,j-1 = M, i-2,j-2 = A, i-3,j-3 = S
                if chk(i - 1, j - 1, 'M') and chk(i - 2, j - 2, 'A') and chk(i - 3, j - 3, 'S'):
                    count += 1

                # Diag down-right: i+1,j+1 = M, i+2,j+2 = A, i+3,j+3 = S
                if chk(i + 1, j + 1, 'M') and chk(i + 2, j + 2, 'A') and chk(i + 3, j + 3, 'S'):
                    count += 1

                # Diag down-left: i+1,j-1 = M, i+2,j-2 = A, i+3,j-3 = S
                if chk(i + 1, j - 1, 'M') and chk(i + 2, j - 2, 'A') and chk(i + 3, j - 3, 'S'):
                    count += 1
    print("count=" , count)


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
