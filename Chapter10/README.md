
# Chapter 10

## ORGANIZING FILES

## Solutions

--------------

1. What is the difference between shutil.copy() and shutil.copytree()?

    ***A***. shutil.copy() will copy a file from one destination to another, whereas shutil.copytree() will copy the folder including its content to another location.
------------

2. What function is used to rename files?

    ***A***.  shutil.move() method can be used to rename the file of the new file name is given as move to address. 
----------

3. What is the difference between the delete functions in the send2trash and shutil modules?

    ***A***. Delete function in send2trash will not permanently delete the function rather move it to trash folder from where it can be again accessed, whereas delete function in shutil module will permanently delete the file which can not be further accessed.
----------------------------

4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?

    ***A***. The extract() method of zipFile is equivalent to open() function in File objects.
----------