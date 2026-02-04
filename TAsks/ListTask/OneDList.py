# 1D List Task

list = []   
element = int(input("How many elements you want in list : "))

for i in range(element):
    value = input(f"Enter value  {i +1} :")
    list.append(value)
    
print("The Created List is : ",list)