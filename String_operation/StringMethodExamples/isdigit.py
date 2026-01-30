# isdigit method example

# 1. Validationg age number and zip code input 
age = "25"
zip_code = "12345"
if age.isdigit():
    print(f"Valid age: {age}")
else:
    print(f"Invalid age: {age}")
if zip_code.isdigit():
    print(f"Valid zip code: {zip_code}")
else:
    print(f"Invalid zip code: {zip_code}")
    
# 2. number validation in user registration form
phone_number = "5551234567"
if phone_number.isdigit():
    print(f"Valid phone number: {phone_number}")
else:
    print(f"Invalid phone number: {phone_number}")

# 3. Extracting numeric values from a mixed string
mixed_string = "+91-9876543210"
numeric_part = ''.join(filter(str.isdigit, mixed_string))
print(f"Numeric part extracted: {numeric_part}")


