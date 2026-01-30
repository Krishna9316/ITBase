String_input = input("Enter a string: ")



# Converting String to Boolean
if String_input.isdigit():
    num = float(String_input)
    Converted_Boolean = bool(num)
else:
    Converted_Boolean = bool(String_input)
print(f"Boolean value is: {Converted_Boolean}")
print(f"Datatype is: {type(Converted_Boolean)}")    