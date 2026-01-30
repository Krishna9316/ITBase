# count method example

# 1. Used in feedback section for letter counting out of total letters

feedback = "Great product, really enjoyed using it!"
letter_count = feedback.count('e')  
print("Number of 'e' in feedback:", letter_count)

# 2. total writed Word counting in form

form_text = "I am very satisfied with the service provided."
word_count = form_text.count(' ') +1
print("Total words in form text:", word_count)

# 3. Value counting in survey responses
survey_responses = "Yes, No, Yes, Yes, No, Yes"
yes_count = survey_responses.count('Yes')
print("Number of 'Yes' responses:", yes_count)  

# 4. product counting in inventory list
inventory = "apple, banana, orange, apple, grape, apple"
apple_count = inventory.count('apple')  
print("Number of apples in inventory:", apple_count)

# 5. character frequency analysis
text = "Data analysis is crucial for decision making."
a_count = text.count('a')
print("Frequency of 'a' in text:", a_count)
