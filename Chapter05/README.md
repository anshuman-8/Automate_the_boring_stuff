
# Chapter 05

## DICTIONARIES AND STRUCTURING DATA 

## Solutions
---
1. What does the code for an empty dictionary look like?

    ***A***. 
    ```python
    dict = {}
    ```
    { }
---
2. What does a dictionary value with a key 'foo' and a value 42 look like?

    ***A***. 
     { 'foo' : 42 } 
-----
3. What is the main difference between a dictionary and a list?

    ***A***. Dictonary can store key value pair, whereas List store only the value.
-----
4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?

    ***A***. It give       >>> KeyError: 'foo'
-------
5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

    ***A***. Expression 'cat' in span prints the value of the key cat, whereas .keys() will print a list dict_keys containing all the value.
----------
6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?


    ***A***. The expresssion cat in spam prints the value of the key cat, and ,values print all the values in the dictonary spam in a list dict_values.
----
7. What is a shortcut for the following code?
    ```python
    if 'color' not in spam:
        spam['color'] = 'black'
    ```
    
    ***A***. 
    ```python

------
8. What module and function can be used to “pretty print” dictionary values?

    ***A***. module is pprint, and function is pprint().

---