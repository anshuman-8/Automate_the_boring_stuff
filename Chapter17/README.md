
# Chapter 17

## KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS

## Solutions
----------
1. What is the Unix epoch?

    ***A***. The Unix epoch is a time reference commonly used in programming: 12 AM on January 1, 1970, Coordinated Universal Time (UTC).
-----

2. What function returns the number of seconds since the Unix epoch?

    ***A***. time.time() method
-----

3. How can you pause your program for exactly 5 seconds?

    ***A***. time.sleep(5)
-----

4. What does the round() function return?

    ***A***. this returns the whole number after approxing a decimal number.
-----

5. What is the difference between a datetime object and a timedelta object?

    ***A***. datetime object returns the perticular date where as timedelta returns the date or time difference.
-----

6. Using the datetime module, what day of the week was January 7, 2019?

    ***A***. 
    ```pyhton
    import datetime
    tim=datetime.datetime.strptime('January 7 2019','%B %d %Y')
    tim.strftime('%A')
    'Monday'
    ```

-----

7. Say you have a function named spam(). How can you call this function and run the code inside it in a separate thread?

    ***A***. 
-----

8. What should you do to avoid concurrency issues with multiple threads?

    ***A***.
-----