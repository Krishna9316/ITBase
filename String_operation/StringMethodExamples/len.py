# len method Exmaples

# 1. validating specific name string length
name = "Krishna"
name_length = len(name)
print("Length of the name:", name_length)

# 2. Username and password length check validation
username = "kris12"
password = "pass@4"
if len(username) <= 6 and len(password) <= 6:
    print("Username and password length are valid.")
else:
    print("Username or password length is invalid.")
    
# 3. Contact number and zip code length validation
contact_number = "1234567890"
zip_code = "560001"
if len(contact_number) == 10:
    print("Contact number length are valid.")
else:
    print("Contact number length is invalid.")
    
if len(zip_code) == 6:
    print("zip code length are valid.")
else:
    print("zip code length is invalid.")
    
# 4. used in ecommerce cart to count items
cart_items = ["laptop", "mouse", "keyboard", "monitor"]
item_count = len(cart_items)
print("Number of items in the cart:", item_count)

# 5. Alert massage for exceeding character limit in text area
text_area_input = "This is a sample input text. s a sample input text."
max_length = 50
if len(text_area_input) > max_length:
    print("Alert: You have exceeded the character limit!")
else:
    print("Input is within the character limit.")
    