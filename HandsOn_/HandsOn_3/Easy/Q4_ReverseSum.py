num=int(input("Enter the number: "))
sum=0
for i in range (num,0,-1):
    print(i,end=' ')
    sum+=i
print(sum)