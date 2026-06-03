print("Enter two number: ")
m=int(input())
n=int(input())
for i in range(m,n+1):
    if(i%5 == 0 and i%10==0):
        print('dong',end=' ')
    elif(i%5 == 0):
        print('ding',end=' ')
    else:
        print(i,end=' ')