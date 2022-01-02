import re

def isLeapFeb(y,m):
    if (y%4==0 or y%100==0) and m==2:
        return True
    else:
        return False

def validDateCheck(d,m,y):
    if m>12:
        return False
    if d>31:
        return False
    if isLeapFeb(y,m):
        if d!=29:
            return False
    if m==2 and not isLeapFeb(y,m):
        if d!=28:
            return False
    return True


    

date=input("write date(format DD/MM/YYYY): ")
dateformat=re.compile(r'(\d\d/)\(d\d)/(\d\d)')

foundDate=dateformat.search(date)
#print(foundDate.group(1))

if validDateCheck(foundDate.group(1),foundDate.group(2),foundDate.group(3)):
    print("It is a valid date")
else:
    print("Not Valid")

