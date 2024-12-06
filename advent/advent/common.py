import numpy as np


def read_input(filename, delimiter=None, np_array=False):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            lines = [line.rstrip('\n') for line in lines]
            if delimiter:
                # Split each line using the provided delimiter
                lines = [line.split(delimiter) for line in lines]

            if np_array:
                return np.array(lines)
            else:
                return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


def read_input_as_char_array(filename):
    lines = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                lines.append(list(line.rstrip('\n')))
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
