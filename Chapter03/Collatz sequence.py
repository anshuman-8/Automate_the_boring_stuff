import sys

def collatz(number):
    if number%2==0:
        print(number//2)
        return(number//2)
    elif number%2==1:
        print(3*number+1)
        return(3*number+1)
try:
    n=int(input("Input: "))
except :
    print("Please input an integer")
    sys.exit()

a=collatz(n)
while True:
    a=collatz(a)
    if a==1:
        break