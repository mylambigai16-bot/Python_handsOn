code = int(input("Enter the code: "))
if(code == 1):
    num1 = float(input("Enter float number1: "))
    num2 = float(input("Enter float number2: "))
    print("Sum : ",num1+num2)
elif(code == 2):
    num1 = int(input("Enter integer number1: "))
    num2 = int(input("Enter integer number2: "))
    print("Product : ",num1*num2)
else:
    s1 = str(input("Enter two string: "))
    s2 = str(input("Enter two string: "))
    print("Concatenation : ",s1+s2)