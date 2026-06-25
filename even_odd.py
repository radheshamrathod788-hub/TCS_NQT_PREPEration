#print the eve odd number without if else 
# print the even odd number using only for loop withour 

#normaly using if else

for i in range(11):
    if (i%2==0):
        print(i,"ever number")
    else:
        print(i,"odd number")

# acording to Q.


for i in range(2,22,2):
    print( i ,end=" ",)

print("odd number:")
for i in range(1,22,2):
    print(i,end=" ")

# sum of 1st 10 natural number using only for loop
# 1 2 3 4 5 6 7 8 9 

addition = 0;
for i in range(1,11):
    #addition = addition + i
    addition+=i
    print(i,end=" ")
print("addition=",addition)
