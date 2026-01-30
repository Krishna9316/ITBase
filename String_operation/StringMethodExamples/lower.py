# lower method example

# 1. email input validation

# email = input("Enter your email : ")
email = "ABCD@GMAIL.COM"

email = email.lower()
print("Your email is : ", email)


# 2. username input validation

# username = input("Enter your username : ")  
username = "KRIS2154"  

username = username.lower()
print("Your username is : ", username)

# 3. case insensitive comparison    
str1 = "Hello World"
str2 = "hello world"
if str1.lower() == str2.lower():
    print("Strings are equal")
else:
    print("Strings are not equal")
    
# 4. standardizing text for storage
text = "This is Some Sample TEXT."  
standardized_text = text.lower()
print("Standardized Text:", standardized_text)

# 5. search functionality
database = ["apple", "banana", "cherry", "date"]
search_query = "BANANA"
if search_query.lower() in database:
    print("Found")
else:
    print("Not Found")
    