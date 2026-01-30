# integer
# Float
# Complaex
# Boolean  
# Set
# 




# Typecasting of String

String_input = input("Enter a string: ")

print("String value is :",String_input)
print("Datatype is :",type(String_input))
print(" ")


# ------------------------------------------------------------------------------------------------------

# Converting String to Integer

integer_convert = String_input
# Converted_integer = sum(ord(char) for char in integer_convert)
# print("Integer value is :",Converted_integer)
# print("Datatype is :",type(Converted_integer))  
# print(" ")

if String_input.isdigit():
    Converted_integer = int(String_input)
else:
    Converted_integer = sum(ord(char) for char in String_input)

print(f"Integer value is: {Converted_integer}")
print(f"Datatype is: {type(Converted_integer)}")


# ------------------------------------------------------------------------------------------------  


# Converting String to Float

float_convert = String_input
# Converted_float = sum(ord(char) for char in float_convert)
# print("Float value is :",float(Converted_float)) 
# print("Datatype is :",type(float(Converted_float)))
# print(" ")

if String_input.isdigit():
    Converted_integer = float(String_input)
else:
    Converted_integer = sum(ord(char) for char in String_input)

print(f"Integer value is: {float(Converted_integer)}")
print(f"Datatype is: {type(Converted_integer)}")


# Converting String to Complex

# Complex_convert = String_input
# Converted_complex = sum(ord(char) for char in Complex_convert)
# print("Complex value is :", complex(Converted_complex)) 
# print("Datatype is :",type(complex(Converted_complex)))
# print(" ")

if String_input.isdigit():
    Complex_convert = complex(String_input)
else:
    Complex_convert = sum(ord(char) for char in String_input)

print(f"Integer value is: {complex(Complex_convert)}")
print(f"Datatype is: {type(Complex_convert)}")



# -------------------------------------------------------------------------------------------

# Converting String to Boolean


# Converting String to Boolean with specific check
# if String_input.lower() in ['false', '0', '']:
#     Converted_Boolean = False
# else:
#     Converted_Boolean = True

# print("Boolean value is :",Converted_Boolean)
# print("Datatype is :",type(Converted_Boolean))
# print(" ")  

if String_input.isdigit():
    num = float(String_input)
    Converted_Boolean = bool(num)
else:
    Converted_Boolean = bool(String_input)
print(f"Boolean value is: {Converted_Boolean}")
print(f"Datatype is: {type(Converted_Boolean)}")

# -------------------------------------------------------------------------------------------

# convertion strign into set
Set_convert = String_input
Converted_set = set(Set_convert)    
print("Set value is :",Converted_set)
print("Datatype is :",type(Converted_set))
print(" ")  




# Converting string into range
Range_convert = String_input
Converted_range = len(Range_convert)    
print("Range value is :",range(Converted_range))
print("Datatype is :",type(range(Converted_range)))
