# isupper method examples

# 1. password validation
# password = input("Enter your password: ")
password = "PASSWORD123"
if password.isupper():
    print("Valid password")
else:
    print("Invalid password")
    
# 2. data case changing like PAN  or VOter ID if any person enter in lower case it should be converted in upper case automatically
# id_input = input("Enter your PAN or Voter ID: ")
id_input = "abcde1234f"
id_converted = id_input.upper()
print(f"ID converted to uppercase: {id_converted}")

# 3.captcha verification
# captcha_input = input("Enter the captcha: ")
captcha_input = "X7Y8Z9"
if captcha_input.isupper():
    print("Captcha verified")
else:
    print("Captcha verification failed")
    
# 4. id and username validation
# username = input("Enter your username: ")
username = "USER2024"
if username.isupper():
    print("Valid username")
else:
    print("Invalid username")
    
    


