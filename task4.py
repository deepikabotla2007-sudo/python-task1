m=int(input("enter the size of the list: "))
scores=[0]*m
for i in range(m):
    scores[i]=int(input("enter the student's score: "))

print("scores of students: ",scores)

Invalid_count=0
Valid_count=0
low_risk = []
medium_risk = []
high_risk = []
critical_risk = []

for score in scores:
    if score<0:
        Invalid_count+=1
    else:
        Valid_count+=1
        if score>=0 and score<=30:
            low_risk.append(score)
        elif score>30 and score<=60:
            medium_risk.append(score)
        elif score>60 and score<=100:
            high_risk.append(score)
        else:
            critical_risk.append(score)

print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

D=int(input("\nenter the last digit of your registration number: "))
removed_count = 0
if D % 2 == 0:
    print("D is EVEN(Removing all Low Risk scores)")
    removed_count = removed_count + len(low_risk)
    low_risk = []
else:
    print("D is ODD(Removing all Critical Risk scores)")
    removed_count = removed_count + len(critical_risk)
    critical_risk = []

print("\nAfter Personalized Filtering:")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

print("\nTotal Valid Entries:", Valid_count)
print("Ignored Entries:", Invalid_count)
print("Removed Due to Personalization:", removed_count)
