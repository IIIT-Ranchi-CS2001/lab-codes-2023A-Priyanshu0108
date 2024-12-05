def sum(a,b):
    sum=a+b
    print("Sum is:",sum)

def product(a,b):
    product=a*b
    print("Product is:",product)

def division(a,b):
    division=a/b
    print("Division is:",division)

def substraction(a,b):
    sub=a-b
    print("Substraction is: ",sub)
    
def intquo(a,b):
    intquo=a//b
    print("Integer qoutient is: ",intquo)
    
while True:
    a=int(input("Enter first number: "))
    b=int(input("ENter second number: "))
    sum(a,b)
    product(a,b)
    division(a,b)
    substraction(a,b)
    intquo(a,b)
    