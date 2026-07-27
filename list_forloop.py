list=[1,2,3,4,5]
#value=

   # print(i,end=" ")
   
    #print(list.index(i),end=" ")
    #print("\n")
    #if i ==5:
    #print(list[i])  #  0 1 2 3 4 them 5 
                    #after 5 function go's out of range
for i in range(0,len(list)):
    print(i)

for i in range(len(list)):  #this code is use for solve the error of out of range 
    if list[i]==i+1:          #if we want to print (list[i]) then use this method
        print(i)

    #hard code logic

'''n=len(list)-1
print("value of n",n)
check=False            " #error" dont try this
for i in list:
    if i==n:
        check=True
if check==False:
'''

