# DAfinition of For Loop => It is used when yo know the value of iteration 

# syntax => for(Condition):
                # print
                
                
# for loop on 2D Array
                
mylist1 = ["krishna","Raj ","Sumit","Umang","RAhul"]
mylist2 = ["Banana","Apple","cherry","orange"]

my2dlist = [mylist1,mylist2]
# print(my2dlist)

for i in my2dlist:
    for j in i:
        print(j)
    print(i)  
    
    
    
# for loop on 3d List

my3dlist = [
                [ ["Name","Krishna"],["Age","20"],["Course","iMsc IT"]],
                [ ["Name","Raj"],["Age","21"],["Course","B.Tech"]],
                [ ["Name","Gaurav"],["Age","22"],["Course","BCA"]]
            ]
# print(my3dlist) 

for i in my3dlist :
    for j in i:
        for k in j:
            print(k)
        # print(j)
        
    print(i)


