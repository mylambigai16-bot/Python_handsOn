s1 = "Abc"
s2 = "Xyz"
s3 = ""

len1 = len(s1)
len2 = len(s2)

for i in range(max(len1, len2)):
    if i < len1:  
        s3 += s1[i]
    if i < len2:  
        s3 += s2[-(i+1)]

print("Result:", s3)
