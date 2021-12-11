# Chapter 02

# FLOW CONTROL
## Solutions
---
1. What are the two values of the Boolean data type? How do you write them?

        Two data types are :
          True
          False
---
2. What are the three Boolean operators?

        or
        and
        not
---
3. Write out the truth tables of each Boolean operator (that is, every  possible combination of Boolean values for the operator and what they    evaluate to).

    Expression| Evaluate to
    -----|-----
    |True and True | True| 
    |True or True |True    | 
    |not True   |False
    |False and False |False
    |False or False| Flase
    |not False| True
    |True and False| False
    |True or False| True
---
4. What do the following expressions evaluate to?\
    a. (5 > 4) and (3 == 5)\
b. not (5 > 4)\
c. (5 > 4) or (3 == 5)\
d. not ((\5 > 4) or (3 == 5))\
e. (True and True) and (True == False)\
f. (not False) or (not True)

        a. False
        b. False
        c. True
        d. False
        e. False
        f. True
---
5. What are the six comparison operators?

    Operator|Meaning
    --------|-------
    ==|Equal to
    !=| Not Equal to
    <|Less than
    |>|Greater Than
    <=| Less than or equal to
    |>=| Greater than or equal to|
---
6.  What is the difference between the equal to operator and the assignment operator?

        Assignment operator assigns a value to an variable, i.e. '='.
        Whereas equal to  checks if both the value are equal or not, i.e. '=='.

---
7. Explain what a condition is and where you would use one.

        Equal to operator(==) is used when we are suppose to compare two values, example: 2==2. 
        Assignment operator(=) is used to assign a value to a variable, example: a=23.
---
8.  Identify the three blocks in this code:

```python
spam = 0
if spam == 10:
        print('eggs')
    if spam > 5:
        print('bacon')
    else:   
        print('ham')
    print('spam')
print('spam')
```
        The first block the is if block comparing the value between spam and 10.
        Second Block is the nested if block comparing the value between span and 5 & printing 'bacon'.
        Third Block is the nested else block printing 'ham'.
---
9.  Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

```python
if span==1:
    print("Hello")
elif span==2:
    print("Howdy")
else:
    print("Greetings!")
```
----------
10. What keys can you press if your program is stuck in an infinite loop?

        CTRL-C         

------
11. What is the difference between break and continue?

        When the program execution reaches the continue statement it stops the further execution and goes to the top of the loop, 
        whereas in break statement the program exits the loop.  
-----
12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?

        range(10)       -> reads from 0 to 9(included)
        range(0, 10)    -> reads from 0 to 9(included)
        range(0, 10, 1) -> reads from 0 to 9(included)

        there is no difference between all three of them 

---
13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
```python
# using for loop
for i in range(1,11):
    print(i)

# using while loop
i=1
while i<=10:
    print(i)
```
-----
14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
```python
import spam
spam.bacon()
```
    