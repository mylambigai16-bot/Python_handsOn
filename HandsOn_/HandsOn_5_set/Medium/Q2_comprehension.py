def set_comprehension(n):
    return {i**2 for i in range(1, n+1)}

n = int(input("Enter input: "))
print(set_comprehension(n))  
 