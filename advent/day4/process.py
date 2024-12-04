import numpy as np


def chk(data,max_rows, max_cols,i, j, ch):
    if i >= max_rows or j >= max_cols or i < 0 or j < 0:
        return False
    if data[i][j] == ch:
        return True
    return False

def process(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            arr = np.array(list(line))
            data.append(arr)
    print(data)

    max_rows = len(data)
    max_cols = max(len(row) for row in data)
    print(max_rows, ", ", max_cols)

    count = 0
    for i in range(max_rows):
        for j in range(max_cols):
            ch = data[i][j]
            if ch == 'X':
                # Across Forward:  i,j+1 = M , i,j+2 = A, i,j+3 = S
                if chk(data,max_rows, max_cols,i, j + 1, 'M') and chk(data,max_rows, max_cols,i, j + 2, 'A') and chk(data,max_rows, max_cols,i, j + 3, 'S'):
                    count += 1
                # Across Backward: i,j-1 = M , i,j-2 = A, i,j-3 = S
                if chk(data,max_rows, max_cols,i, j - 1, 'M') and chk(data,max_rows, max_cols,i, j - 2, 'A') and chk(data,max_rows, max_cols,i, j - 3, 'S'):
                    count += 1

                # Down: i+1,j = M, i+2,j = A, i+3,j = S
                if chk(data,max_rows, max_cols,i + 1, j, 'M') and chk(data,max_rows, max_cols,i + 2, j, 'A') and chk(data,max_rows, max_cols,i + 3, j, 'S'):
                    count += 1

                # Up: i-1,j = M, i-2,j = A, i-3,j = S
                if chk(data,max_rows, max_cols,i - 1, j, 'M') and chk(data,max_rows, max_cols,i - 2, j, 'A') and chk(data,max_rows, max_cols,i - 3, j, 'S'):
                    count += 1

                # Diag up-right: i-1,j+1 = M, i-2,j+2 = A, i-3,j+3 = S
                if chk(data,max_rows, max_cols,i - 1, j + 1, 'M') and chk(data,max_rows, max_cols,i - 2, j + 2, 'A') and chk(data,max_rows, max_cols,i - 3, j + 3, 'S'):
                    count += 1

                # Diag up-left: i-1,j-1 = M, i-2,j-2 = A, i-3,j-3 = S
                if chk(data,max_rows, max_cols,i - 1, j - 1, 'M') and chk(data,max_rows, max_cols,i - 2, j - 2, 'A') and chk(data,max_rows, max_cols,i - 3, j - 3, 'S'):
                    count += 1

                # Diag down-right: i+1,j+1 = M, i+2,j+2 = A, i+3,j+3 = S
                if chk(data,max_rows, max_cols,i + 1, j + 1, 'M') and chk(data,max_rows, max_cols,i + 2, j + 2, 'A') and chk(data,max_rows, max_cols,i + 3, j + 3, 'S'):
                    count += 1

                # Diag down-left: i+1,j-1 = M, i+2,j-2 = A, i+3,j-3 = S
                if chk(data,max_rows, max_cols,i + 1, j - 1, 'M') and chk(data,max_rows, max_cols,i + 2, j - 2, 'A') and chk(data,max_rows, max_cols,i + 3, j - 3, 'S'):
                    count += 1
    print("count=" , count)


            # across






f = "test.txt"
f1 = "2024-4-input.txt"

process(f1)
