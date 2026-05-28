str1 = input("Enter string: ")
str2 = input("Enter string to find: ")

index1 = str1.rfind(str2)
print(f"Last occurrence of {str2} starts at index: ",index1)