import numpy as np 

x = np.random.uniform(0, 100, size=[30])

print(f"The greatest value index is: {x.argmax()},\nand the lowest value index is: {x.argmin()}")