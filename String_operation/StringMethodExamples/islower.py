#  islower method example

# 1. email validation
# email = input("Enter your email address: ")
email = "Xyz@gmail.com"
if email.islower():  
    print("Valid email address")
else:
    print("Invalid email address: Email should be in lowercase")
    
# 2. username validation
# username = input("Enter your username: ")
username = "userName123"
if username.islower():
    print("Valid username")
else:
    print("Invalid username")

# 3. Captcha verification
# captcha_input = input("Enter the captcha: ")
captcha_input = "a1b2c3"
if captcha_input.islower():
    print("Captcha verified")
else:
    print("Captcha verification failed")

# 4. link validation
# link = input("Enter the link: ")
link = "www.example.COM/page"
if link.islower():
    print("Valid link")
else:
    print("Invalid link")

