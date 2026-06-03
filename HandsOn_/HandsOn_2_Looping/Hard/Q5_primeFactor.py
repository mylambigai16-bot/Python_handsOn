num = int(input("Enter the number: "))
i = 2
while num > 1:
    if num % i == 0:
        print(i, end=" ")
        num //= i
    else:
        i += 1
