import re

word=input("Enter the password to check: ")

if len(word) < 8:
    print("not valid")
    exit()

numcheck=re.compile(r'\d')
c=0
for i in word:
    if i.isupper:
        c+=1
        break
for i in word:
    if i.islower:
        c+=1
        break

for i in word:
    if i.isdigit:
        c+=1
        break

if c==3:
    print("valid")
else:
    print("Invalid")

if i.islower:
        c+=1