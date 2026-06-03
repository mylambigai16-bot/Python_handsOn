def prime(start,end):
    for i in range(start,end+1):
        for j in range(2,i):
            if(i % j == 0):
                break;
        else:
            print(i,end=' ')

start = int(input("Enter range starts from: "))
end = int(input("ENter range ends from: "))
prime(start, end)