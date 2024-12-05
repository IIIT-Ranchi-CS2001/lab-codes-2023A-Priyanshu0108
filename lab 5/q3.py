inp_str=input("enter the string: ")

all_freq={}

for i in inp_str:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1
        
# print("count of all character is: " +str(all_freq))
print(all_freq)
# print(type())