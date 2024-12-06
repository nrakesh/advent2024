import numpy as np


def process(file_path):
    sum = 0
    with open(file_path, 'r') as f:
        for line in f:
            row = np.fromstring(line, dtype=int, sep=' ')
            if is_safe(row):
                sum += 1
                print(row, "-----------Safe")
            else:
                print(row, "-----------Not Safe")
    print(sum)




# get the difference
# check if there is one direction change
#  all < 0
#  all >= 0
#

#   -- change can be find one -ve
#
def is_safe(row):
    diff = np.diff(row)
    if np.all(diff < 1):
        # check then cound of number less than -3
        # if the count is 1 .. remove the item from the row and calcualte diff again
        count = ((diff < -3) | (diff == 0)).sum()
        if count > 1:
            return False
        elif count == 1:
            # remove the index from row
            index = np.where((diff < -3) | (diff == 0))[0]
            return check(row, index)
        else:
            return safe(np.diff(row))

    elif np.all(diff > -1):
        count = ((diff > 3) | (diff == 0)).sum()
        if count > 1:
            return False
        elif count == 1:
            # remove the index from row
            index = np.where((diff > 3) | (diff == 0))[0]
            return check(row, index)
        else:
            return safe(np.diff(row))

    else: #combination of +ve, 0 and -ve
        positive_count = (diff > -1).sum()
        negative_count = (diff < 0).sum()
        if positive_count == 1:
            index = np.where(diff > -1)[0]
            return check(row,index)
        elif negative_count == 1:
            index = np.where(diff < 0)[0]
            return check(row,index)
        else:
            return False


def check(row, index):
    row1 = np.delete(row, index )
    row2 = np.delete(row, index + 1)
    row3 = np.delete(row, index - 1)
    return safe(np.diff(row1)) or safe(np.diff(row2)) or safe(np.diff(row3))





def safe(diff):
    if np.all(diff > 0) or np.all(diff < 0):
        diff = np.abs(diff)
        if np.all(diff < 4):
            return True
    return False


process("../day6/2024-2-input.txt")
#process("test.txt")
