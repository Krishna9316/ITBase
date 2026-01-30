# isalnum method example isalnum = is alphanumeric

# 1. User input validation for usernames
# username = input("Enter your username: ")
username = "User123"
if username.isalnum():
    print("Valid username")
else:  
    print("Invalid username: Only alphanumeric characters are allowed")


# 2. Product code validation
# product_code = input("Enter the product code: ")
product_code = "ABCD1234"
if product_code.isalnum():
    print("Valid product code")
else:
    print("Invalid product code: Only alphanumeric characters are allowed")
    
# 3. password validation
# password = input("Enter your password: ")
password = "Passw0rd!"
if password.isalnum():
    print("Valid password")
else:
    print("Invalid password: Only alphanumeric characters are allowed")
    
    
# 4. login ID validation
# login_id = input("Enter your login ID: ")
login_id = "LoginID2024"
if login_id.isalnum():
    print("Valid login ID")
else:
    print("Invalid login ID: Only alphanumeric characters are allowed")
    
# 5. Coupon code validation
# coupon_code = input("Enter your coupon code: ")
coupon_code = "SAVE20OFF"
if coupon_code.isalnum():
    print("Valid coupon code")
else:
    print("Invalid coupon code: Only alphanumeric characters are allowed")
    
