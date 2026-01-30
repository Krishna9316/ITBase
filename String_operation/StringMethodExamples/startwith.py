# startwith method example  

# 1. for specific value input validation like country code 
# country_code = input("Enter your country code: ")
country_code = "+91"
if country_code.startswith("+9"):
    print("Valid country code")
else:
    print("Invalid country code: Country code should start with '+'")
    

# 2. specific searching
# filename = input("Enter the filename: ")
filename = "report.pdf"
if filename.startswith("report"):
    print("File found")
else:
    print("File not found")
    
# 3. URL validation
# url = input("Enter the URL: ")
url = "https://www.example.com"
if url.startswith("https://"):
    print("Secure URL")
else:
    print("Insecure URL")
    
# 4. Email validation ( email cannot start with special characters  )
# email = input("Enter your email address: ")
email = "xyz@gmail.com"
if email.startswith(("!", "#", "$", "%", "&", "*")):
    print("Invalid email address: Email cannot start with special characters")
else:
    print("Valid email address")
    

