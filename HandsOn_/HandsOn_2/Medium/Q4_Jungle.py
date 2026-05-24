jungle = int(input())
r=int(input())
d=int(input())
b=int(input())
s=int(input())
lion=jungle-(r+d+b+s)
print(lion)
if(lion < 0):
    print(" Counted wrongly")
elif(lion==0):
    print(" Baby lion is well behaved ")
else:
    print(" Baby lion is mischievous")