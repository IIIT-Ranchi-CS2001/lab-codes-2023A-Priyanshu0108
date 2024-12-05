x = [int(x) for x in input("Enter multiple values: ").split()]
n=len(x)

mean=(sum(x)/n)
if(n%2==0):
    median=(x[(n//2)]+x[(n//2)+1])//2
else:
    median=(x[((n+1)//2)])
    

mode=max(x,key=x.count)

print("mean is : ",mean)
print("median is : ",median)
print("mode is: ",mode)