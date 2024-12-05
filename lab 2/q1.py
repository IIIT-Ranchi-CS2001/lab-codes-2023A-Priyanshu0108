s1="Maha Bharat"
s2=lambda s1: s1[:1].lower() + s1[1:s1.find("Bharat")].upper() + s1[s1.find("Bharat")].lower()+ s1[s1.find("Bharat")+1:].upper()
print(s2(s1))

q=s1.find("Bharat")
s3=print(s1[q:])

s3=print(s1[q:]*3)

q=s1.replace("aha","era")
print(q)

print(q+" Mahan")