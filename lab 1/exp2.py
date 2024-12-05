'''wap to find a) area and perimeter of traingle when alll three sides are given(take user input)
               b) find all three angles of the above traingle
'''

import math

a=int(input("Enter the first side: "))
b=int(input("Enter the second side: "))
c=int(input("Enter the third side: "))

s=(a+b+c)/2
p=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(p)
print("Area of triangle is : ",area)
print("Perimeter of triangle is: ",s*2)


A=math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
B=math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
C=math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))


print("Angle alpha is: ",A)
print("Angle beta is: ",B)
print("Angle gamma is: ",C)