
def first_example():
    name = input("Enter your first name: ")
    reversed_name = ""

    for i in range(len(name), 0, -1):
        reversed_name += name[i-1]

def second_example():
    name = input("Enter your first name: ")
    reversed_name = name[::-1]
    print(reversed_name)

second_example()