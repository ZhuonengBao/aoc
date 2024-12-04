import numpy as np


a = []
b = []

with open("input.txt", "r") as file:
    for line in file:
        num1, num2 = map(int, line.split())
        a.append(num1)
        b.append(num2)


print(sum([b.count(a[i]) * a[i] for i in range(len(a))]))

