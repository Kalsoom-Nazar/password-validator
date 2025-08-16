password=input("Enter your Password here ")
has_upper=False
has_lower=False
has_digit=False
for char in password:
    if char.isupper():
        has_upper=True
    if char.islower():
        has_lower=True
    if char.isdigit():
        has_digit=True

if len(password)>=8 and has_digit and has_lower and has_upper:
    print("Password id strong")
else:
    print("Password is weak")   
              




 
