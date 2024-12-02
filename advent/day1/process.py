import numpy as np


def process(file_path="input1.txt"):
    try:
        data = np.loadtxt(file_path, dtype=int)  # Load data into NumPy array
        data = np.sort(data, axis=0)  # Sort along the columns
        print(np.shape(data))
        print(data[:, 0])
        compare(data)
        similarity(data)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading the file: {e}")


def compare(arr):
    diff = np.abs(arr[:, 0] - arr[:, 1])
    print(np.sum(diff))


def similarity(arr):
    unique, counts = np.unique(arr[:, 1], return_counts=True)
    count_dict = dict(zip(unique, counts))

    sum = 0
    for num in arr[:, 0]:
        occurrences = count_dict.get(num, 0)
        sum += num * occurrences
    print(sum)


process()
