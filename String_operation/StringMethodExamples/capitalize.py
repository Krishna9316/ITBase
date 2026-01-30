# Capitalize method example

# 1. used in paragraph and sentance submitting

# paragraph = input("Enter your paragraph: ")
paragraph = " this is a sample paragraph. it contains multiple sentences. each sentence should start with a capital letter."
sentences = paragraph.split('. ')
capitalized_sentences = [sentence.capitalize() for sentence in sentences]
capitalized_paragraph = '. '.join(capitalized_sentences)    
print("Capitalized Paragraph:", capitalized_paragraph)