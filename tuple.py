#what is tuple
#it is a collection datatype 
#it is a collection data structure list tuple set dictnory
#tuple is a built in python data type
#used to store the multiple values in a single variable
#it is ordered and immutable collection
#which means once a tuple is created 
#we cannot remove , change or add the values of the tuple
#tuple_name =(val1,val2,val3,....)



student =("yash",20 , "python")
print(type(student))
print(student)

#characteristics of tuple
#orded
tuple=(1,2,3,4,5)
print(tuple[3])
#endex wise data insert
#Immutable you can not modigy elemtns after creation
#tuple1=(10,20,30,40,50)
#tuple[2]=30
#print(tuple1)

#allow duplicate values
#can store diffrent data types
tuple2=(1,2,3,4,44,5,5,6,6,6,6,3)
print(tuple2)

#support negative indexing
# indexing start form 0  
#last size size -1==> -1,-2,-3
print(tuple2[-1])

# +ve indexing (0 1 2 3 4 5 6......)
# -ve indexing (-4,-3,-2,-1,.......)

#how to create empty tuple
tuple=()
print(tuple)
print(type(tuple))
tuple5=(10,)
print(type(tuple5))


