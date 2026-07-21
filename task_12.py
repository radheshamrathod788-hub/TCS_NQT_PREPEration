#check alphabet digits and special char

a=input(":")
value=ord(a)
if (value>=65 and value<=90) or (value>=97 and value<=122):
    print("Alphabet")
elif value>=48 and value<=57:
    print("digit")
else:
    print("symbol") 
