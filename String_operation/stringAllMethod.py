# PYTHON STRING METHODS

# 1. capitalize()
s1 = "python programming"
print(s1.capitalize())      # Output: Python programming



# 2. casefold()
s2 = "PYTHON"
print(s2.casefold())        # Output: python



# 3. center()
s3 = "python"
print(s3.center(10, "*"))   # Output: **python**



# 4. count()
s4 = "banana"
print(s4.count("a"))    # Output: 3



# 5. encode()
s5 = "python"
print(s5.encode())      # Output: b'python'


         
# 6. endswith()
s6 = "python.py"
print(s6.endswith(".py"))   # Output: True



# 8. find()
s8 = "python"
print(s8.find("t"))     # Output: 2



# 9. format()
s9 = "My name is {}"
print(s9.format("Krishna"))     # Output: My name is Krishna



# 10. format_map()
s10 = "My age is {age}"
print(s10.format_map({"age": 21}))   # Output: My age is 21


# 11. index()
s11 = "python"
print(s11.index("h"))   # Output: 3



# 12. isalnum()
s12 = "python123"
print(s12.isalnum())        # Output: True



# 13. isalpha()
s13 = "python"
print(s13.isalpha())        # Output: True



# 15. isdecimal()
s15 = "123"
print(s15.isdecimal())      # Output: True



# 16. isdigit()
s16 = "123"
print(s16.isdigit())        # Output: True



# 17. isidentifier()
s17 = "var_name"
print(s17.isidentifier())   # Output: True



# 18. islower()
s18 = "python"
print(s18.islower())        # Output: True



# 19. isnumeric()
s19 = "123"
print(s19.isnumeric())      # Output: True


# 21. isspace()
s21 = "   "
print(s21.isspace())        # Output: True



# 22. istitle()
s22 = "Python Programming"
print(s22.istitle())        # Output: True



# 23. isupper()
s23 = "PYTHON"
print(s23.isupper())        # Output: True



# 24. join()
s24 = "-"
print(s24.join(["p", "y", "t", "h", "o", "n"]))     # Output: p-y-t-h-o-n



# 25. ljust()
s25 = "python"
print(s25.ljust(10, "*"))       # Output: python****



# 26. lower()
s26 = "PYTHON"
print(s26.lower())         # Output: python


# 29. partition()
s29 = "python-programming"
print(s29.partition("-"))       # Output: ('python', '-', 'programming')



# 30. replace()
s30 = "python"
print(s30.replace("p", "P"))    # Output: Python



# 31. rfind()
s31 = "banana"
print(s31.rfind("a"))            # Output: 5



# 32. rindex()
s32 = "banana"
print(s32.rindex("a"))          # Output: 5



# 33. rjust()
s33 = "python"
print(s33.rjust(10, "*"))        # Output: ****python



# 34. rpartition()
s34 = "python-programming"
print(s34.rpartition("-"))      # Output: ('python', '-', 'programming')



# 35. rsplit()
s35 = "python is easy"
print(s35.rsplit())             # Output: ['python', 'is', 'easy']


# 36. rstrip()
s36 = "python   "
print(s36.rstrip())             # Output: python



# 37. split()
s37 = "python is fun"
print(s37.split())              # Output: ['python', 'is', 'fun']



# 38. splitlines()
s38 = "python\njava"
print(s38.splitlines())         # Output: ['python', 'java']



# 39. startswith()
s39 = "python.py"
print(s39.startswith("py"))     # Output: True



# 40. strip()
s40 = "  python  "
print(s40.strip())             # Output: python



# 41. swapcase()
s41 = "PyThOn"
print(s41.swapcase())           # Output: pYtHoN



# 42. title()
s42 = "python programming"
print(s42.title())          # Output: Python Programming


# 43. upper()
s43 = "python"
print(s43.upper())          # Output: PYTHON



# 44. zfill()
s44 = "123"
print(s44.zfill(5))        # Output: 00123
