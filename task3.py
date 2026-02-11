from unicodedata import category

m=int(input("enter the size of list: "))
marks=[0]*m
for i in range(m):
    marks[i]=int(input("enter the marks scored by student: "))

print("student marks: ",marks)

name="deepika"
name_length=len(name)

valid_count=0
fail_count=0

for mark in marks:
    if mark < 0 or mark > 100 :
        category="Invalid"
    else:
        valid_count+=1
        if mark % name_length ==0:
            category="lucky (because length of my name is 7)"
        elif mark >= 90:
            category = "Excellent"
        elif mark >= 75:
            category = "Very Good"
        elif mark >= 60:
            category = "Good"
        elif mark >= 40:
            category = "Average"
        else:
            category = "Fail"
            fail_count+=1


    print("Marks Scored: ", mark, "->", category)

print("Final Summary: ")
print("Total Valid Students: ", valid_count)
print("Total Fail Students: ", fail_count)



