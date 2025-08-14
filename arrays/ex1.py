import numpy

x = numpy.zeros(10)


for i in range(len(x)):
    x[i] = i#float(input(f"Type any amount at {i} position: "))

print("Here are the inserted values: ")
for i in x:
    print(f"{i}", end="\n")