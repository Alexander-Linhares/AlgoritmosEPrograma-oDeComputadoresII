import numpy as np

x = np.zeros(5)

for i in range(len(x)):
    x[i] = float(input(f"Type a value at {i+1} position of the vector: "))

print(x.mean())