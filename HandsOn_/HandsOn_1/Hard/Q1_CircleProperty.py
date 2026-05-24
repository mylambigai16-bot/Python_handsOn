radius=float(input('Enter the radius of thr circle: '))
angle=float(input("Enter the angle in degrees: "))
pi=3.14159
diameter=2*radius
circumference=2*pi*radius
area=pi*(radius*radius)
sector_area=(angle/360)*area
print("Radius: ",radius)
print("Diameter:",diameter)
print("Circiumference: ",circumference)
print(f"Sector Area for {angle} degrees: ",sector_area)
arc_length=(angle/360)*circumference
print(f"Arc Length for {angle} degrees: ",arc_length)
