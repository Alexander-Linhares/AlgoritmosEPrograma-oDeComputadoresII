import numpy as np

x = np.zeros(5)

for i in range(len(x)):
    x[i] = float(input(f"Insert a value at {i} position: "))

print("the summation result is: ")
print(x.sum())
