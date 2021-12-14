import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    li=[]
    for i in range(100):
        c=random.randint(0,1)
        li.append(c)
    
 # Code that checks if there is a streak of 6 heads or tails in a row.
    ch=0
    past=None
    for toss in li:
        #print("do")
        if toss==past:
            ch+=1
        else:
            ch=0

        if ch==6:
            numberOfStreaks+=1
            ch=0
        past=toss
print('Chance of streak: %s%%' % (numberOfStreaks / 100))