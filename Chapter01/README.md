
# Chapter 01

## Solutions

1.  Which of the following are operators, and which are values?

        *         -> Operator
        'hello'   -> Value
        -88.8     -> Value
        -         -> Operator
        /         -> Operator
        +         -> Operator
        5         -> Value

---

2.  Which of the following is a variable, and which is a string?

        spam    -> Variable
        'spam'  -> String
        
---
3. Name three data types.

        String
        Integer
        Float
---
4. What is an expression made up of? What do all expressions do?
        
        Expressions are most basic form of programming instructions, consisting of values and operators.
        These expressions evaluate down the expression to a single value.
---
5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?

        Expression is a programming instruction consisting of Values and operators which can be further evaluated,
        whereas statements executes some code like assigning a value to a variable.
---
6. What does the variable bacon contain after the following code runs?\
    bacon = 20\
    bacon + 1

        20
---
7. What should the following two expressions evaluate to?\
    'spam' + 'spamspam'\
    'spam' * 3
        
        spamspamspam
        spamspamspam
---
8. Why is eggs a valid variable name while 100 is invalid?
        
        A variable cannot start from an integer but can start from an alphabet.
---
9. What three functions can be used to get the integer, floating-point number, or string version of a value?

        value="309.02"
        int_value=int(value)
        str_value=str(int_value)
        float_value=float(str_value)

        
---
10. Why does this expression cause an error? How can you fix it?\
    'I have eaten ' + 99 + ' burritos.'

        Python can only concatinate string with a string not integer.
        Can be corrected by converting 99 to string.
        correction=>
              'I have eaten '+ '99'+' burritos.'