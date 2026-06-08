import re

def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$'
    res = re.findall(email_pattern, email)
    return res    

def validate_phone(phone):
    phone_pattern = r'^[6-9]{1}+[0-9]{9}'
    res = re.match(phone_pattern, phone)
    return res

def validate_usn(username):
    username_pattern = r'^[25MCA]+[\d]{3}'
    res = re.match(username_pattern, username)
    return res
    
email = "user@domain.ext"
res = validate_email(email)
if(res):
    print("Matched!")
else:
    print("Not  match!")

phone = "6932581470"
res = validate_phone(phone)
if(res):
    print("Matched!")
else:
    print("Not  match!")

usn = "25MCA007"
res = validate_usn(usn)
if(res):
    print("Matched!")
else:
    print("Not  match!")
