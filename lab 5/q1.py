from math import sqrt

point1=tuple(map(int,input("Enter coordinate of first point x1,y1,z1: ")))
point2=tuple(map(int,input("Enter coordinate of second point x2,y2,z2: ")))

d=sqrt(((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2)+((point1[2]-point2[2])**2))

print(d)
