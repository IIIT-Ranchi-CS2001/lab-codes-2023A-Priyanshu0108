import math

a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))

d=b**2-(4*a*c)

if(d==0):
    r1=(-b)/(2*a)
    r2=r1
    print("the roots are: ",r1,r2)
elif(d>0):
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("the roots are: ",r1,r2)
else:
    r1=(-b)/(2*a)
    r2=(math.sqrt(-d))/(2*a)
    print("the roots are: ",r1,r2)