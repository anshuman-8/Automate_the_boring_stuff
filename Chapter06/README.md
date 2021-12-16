
# Chapter 06

## MANIPULATING STRINGS

## Solutions

---
1. What are escape characters?

    ***A***. An escape character lets you use characters that are otherwise impossible to put into a string. Over here it is backslash(/).
-------
2. What do the \n and \t escape characters represent?

    ***A***. \n is used for leaving a line gap.
     \t is used for giving a tam space in a line. 
---------
3. How can you put a \ backslash character in a string?

    ***A***. Backslash is an escape sequence, so to write it use it with another escpe sequence, i.e. //.
-------
4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?

    ***A***. Since the string begins with a double quote, Python knows that the single quote is part of the string and not marking the end of the string.
-------
5. If you don’t want to put \n in your string, how can you write a string with newlines in it?

    ***A***. The string can be written inside triple single quots.
--------

6. What do the following expressions evaluate to?

    'Hello, world!'[1]\
    'Hello, world!'[0:5]\
    'Hello, world!'[:5]\
    'Hello, world!'[3:]

    ***A***. 'He'\
            'Hello,'\  
            'Hello,'\  
            'o, world!'
-------
7. What do the following expressions evaluate to?

    'Hello'.upper()\
    'Hello'.upper().isupper()\
    'Hello'.upper().lower()  

    ***A***. 'HELLO'  
              True\
            'hello'
----------
8. What do the following expressions evaluate to?

    a. 'Remember, remember, the fifth of November.'.split()  
b. '-'.join('There can be only one.'.split())
    
    ***A***. ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']       b. Therecanbeonlyone.
--------------
9. What string methods can you use to right-justify, left-justify, and center a string?

    ***A***. rjust() for right -justify, ljust() for left justify and center() to center the string.
-------
10. How can you trim whitespace characters from the beginning or end of a string?

    ***A***. by using strip() we can trim white spaces from the beginning and from the end.
------------