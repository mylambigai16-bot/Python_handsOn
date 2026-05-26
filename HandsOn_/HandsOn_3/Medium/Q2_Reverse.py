num = int(input("Enter the number: "))
c=0
n=num

print(len(str(num)))
while n!=0:
    n//=10
    c+=1
if(c == 5):
    rev = int(str(num)[::-1])
    print("Reversed number:", rev)
else:
    print("Not a valid number")