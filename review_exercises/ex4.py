number = int(input("Type an integer number to see your odds: "))

for i in range(number):
    (i % 2 != 0) and print(i)