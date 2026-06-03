age=int(input("Enter the age: "))
if(age<=0):
    print("Invalid age")
elif(age>0 and age<=10):
    print("Cartoon club")
elif(age>=10 and age<=20):
    print("Teens club")
else:
    print("Not Allowed")