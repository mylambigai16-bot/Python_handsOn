total_price=0
while True:
    price=int(input("Enter the price of the first item:"))
    quantity=int(input("Enter the quantity of the item:"))
    total_price=total_price+(price*quantity)
    option=input("Do you want to enter anothr item?(Yes/No):")
    if(option == 'no'):
        break
print("Total quantity:",total_price)
