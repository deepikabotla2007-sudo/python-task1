from operator import and_

stID = input("Enter Student ID : ")
email = input("Enter Email ID : ")
password = input("Enter Password : ")
referral = input("Enter Referral Code : ")

valid=False

if len(stID)==7 and stID[0:3]=="CSE" and stID[3]=="-" and stID[4].isdigit() and stID[5].isdigit() and stID[6].isdigit():
 valid=True

if valid:
  if email.count("@")>=1 and email.count(".")>=1 and email[0]!="@" and email[len(email)-4:len(email)]==".edu":
    valid=True

if valid:
  if len(password)>=8 and password[0].isupper() and (password[0].isdigit() or password[1].isdigit() or password[2].isdigit() or password[3].isdigit() or password[4].isdigit() or password[5].isdigit() or password[6].isdigit() or password[7].isdigit()):
    valid=True

if valid:
  if referral[0:3]=="REF" and referral[3].isdigit() and referral[4].isdigit() and referral[len(referral)-1]=="@":
     valid =True

if valid:
 print("APPROVED")
else:
 print("REJECTED")