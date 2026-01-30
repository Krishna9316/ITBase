# replace method example

# 1. used in form  to edit data

# data = input("Enter your data with wrong word: ")
data = "This car's owner is Raj."
corrected_data = data.replace("Raj", "Krishna")
print("corrected_data: ", corrected_data)

# 2. change the formattion of phone number

phoneNumber = "123-456-7890"
ChangedPhoneNumber = phoneNumber.replace("-", "")
print("Changed Phone Number : ", ChangedPhoneNumber)

# 3. MAsking Information of Mobile Number or Aadhar Number Last Digits

MobileNumber = "9876543210"
MaskedNumber = MobileNumber.replace(MobileNumber[6:], "XXXX")
print("Masked Mobile Number : ", MaskedNumber) 

AadharNumber = "9999 8888 7777 "
MaskedAadharNumber = AadharNumber.replace(AadharNumber[9: ], " XXXX")
print("Masked Mobile Number : ", MaskedAadharNumber) 

# 4.
