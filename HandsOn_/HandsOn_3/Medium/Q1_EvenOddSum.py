num = int(input("Enter the number: "))
odd_sum,even_sum=0,0
for i in range(1,num+1):
    if(i%2 == 0):
        even_sum += i
    else:
        odd_sum += i
print("Even sum : ",even_sum,"\nOdd sum : ",odd_sum)