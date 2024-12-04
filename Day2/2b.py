import numpy as np


def is_safe(report):
    monotonic = all(np.diff(report) <= 0) or all(np.diff(report) >= 0)
    differences_valid = all(np.abs(np.diff(report)) >= 1) and all(np.abs(np.diff(report)) <= 3)

    return monotonic and differences_valid


def problem_dampener(report):
    for i in range(len(report)):
        new_report = np.delete(report, i)

        if is_safe(new_report):
            return True

    return False


safe = 0

with open("input.txt", "r") as file:
    for line in file:
        report = np.array(list(map(int, line.split())))
        
        if is_safe(report) or problem_dampener(report):
            safe += 1

print(safe)
