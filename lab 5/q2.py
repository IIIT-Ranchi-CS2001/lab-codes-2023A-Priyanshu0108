p1=[int(x) for x in input("Enter the coordinate of point1: ").split()]
p2=[int(x) for x in input("Enter the coordinate of point2: ").split()]

a1=(p1[0]-p2[0])/(p1[1]-p2[1])
ans=f"(x-{p1[0]})=({a1}) (y-{p1[1]})"

print(ans)