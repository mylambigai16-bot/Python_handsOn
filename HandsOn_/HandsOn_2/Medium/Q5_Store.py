name=input("Customer name: ")
item=int(input("Items they are buying: "))
if(item < 10):
    print(name,item*12)
elif(item >= 10 and item <= 99):
    print(name, item*10)
else:
    print(name, item*7)
