
import re

helloFile = open('/home/anshuman/Desktop/Anshuman/Automate_the_boring_stuff/Chapter09/Romeodf.txt')

helloContent = helloFile.read()
line=input("Enter the line you want to search in Romeo and Juleit play : ")
mo=re.compile(r'')

j=0
for i in helloContent.split('. '):
    # print(i)
    a=mo.finditer(i)
    if a is not None:
        print("Found !!")
        print(line)
        print(" In Line/Paragraph \n")
        print(i)
