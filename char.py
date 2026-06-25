sub1=int(input("enter the marks of sub1"))
sub2=int(input("enter the marks of sub2"))

total=sub1+sub2
percentage=total/200*100
print(percentage,"%")

if percentage>=90:
    print("obtaind A grade")
else:
    print("obtaind lover than A gade")