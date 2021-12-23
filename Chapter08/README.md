
# Chapter 08

## INPUT VALIDATION

## Solutions
------------
1. Does PyInputPlus come with the Python Standard Library?

    ***A***. No, pyinputplus does not come with standard library.
-----

2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?

    ***A***. In python PyInputPlus is imported as - import pyinputplus because it is a library, it can be referred as any variable here pyip.
-----

3. What is the difference between inputInt() and inputFloat()?

    ***A***. inputInt takes the integer value whereas inputFloat takes decimal input.
----

4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?

    ***A***. inputInt(min=0, lessThan=100)
----------

5. What is passed to the allowRegexes and blockRegexes keyword arguments?

    ***A***.  allowRegexes takes input which has to be their in the input and blockRegexes contain keyword which are not allowed as input.
--------

6. What does inputStr(limit=3) do if blank input is entered three times?

    ***A***. It will print Traceback error
-----------

7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?

    ***A***. It wii give output as hello.
-----