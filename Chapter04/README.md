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
11.  What are two ways to remove values from a list?

        ***A***.    
        ```python
        list.remove(value)
        del list[index]
        ``` 
---
12. Name a few ways that list values are similar to string values.

    Strings and lists both can be concatinated, and we can access any perticular value providing its index.
-----
13. What is the difference between lists and tuples?

    ***A***. List is a mutable type data, whereas tuple is immutable.
---------
14. How do you type the tuple value that has just the integer value 42 in it?


    ***A***. 
    ```python
    variable=(42)
    `````````
----------------
15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

    ***A***.
    ```python
    >>> tuple(['List'])
    >>> list(('tuple'))
    ```
----------
16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

    ***A***. All the variables contain the reference to the list value in hay.
-------
17.  What is the difference between copy.copy() and copy.deepcopy()?

     ***A***. If the list to be copied contains another list then deepcopy() should be used. Else copy() can be used.