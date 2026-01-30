# endswith method examples

# 1. email validation
# email = input("Enter your email address: ")
email = "krishna@gmail.com"
if email.endswith(".com"):  
    print("Valid email address")
else:
    print("Invalid email address")
    
# 2. url validation
# url = input("Enter website URL: ")
url = "www.krishna.org"
if url.endswith(".org"):
    print("Valid organization URL")
else:
    print("Invalid organization URL")
    
# 3. Card type identification
# card_number = input("Enter your card number: ")
card_number = "1234-5678-9012-3456"
if card_number.endswith("3457"):
    print("This is a valid card ending with 3456")
else:
    print("This card does not end with 3456")
    
# 4. File type checking
# file_name = input("Enter the file name: ")
file_name = "document.docx"
if file_name.endswith(".pdf"):
    print("This is a PDF file")
elif file_name.endswith(".docx"):
    print("This is a Word document")
elif file_name.endswith(".txt"):
    print("This is a text file")
else:
    print("This is not a PDF file")
    

    

    
    