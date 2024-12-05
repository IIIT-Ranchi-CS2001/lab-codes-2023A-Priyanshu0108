name=input("Enter the name of student: ")
roll=int(input("Enter the roll of student: "))
Marks=int(input("Enter the mark in math: "))

if(Marks>=90):
    grade=10
    remark="Outstanding"
elif(90 > Marks >= 80):
    grade=9
    remark="Very good"
elif(80 > Marks >= 70):
    grade=8
    remark="Good"
elif(70 > Marks >= 60):
    grade=7
    remark="Average"
elif(60 > Marks >= 50):
    grade=6
    remark="Pass"
else:
    grade=0
    remark="Fail"
    
print("Name: ",name)
print("Roll: ",roll)
print("Marks: ",Marks)
print("Grade: ",grade)
print("Remark: ",remark)