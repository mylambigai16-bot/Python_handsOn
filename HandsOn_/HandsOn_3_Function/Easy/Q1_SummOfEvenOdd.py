def sumOf(n):
    even_sum,odd_sum=0,0
    for i in range(1,n+1):
        if(i % 2 == 0):
            even_sum+=i
        else:
            odd_sum+=i
    print(f"Even sum: {even_sum}\nOdd sum: {odd_sum}")

num = int(input("Enter the number: "))
sumOf(num)
