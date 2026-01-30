#  isspace method example

# 1. for login validation
# username = input("Enter your username: ")
username = "nc "
if not username.isspace() and username != "":
    print("Valid username")
else:
    print("Invalid username: Username cannot be empty or whitespace only")
    
    
# 2. word counting
text = "Hello World  "
space_count = 0
for char in text:
    if char.isspace():
        space_count += 1 
print(f"Number of characters in the text: {space_count}")


