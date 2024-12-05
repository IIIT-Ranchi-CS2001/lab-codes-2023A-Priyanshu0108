code=[int(x) for x in input("enter the course codes : ").split()]
name=[x for x in input("enter the course names : ").split()]
# print(code)
# print(name)
new_list=[f"{i}:{j}" for i,j in zip(code,name)]
print(new_list)