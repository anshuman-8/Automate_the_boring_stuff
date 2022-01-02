
# Chapter 13

## WORKING WITH EXCEL SPREADSHEETS

## Solutions
--------
1. What does the openpyxl.load_workbook() function return?

    ***A***. It returns an sheet object.
--------

2. What does the wb.sheetnames workbook attribute contain?

    ***A***. It constains a list contining names of all the sheets. 
--------

3. How would you retrieve the Worksheet object for a sheet named 'Sheet1'?

    ***A***. sheet=wb['Sheet1'] # where wb is the sheet object
--------

4. How would you retrieve the Worksheet object for the workbook’s active sheet?

    ***A***. 
--------

5. How would you retrieve the value in the cell C5?

    ***A***. sheet['C5'].value
--------

6. How would you set the value in the cell C5 to "Hello"?

    ***A***. sheet['C5']="Hello"
--------

7. How would you retrieve the cell’s row and column as integers?

    ***A***. sheet.max_rows  or max_cloumn
--------

8. What do the sheet.max_column and sheet.max_row sheet attributes hold, and what is the data type of these attributes?

    ***A***. max_column holds the maximum number of columns in the sheet similar with max_rows. They give out integer.
--------

9. If you needed to get the integer index for column 'M', what function would you need to call?

    ***A***. Column_index_form_Sting('M')
--------

10. If you needed to get the string name for column 14, what function would you need to call?

    ***A***. get_Column_letter(14)
--------

11. How can you retrieve a tuple of all the Cell objects from A1 to F1?

    ***A***. 
    ```python
        for rowOfCellObjects in sheet['A1':'C3']:      
            for cellObj in rowOfCellObjects:
                print(cellObj.coordinate, cellObj.value)
    ```
--------

12. How would you save the workbook to the filename example.xlsx?

    ***A***. 
--------

13. How do you set a formula in a cell?

    ***A***. indicating the cell address write '=SUM(fromcell:tocell)'
--------

14. If you want to retrieve the result of a cell’s formula instead of the cell’s formula itself, what must you do first?

    ***A***.
--------

15. How would you set the height of row 5 to 100?

    ***A***. sheet.row_dimentions[5].height=100
--------

16. How would you hide column C?

    ***A***. sheet.column_dimensions['C'].hidden = True
--------

17. What is a freeze pane?

    ***A***. freeze pane will freex a perticular set of rows which can be seen from all the part of the sheet.
--------

18. What five functions and methods do you have to call to create a bar chart?

    ***A***. 
    ```python
    refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1,max_col=1,max_row=10)
    seriesObj = openpyxl.chart.Series(refObj, title='First series')
    chartObj = openpyxl.chart.BarChart()
    chartObj.append(seriesObj)
    sheet.add_chart(chartObj, 'C5')
--------

