sub1=int(input("enter the sub1 marks:"))
sub2=int(input("enter the sub2 marks:"))
sub3=int(input("enter the sub3 marks:"))
sub4=int(input("enter the sub4 marks:"))
sub5=int(input("enter the sub5 marks:"))

total=sub1+sub2+sub3+sub4+sub5
percentage=total/500*100

if percentage>=90:
    print("Pass",percentage,"%")
    print("obtaind A+ grade")
elif percentage>=80:
    print("Pass",percentage,"%")
    print("obtaind A grade")
    
elif percentage>=70:
    print("Pass",percentage,"%")
    print("obtaind B+ grade")
elif percentage>=60:
    print("Pass",percentage,"%")
    print("obtainde B grade")
elif percentage>=50:
    print("Pass",percentage,"%")
    print("obtaind C+ grade")
elif percentage>=40:
    print("pass",percentage,"%")
    print("obtaind C grade")
else:
    print("fail")
