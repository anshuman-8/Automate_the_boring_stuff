
while True:
    try:
        li=input("Enter the list values").split()
    except:
        print("not a propper input")
    else:
        break

for i in li:
    print(i,", ",end="")

