import re
str1 = input("Enter text")
pat = r"[!@#$%^&*,#]"
s = re.sub(pat,"#",str1)
print(s)