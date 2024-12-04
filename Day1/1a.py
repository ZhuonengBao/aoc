import numpy as np


a = []
b = []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        a.append(num1)
        b.append(num2)

a.sort()
b.sort()
a_arr = np.array(a)
b_arr = np.array(b)

c_arr = np.abs(a_arr - b_arr)

print(sum(c_arr))

