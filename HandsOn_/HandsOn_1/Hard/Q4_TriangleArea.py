import math
a = int(input("Enter first side:"))
b = int(input("Enter second side:"))
c=int(input("Enter third side:"))
if (a + b > c) and (a + c > b) and (b + c > a):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of the Triangle:",area)
else:
    print("Not a valid side!")
