s1=input("Give the sentence: ")
listOfWords=s1.split(" ")
count=0
for words in listOfWords:
    if(words[::1]==words[::-1]):
        count+=1
        
print("No. of palindrome words are: ",count )