def newsalary(oldsalary,hike):
    new_salary=oldsalary + (oldsalary*hike/100)
    return new_salary

old_salary = int(input('Enter old salary per month: '))
hike = int(input("Enter hike: "))
print(newsalary(old_salary,hike))