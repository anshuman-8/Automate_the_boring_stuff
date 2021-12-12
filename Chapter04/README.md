# Chapter 04

## Lists

## Sloutions
--- 
1. What is [ ]?

    ***A***. It is a square brackets which are used to write Lists. All Lists starts with opening brackets and closing brackets.
-----
2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)

    For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

    ***A***.    
    ```python
    span[2]="Hello"
    ```
-------------
3. What does spam[int(int('3' * 2) // 11)] evaluate to?

    ***A***.    
    ```python
    >>> spam[int(int('3' * 2) // 11)]
        'c'
    ```
------
4. What does spam[-1] evaluate to?

    ***A***.    
    ```python
    >>> spam[-1]
        'd'
    ```
------
5. What does spam[:2] evaluate to?

    For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
    
    
    ***A***.  

    ```python
    >>>span[:2]
        [3.14,'cat']
    ```
------
6.  What does bacon.index('cat') evaluate to?

    ***A***. 
    ```python
        >>> bacon.index('cat')
            1
    ```
----------
7. What does bacon.append(99) make the list value in bacon look like?

    ***A***.  bacon will become, [3.14, 'cat', 11, 'cat', True, 99]   
----
8. What does bacon.remove('cat') make the list value in bacon look like?

    ***A***.   [3.14, 11, 'cat', True, 99]
-------
9. What are the operators for list concatenation and list replication?

    ***A***. List1+List2    --> Concatination\
                List*3         --> Replication
---
10. What is the difference between the append() and insert() list methods?

    ***A***.    append() , adds an value to the end of the list\
                insert(), inserts the value in the perticular given index
------
