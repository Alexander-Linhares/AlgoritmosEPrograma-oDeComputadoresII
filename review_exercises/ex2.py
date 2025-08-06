from decimal import Decimal

#About salary
better_salary = 0
salary_sum = 0
salary_average = 0

#About dependents
children_average = 0
children_count = 0

#About fagility situation 
min_salary_average_people = 0
min_salary_counter = 0

#Number of people
register_count = 0

while (inp := input("Insert a new person register[s/n]: ").lower() == 's' ):
    #inputs
    salary = Decimal(input("Enter how much she receives: "))
    number_of_dependents = int(input("Enter how many children she has: "))

    #Count processing
    salary_sum += salary
    better_salary = salary if salary > better_salary else better_salary
    min_salary_counter += 1 if salary <= 1570 else 0
    children_count += number_of_dependents if number_of_dependents != 0 else 0
    register_count += 1
else:
    #Getting average processing
    salary_average = Decimal(round((salary_sum/register_count), 2))
    children_average = round((children_count/register_count), 2)
    min_salary_average_people = round((min_salary_counter/register_count)*100, 2)

print("Program Ended".center(50, "-"))

print(f"Salary average: {salary_average}")
print(f"Children average: {children_average}")
print(f"Minimun salary average people percentual: {min_salary_average_people}%")


