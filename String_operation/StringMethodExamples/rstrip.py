# rstrip method example

# 1. data editing for database entry

# data = input("Enter data with trailing spaces: ")
data = "Krishna Verma     "
cleaned_data = data.rstrip()   
print("Cleaned Data:", cleaned_data)


# 2.url sorting/ cleaning
# url = input("Enter URL with trailing spaces: ")
url = "www.example.com/page    "
cleaned_url = url.rstrip()
print("Cleaned URl :", cleaned_url)

#3. Input Validation
# comment = input("Enter your comment: ")
comment = "This is a great product!     "
cleaned_comment = comment.rstrip()
print("Cleaned Comment:", cleaned_comment)


#4. log file processing
# log_entry = input("Enter log entry: ")
log_entry = "ERROR: Invalid user input     "
cleaned_log_entry = log_entry.rstrip()  
print("Cleaned Log Entry:", cleaned_log_entry)

# 5. 