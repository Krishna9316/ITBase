# Upper method example


# 1. example Input validation

# firstName = input("Input First Name : ")
# lastName = input("Input Last Name : ")

firstName = "Krishna"
lastName = "Verma"

name = firstName + " " + lastName
Fullname = name.upper()

print(Fullname)

# 2. value identyfier (PAN Card, PASSPORT)

# pan = input("Enter pan number : " )
# passport = input("Enter passport number : " )

pan = "abscd1234d"
passport = "n1234567"

EditedPAN = pan.upper()
EditedPass = passport.upper()

print("Pan Number : ", EditedPAN, "Passport Number : ", EditedPass)


# 3. database keyword searching

database = ["KRISHNA VERMA", "AJAY KUMAR", "VIKAS SINGH", "RAVI SHARMA"]
search = "krishna verma" 
search = search.upper()
if search in database:
    print("Found")
else:
    print("Not Found")  
    
    
# 4. For generation uppercase String like some Activation code

Code = "ab12cd34ef56"
ActivationCode = Code.upper()
print("Activation Code : ", ActivationCode)

# 5. standardizing text for comparison
text1 = "Hello World"
text2 = "hello world"
if text1.upper() == text2.upper():
    print("Texts are equal")
else:
    print("Texts are not equal")    