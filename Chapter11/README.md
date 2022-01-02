
# Chapter 11

## DEBUGGING

## Solutions
---------------
1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

    ***A***. assert spam > 10
--------------

2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).

    ***A***. assert eggs.upper() != bacon.upper() 
--------------

3. Write an assert statement that always triggers an AssertionError.

    ***A***.assert 1!=1
--------------

4. What are the two lines that your program must have in order to be able to call logging.debug()?

    ***A***. import logging\
                  logging.basicconfig(level=lgging.DEBUG)
--------------

5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

    ***A***. import logging\
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
%(asctime)s -  %(levelname)s -  %(message)s')
--------------

6. What are the five logging levels?

    ***A***. debug\
    info\
    warning\
    error\
    critical
--------------

7. What line of code can you add to disable all logging messages in your program?

    ***A***.logging.disable(logging.CRITICAL)
--------------

8. Why is using logging messages better than using print() to display the same message?

    ***A***. It can disabled easily rather than removing all of them in print.
--------------

9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

    ***A***. 
--------------

10. After you click Continue, when will the debugger stop?

    ***A***. No, on clicking continue the program will be executed , its only if it reaches a breakpoint it will stop.
--------------

11. What is a breakpoint?

    ***A***. Break point is a tag that is placed on a perticular line of code that forces the debugger to stop.
--------------

12. How do you set a breakpoint on a line of code in Mu?

    ***A***. To set a breakpoint, click the line number in the file editor to cause a red dot to appear, marking the breakpoint
--------------