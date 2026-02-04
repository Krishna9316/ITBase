finalList = []

LitsTypeFromUser = input("Which type of list you want 1D, 2D or 3D : ")




if LitsTypeFromUser in ["3D" , "3d"] :
    listValue = int(input("How many Major list (3d) you want in your Final list : "))

    for majorList in range(listValue):
        print(f"\nCreate Major List {majorList + 1}:")
        
        tempMajorList = []
        
        majorListInput = int(input(f"  How many minor lists want in Major List {majorList+ 1}? : "))
        
        for minorList in range(majorListInput):
            tempMinorList = []
            elementsMinorList = int(input(f"    How many elements want for Minor list {minorList + 1}? : "))
            
            for element in range(elementsMinorList):
                elementValue = input(f"      Enter value for Element {element+1}: ")
                tempMinorList.append(elementValue)
            
            tempMajorList.append(tempMinorList)
        
        finalList.append(tempMajorList)
    
elif LitsTypeFromUser in ["2D" ,"2d" ]:
    listValue1 = int(input("How many Minor list (2d) you want in your Final list : "))
    for majorList in range(listValue1):
        print(f"\nCreate Minor List {majorList + 1}:")
        
        tempMajorList = []
        
        majorListInput = int(input(f"  How many Elements want in Minor List {majorList+ 1}? : "))
        
        for element in range(majorListInput):
            elementValue = input(f"      Enter value for Element {element+1}: ")
            tempMajorList.append(elementValue)
                
        finalList.append(tempMajorList)
        
else:
    listValue2 = int(input("How many elements (1d) want in your Final list : "))
    for element in range(listValue2):
        elementValue = input(f"      Enter value for Element {element+1}: ")
        finalList.append(elementValue)
    

print(finalList)



