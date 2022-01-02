
# Chapter 14

## WORKING WITH GOOGLE SHEETS

## Solutions
-----------

1. What three files do you need for EZSheets to access Google Sheets?

    ***A***. 
    * A credentials file named credentials-sheets.json
   * A token for Google Sheets named token-sheets.pickle
   * A token for Google Drive named token-drive.pickle
----

2. What two types of objects does EZSheets have?

    ***A***. The two types of object EZSheets has is spreadsheet and sheet object
----

3. How can you create an Excel file from a Google Sheet spreadsheet?

    ***A***. ss=ezsheets.Spreadsheet()
         ss.downloadAsExcel('fineName.xlsx')
----

4. How can you create a Google Sheet spreadsheet from an Excel file?

    ***A***. ss=ezsheets.upload('sheetName.xlsx')
----

5. The ss variable contains a Spreadsheet object. What code will read data from the cell B2 in a sheet titled “Students”?

    ***A***. sheet=ss['Students']
         sheet['B2']
----

6. How can you find the column letters for column 999?

    ***A***. exsheets.getColumnLetterOf('999')
----

7. How can you find out how many rows and columns a sheet has?

    ***A***. You can read the number of rows and columns in a sheet with the rowCount and columnCount attributes. 
----

8. How do you delete a spreadsheet? Is this deletion permanent?

    ***A***. ss.delete(), no it will not delete it permanently, to delete it permanently use ss.delete(permanent=True)
----

9. What functions will create a new Spreadsheet object and a new Sheet object, respectively?

    ***A***. ezsheets.Spreadsheet and ezsheets.Sheet
----

10. What will happen if, by making frequent read and write requests with EZSheets, you exceed your Google account’s quota?

    ***A***. It will raise the googleapiclient.errors.HttpError “Quota exceeded for quota group” exception. 
----