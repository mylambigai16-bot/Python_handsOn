s = input("Enter input: ").split()
print(s)
for i in s:
    if not(i.isalpha and i.isnumeric):
        print(i)