# Chapter 07

##

## Solutions
----------
1. What is the function that creates Regex objects?

    ***A***.  re.compile()  
-----
2. Why are raw strings often used when creating Regex objects?

    ***A***. To find text by providing resembling raw text. 
---------------------
3. What does the search() method return?

    ***A***. search() method searches the string it is passed for any matches to the regex. 
-----------
4. How do you get the actual strings that match the pattern from a Match object?

    ***A***. match_object.group(), by using group method.
-------------------
5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?

    ***A***. group 0 will print whole number, group 1 will print first part of the number of raw string \d\d\d, group 2 will print second part of the number of raw string \d\d\d-\d\d\d\d.
---------

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

    ***A***. 
------------

7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

    ***A***. If the regular expression does not have any groups then findall() will return a string, but if the regular expression have groups then findall() will return a tuple.
----------

8. What does the | character signify in regular expressions?

    ***A***. 
-----------------

9. What two things does the ? character signify in regular expressions?

    ***A***.
---------------

10. What is the difference between the + and * characters in regular expressions?

    ***A***. 
----------

11. What is the difference between {3} and {3,5} in regular expressions?

    ***A***. {3} will match the text three times but {3,5} will match the text from three times till five times.
------

12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?

    ***A***. 
--------------

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?

    ***A***. 
------------

14. What is the difference between .* and .*??

    ***A***. The dot-star(.\*) uses greedy mode: It will always try to match as much text as possible. To match any and all text in a non-greedy fashion, use the dot, star, and question mark (.*?). 
-----------------

15. What is the character class syntax to match all numbers and lowercase letters?

    ***A***. 
----------------------

16. How do you make a regular expression case-insensitive?

    ***A***. 
-------------------

17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?

    ***A***. 
---------

18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?

    ***A***.
---

19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?

20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

    '42'\
    '1,234'\
    '6,368,745'\
    but not the following:

    '12,34,567' (which has only two digits between the commas)\
    '1234' (which lacks commas)

21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

'Haruto Watanabe'
'Alice Watanabe'
'RoboCop Watanabe'
but not the following:

'haruto Watanabe' (where the first name is not capitalized)
'Mr. Watanabe' (where the preceding word has a nonletter character)
'Watanabe' (which has no first name)
'Haruto watanabe' (where Watanabe is not capitalized)
22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

'Alice eats apples.'\
'Bob pets cats.'\
'Carol throws baseballs.'\
'Alice throws Apples.'\
'BOB EATS CATS.'\
but not the following:

'RoboCop eats apples.'\
'ALICE THROWS FOOTBALLS.'\
'Carol eats 7 cats.'
