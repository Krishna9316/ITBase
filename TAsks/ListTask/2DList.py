# two D List 

List1 = []
List2 = []

finalList = []

ListType = input("Which list you want 2D or 3D : ")


L1 = int(input("How many elements you want in list1 : "))
for i in range(L1):
    
    value = input(f"Enter value  {i +1} :")
    List1.append(value)

L2 = int(input("How many elements you want in list2 : "))
for i in range(L2):
    value = input(f"Enter value  {i +1} :")
    List2.append(value)
    
if ListType == "2D" or "2d":
    finalList.append(List1)
    finalList.append(List2)
    
    # print(finalList)
else:
    pass

print(finalList)