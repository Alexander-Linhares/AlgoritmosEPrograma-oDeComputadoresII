odd = 0
pair = 0

while (number := int(input("Type an integer number or type zero to quit: "))) != 0:
    if number % 2 == 0:
        pair += 1
    else:
        odd += 1

print("The program has been ended.")
print(f"The number of pair numbers is: {pair}")
print(f"The number of odd numbers is: {odd}")