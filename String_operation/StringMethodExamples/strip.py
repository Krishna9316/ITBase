# strip method example

# 1. removing leading and trailing spaces from user input

# user_input = input("Enter your name with spaces: ")
user_input = "   Krishna Verma   "  
cleaned_input = user_input.strip()
print("Cleaned Name:", cleaned_input)


# 2. IN OTP input validation
# otp = input("Enter OTP: ")
otp = "  123456  "  
cleaned_otp = otp.strip()
print("Cleaned OTP:", cleaned_otp)

# 3. cleaning data from files
# file_data = input("Enter data from file: ")
file_data = "   Data from file   "
cleaned_file_data = file_data.strip()
print("Cleaned File Data:", cleaned_file_data)

# 4. URL cleaning
# url = input("Enter URL: ")
url = "   www.example.com   "
cleaned_url = url.strip()
print("Cleaned URL:", cleaned_url)

# 5. cleaning email input
# email = input("Enter your email: ")
email = "fdgxhj@gmail.com      "
cleaned_email = email.strip()
print("Cleaned Email:", cleaned_email)

