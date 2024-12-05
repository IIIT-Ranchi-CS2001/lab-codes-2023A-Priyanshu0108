name=[x.replace('_', ' ') for x in input("Enter the customer name: ").split(' ')]
ids=[x for x in input("Enter the customer id: ").split(" ")]
points=[int(x) for x in input("Enter the shopping point: ").split(" ")]


r=list(zip(name,ids,points))

print(r)

ans=[(e,ids[i],points[i]) for i, e in enumerate(name)]
print(ans)