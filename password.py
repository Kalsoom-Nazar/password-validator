# Tum ek freelance developer ho, client ne bola:
# "Ek system banao jo check kare ke entered password strong hai ya weak."

# Rules for strong password:

# Kam se kam 8 characters ka ho

# Kam se kam 1 uppercase letter ho

# Kam se kam 1 lowercase letter ho

# Kam se kam 1 number ho

# Tumhara task:
# Python me ek program likho jo user ka password le aur bole:
# Strong Password ya Weak Password.
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
              



 