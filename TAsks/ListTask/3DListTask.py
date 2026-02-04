finalList = []

listValue = int(input("How many Major list you want in your Final list : "))

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

print(finalList)

