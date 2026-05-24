num=int(input("Enter the number: "))
n=num
digits=len(str(num)) 
sum_of_powers = 0

while n>0:
    digit= n%10
    sum_of_powers += digit**digits
    n //= 10

if sum_of_powers == num:
    print("true")
else:
    print("false")
