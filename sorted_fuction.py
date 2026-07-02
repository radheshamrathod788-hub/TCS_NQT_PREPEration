
#sort fuction arrenged the valu in assending data
tuple1=(1,2,3,4,5,63,2,4,5)
print(sorted(tuple1))

#hard code for sorted fuctin in putle
#bubble sort using for loop
#while loop

list1=list(tuple1)
for i in range(len(list1)):
    for j in range(len(list1)-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            
print(list1)
