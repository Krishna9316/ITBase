# isnumeric method example

# 1. for number input validation
age = "30"
zip_code = "560001"
if age.isnumeric():
    print(f"Valid age: {age}")
else:
    print(f"Invalid age: {age}")
if zip_code.isnumeric():
    print(f"Valid zip code: {zip_code}")
else:
    print(f"Invalid zip code: {zip_code}")
    
# 2. contact number validation in user registration form
contact_number = "9876543210"
if contact_number.isnumeric():
    print(f"Valid contact number: {contact_number}")
else:
    print(f"Invalid contact number: {contact_number}")
    
# 3. String validation for numeric content
mixed_string = "Room 101"
numeric_part = ''.join(filter(str.isnumeric, mixed_string))
print(f"Numeric part extracted: {numeric_part}")

