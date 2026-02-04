final_list = []

list_type = input("Which list do you want? (1D or 2D or 3D): ")

if list_type == "2D" or "2d":
    num_sublists = 2
elif list_type == "3D" or "3d":
    num_sublists = 3
else:
    print("1D" or "1d")
    num_sublists = 1

for list_idx in range(1, num_sublists + 1):
    temp_list = []
    num_elements = int(input(f"\nHow many elements for List {list_idx}? "))
    
    for element_idx in range(1, num_elements + 1):
        value = input(f"  Enter value {element_idx}: ")
        temp_list.append(value)  
    
    final_list.append(temp_list)

# print("\n--- Your Result ---")
print(final_list)





# =====================================================================================================================================

finalList = []

listValue = int(input("How many Major list you want in your Final list : "))
# 2d Dynamic value list
for majorList in range(listValue):
    print(f"\nCreate Major List {majorList + 1}:")
    
    tempMajorList = []
    
    majorListInput = int(input(f"  How many minor lists want in Major List {majorList+ 1}? : "))
    
    for element in range(majorListInput):
        elementValue = input(f"      Enter value for Element {element+1}: ")
        tempMajorList.append(elementValue)
            
    finalList.append(tempMajorList)
    
    
# 1d  dynamic value list
    

for element in range(listValue):
    elementValue = input(f"      Enter value for Element {element+1}: ")
    finalList.append(elementValue)




print(finalList)
    
    
