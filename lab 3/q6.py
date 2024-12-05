string = input("Enter the string: ")
check= input("Enter the character to count occurence: ")
count=0
for char in string:
    if(char==check):
        count+=1
        
print("The given character appears",count,"times")