s = input("Enter string: ")

lower_count = 0
upper_count = 0
non_letter_count = 0

for ch in s:
    if ch.islower():
        lower_count += 1
    elif ch.isupper():
        upper_count += 1
    else:
        non_letter_count += 1

print("Lower case letters:", lower_count)
print("Upper case letters:", upper_count)
print("Non-letters:", non_letter_count)
