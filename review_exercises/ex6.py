start = int(input("Type a number to start: "))
stop = int(input("Type a nubmer to end: "))
k = 3
total = 0
sum_string = ""

for i in range(start, stop):
    print(i)
    if i % k == 0:
        sum_string += f"{i} + " if stop > i else f" {i} = "
        total += i

print(sum_string)