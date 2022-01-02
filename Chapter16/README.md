
# Chapter 16

## Working with CSV Files and JSON Data

## Solutions
-----------
1. What are some features Excel spreadsheets have that CSV spread-sheets don’t?

    ***A***. We can not use formulas in CSV and can not shape the cell. We can not also make charts in CSV.
-----

2. What do you pass to csv.reader() and csv.writer() to create reader and writer objects?

    ***A***. we pass open file object with type r or w.
-----

3. What modes do File objects for reader and writer objects need to be opened in?

    ***A***. reader objects need to be oopened in 'r' whereas writer object have to be opened in 'w' mode.
-----

4. What method takes a list argument and writes it to a CSV file?

    ***A***. filewriter.writerow() method will write the list in the csv file.
-----

5. What do the delimiter and lineterminator keyword arguments do?

    ***A***. delimiter will make spaces or add character between the cells in a row, whereas literminator will make spaces or add character between the rows.
-----

6. What function takes a string of JSON data and returns a Python data structure?

    ***A***. json.loads() method
-----

7. What function takes a Python data structure and returns a string of JSON data?

    ***A***. json.dumps() method.
-----