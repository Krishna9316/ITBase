# Nested if else example

# 1. Grade Assignment
score = 85
if score >= 90:
    print("Score: {}, Grade: A")
elif score >= 80:
    print("Score: {}, Grade: B")
else:
    print("Score: {}, Grade: C")

# 2. Discount Coupon if purchase is above rs. 1000 discount 10% else if purchase is above rs. 500 discount 5% else no discount
purchase_amount = 750
if purchase_amount > 1000:
    print("Discount: 10%")
elif purchase_amount > 500:
    print("Discount: 5%")
else:
    print("Discount: No discount")
    
    
# 3. Traffic Light System
light_color = "Yellow"
if light_color == "Red":
    print("Stop")
elif light_color == "Yellow":
    print("Caution")
else:
    print("Go")
    
# 4. payment transaction 

# Variables for demonstration
entered_pin = 1234
saved_pin = 1234
transaction_amount = 500
current_balance = 1000

if entered_pin == saved_pin:
    print("PIN verified.")
    if transaction_amount <= current_balance:
        print("Payment successful!")
    else:
        print("Payment failed: Insufficient balance.")

else:
    print("Payment failed: Incorrect PIN.")

#5.  Temprature system

temperature = -25
if temperature > 40:
    print("It is Hotter")
else:
    if temperature >= 20:
        print("It is Cool")
    else:
        if temperature > 0:
            print("It is Cold")
        else:
            print("It is Freez")
            
# 6. Loan Eligibility
age = 30
income = 60000
if age >= 18:
    if income >= 50000:
        print("Eligible for loan")
    else:
        print("Not eligible for loan: Insufficient income")
else:
    print("Not eligible for loan: Underage")


# 7. Password Strength Checker
has_alphabet = True
has_number = True
has_special_char = True

if has_alphabet:
    if has_number:
        if has_special_char:
            print("Password is correct")
        else:
            print("Error: Invalid form (Missing special character)")
    else:
        print("Error: Invalid form (Missing number)")
else:
    print("Error: Invalid form (Missing alphabet)")
    
# 8. Age Restricted Validation
age = 20
has_valid_id = True

if age >= 18:
    if has_valid_id:
        print("Access Granted: Age and ID verified")
    else:
        print("Access Denied: Please provide a valid ID")
else:
    print("Access Denied: You must be at least 18 years old")
    
# 9. Job Application

has_degree = True
years_experience = 2

if has_degree == True:
    if years_experience >= 2:
        print("Applicant Accepted")
    else:
        print("Applicant Rejected: Requires at least 2 years of experience")
else:
    print("Applicant Rejected: Degree required")

# 10. Standard Addmission process if student is passed in 12th and has more than 75% marks then eligible for admission else not eligible for admission
passed_12th = True
marks_percentage = 80
if passed_12th:
    if marks_percentage > 75:
        print("Eligible for admission")
    else:
        print("Not eligible for admission: Marks below 75%")
else:
    print("Not eligible for admission: 12th grade not passed")

# 11. Charging Indicator system
battery = 55  
if battery < 20:
    print("Battery is Red")
else:
    if battery <= 40: 
        print("Battery is Orange")
    else:
        if battery <= 60: 
            print("Battery is Yellow")
        else:
            if battery <= 80: 
                print("Battery is Green")
            else: 
                print("Battery is Full")

# 12. check it is number if it is number then check it is Positiv, Negative and Zero (nutral)
number = -5

if number > 0:
    print("Number is Positive")
else:
    if number < 0:
        print("Number is Negative")
    else:
        print("Number is Zero")

# 13. Age Validation
        
age = 22

if age < 18:
    print("It is minor")
else:
    if age >= 18 and age <= 40:
        print("Young")
    else:
        print("Upper Older")
        
# 14. time base greeting 
hour = 14  # Example: 2 PM

if hour >= 1 and hour <= 11:
    print("Morning")
else:
    if hour >= 12 and hour <= 17:
        print("Afternoon")
    else:
        if hour >= 18 and hour <= 21:
            print("Evening")
        else:
            print("Night")


# 15. Salary Spending 

spending_percentage = 75  

if spending_percentage == 100:
    print("It is not good")
else:
    if spending_percentage >= 60 and spending_percentage <= 80:
        print("It is acceptable spending")
    else:
        print("Amount Saving")
        
# 16. Parking system
vehicle_type = "Bike"  
hours = 3             

if vehicle_type == "Car":
    print("Vehicle identified: Car")
    
    if hours <= 1:
        print("Parking Fee: 0")
    else:
        print("Parking Fee: 20 Rs. ")

else:
    if vehicle_type == "Bike":
        print("Vehicle identified: Bike")
        if hours <= 1:
            print("Parking fee : 0")
        else:
            print("Parking fee : 10 Rs.")
    else:
        print("Vehicle type unknown.")  

# 17. Student Science Commerce and arts addmission

percentage = 60
ScienceMarks = 85
BioMarks = 70
MathsMarks = 78

if percentage >= 80 and ScienceMarks >= 80 and MathsMarks >= 80:
    print("Qualified for Science Stream")
    if BioMarks >= 70:
        print("Specialization: Medical")
    else:
        if MathsMarks > 70:
            print("Specialization: Maths")
        else:
            print("Specialization: General Science")

else:
    if percentage >= 60:
        print("Qualified for Commerce Stream")
        if MathsMarks >= 70:
            print("Specialization: Commerce with Math")
        else:
            print("Specialization: Plain Commerce")
            
    else:
        if percentage >= 45:
            print("Qualified for Arts Stream")
        else:
            print("Admission Rejected: Percentage too low")
            
