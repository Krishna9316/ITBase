List1 = [1,1,2,3,3,4,2,1]
temp_dict = {}
for i in List1:
    temp_dict[i]= temp_dict.get(i , 0) + 1
print(temp_dict)

