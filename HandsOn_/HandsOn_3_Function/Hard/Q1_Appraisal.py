def level1(salary):
    incre_salary = salary + salary * (10/100)
    return incre_salary

def level2(salary):
    incre_salary = salary + salary * (25/100)
    return incre_salary

def level3(salary):
     incre_salary = salary + salary * (30/100)
     return incre_salary

salary = int(input("Enter salary: "))
appraisal_range = float(input("Enter appraisal  rating: "))
if(appraisal_range >= 1 and appraisal_range <=4):
    print(level1(salary))
elif(appraisal_range >=4.1 and appraisal_range <=7):
    print(level2(salary))
elif(appraisal_range >= 7.1 and appraisal_range <= 10):
    print(level3(salary))
else:
    print("Invalid  input!")
