# casefold method exmample

# 1. for search engine optimization (SEO)
text = "Python is Awesome"
search_term = "python"
if search_term in text.casefold():
    print(f"Search term '{search_term}' found in text.")
else:
    print(f"Search term '{search_term}' not found in text.")
    

# 2. user validation  from email input
email_input = "xyz@gmail.com"
valid_email = "xyz@gmail.com"
if email_input.casefold() == valid_email.casefold():
    print("Email is valid.")
else:
    print("Email is invalid.")  
    