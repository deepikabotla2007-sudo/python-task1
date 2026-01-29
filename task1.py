name=input("enter your full name:")
email=input("enter your email ID:")
phno=input("enter your phone number:")
age=int(input("enter your age:"))
n=len(name)

if (name.count(" ")>=1 and name[0]!=" " and name[n-1]!=" " and
    email[0]!="@" and email.count("@")==1 and email.count(".")==1 and
    len(phno)==10 and phno.isdigit() and phno[0]!='0' and
    age>18 and age<60) :
 print("User Profile is VALID")
else:
 print("User Profile is INVALID")