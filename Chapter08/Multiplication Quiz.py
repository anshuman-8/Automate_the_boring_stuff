import pyinputplus as inp
import random
import time

print("Welcome to multiplication test")
print("You will get 10 question answer it within 8 seconds")

print("All the best")

for i in range(10):
    try:
        a=random.randint(0,9)
        b=random.randint(0,9)
        c=a*b
        
        ans=inp.inputInt("%s x %s = "%(a,b),limit=3,timeout=8)

        if(ans==c):
            print("Correct !!")
            time.sleep(3)
        else:
            print("Wrong answer !!")

    except TimeoutError:
        print("time out try answering within 8 sec")
