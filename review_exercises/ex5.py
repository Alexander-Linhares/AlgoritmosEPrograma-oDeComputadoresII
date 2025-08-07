number = int(input("Type an integer number to see the sum of the each number into the interval sequence: "))
total_sum = 0

for i in range(1, number):
    print(f"adding: {i} + {total_sum}")
    total_sum += i

print(f"Final result: {total_sum}")