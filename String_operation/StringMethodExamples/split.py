# Split method Exmaples

# 1. Driving Licence Father's Name Input only Take First Letters
Name = "Krishna "
FatherName = "Mansingh"
Surname = "Verma"
FatherInitials = FatherName.split()
print("Drivers Fullname is : ", Name + FatherInitials[0][0] +" " + Surname)
 
 
#  2. Word Counting in a Sentence
sentence = "This is a sample sentence for word counting"
words = sentence.split()
word_count = len(words)
print("word Count : ", word_count)

# 3. Data Sepration
data = "Krishna,Verma,25,Engineer,India"
separated_data = data.split(",")
print("Separated Data: ", separated_data)


# 4. URL Extration
url = "https://www.krishnaverma.com/profile"
parts = url.split("/")
print("Protocol is :", parts[0])
print("Domain: ", parts[2])
print("Page is : ", parts[3])

# 5. multiline text splitting
multiline_text = """Hello World,This is a sample multiline text.It contains multiple lines.Have a great day!"""

parts = multiline_text.split(".")
print("Splited parts are of Paragraph : ", parts)
