list1 = ["Daksh", "Daksh", "Krishna", "Helie","Gaurav", "Sejal","Sejal", "Gaurav", "Aastha", "Fenil", "Sahil", "Fenil", "Krishna"]

FinalDict = {}
FinalDict1 = {}

# count = 0
for i in list1:
    FinalDict[i]= FinalDict.get(i, 0)+1
print("Daksh is repeate : ", FinalDict["Daksh"], "Times in List")


for i in list1:
    if i in FinalDict1:
        FinalDict1[i] += 1
    else:
        FinalDict1[i] =1
        # pass
print(FinalDict1)
print("Krishna is repeate : ", FinalDict["Krishna"], "Times in List")