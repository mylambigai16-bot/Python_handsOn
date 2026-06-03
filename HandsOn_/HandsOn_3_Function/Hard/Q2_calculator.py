def add(m,k):
    return m+k
def subtract(m,k):
    return m-k
def multiple(m,k):
    return m*k

operator = input("Enter operation to perform: ")
operand1 = int(input("Enter the first operand: "))
operand2 = int(input("Enter the second operand: "))
if( operator == '+'):
    addition = add(operand1,operand2)
    print(addition)
elif( operator == '-'):
    subtraction = subtract(operand1,operand2)
    print(subtraction)
elif( operator == '*'):
    multiplication = multiple(operand1,operand2)
    print(multiplication)
else:
    print("Invalid!")