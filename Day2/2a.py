import numpy as np


def is_safe(report):
    monotonic = all(np.diff(report) <= 0) or all(np.diff(report) >= 0)
    differences_valid = all(np.abs(np.diff(report)) >= 1) and all(np.abs(np.diff(report)) <= 3)

    return monotonic and differences_valid


safe = 0

with open("input.txt", "r") as file:
    for line in file:
        report = np.array(list(map(int, line.split())))
        
        if is_safe(report):	
            safe += 1


print(safe)
