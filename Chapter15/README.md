
# Chapter 15

## WORKING WITH PDF AND WORD DOCUMENTS

## Solutions
-----------
1. A string value of the PDF filename is not passed to the PyPDF2.PdfFileReader() function. What do you pass to the function instead?

    ***A***. pdf open object is passed in write mode.
----

2. What modes do the File objects for PdfFileReader() and PdfFileWriter() need to be opened in?

    ***A***. PdfFileReader() has to opened in rb i.e. read binary mode where as PdfFileWriter() has to written in wb i.e. write binary mode. 
----

3. How do you acquire a Page object for page 5 from a PdfFileReader object?

    ***A***. pdfFileReader.getPage(5)
----

4. What PdfFileReader variable stores the number of pages in the PDF document?

    ***A***. 
----

5. If a PdfFileReader object’s PDF is encrypted with the password swordfish, what must you do before you can obtain Page objects from it?

    ***A***. pdfobj.decrypt('swordfish')
----

6. What methods do you use to rotate a page?

    ***A***. pageobj=padfReader.getpage(0)
             pageobj.rotateClockwise(90)
----

7. What method returns a Document object for a file named demo.docx?

    ***A***. docx.Document('demo.docx')
----

8. What is the difference between a Paragraph object and a Run object?

    ***A***. paragraph object contains different paragraphs of the doc whereas run objects of different types inside a paragraph 
----

9. How do you obtain a list of Paragraph objects for a Document object that’s stored in a variable named doc?

    ***A***. 
   doc.paragraphs

----

10. What type of object has bold, underline, italic, strike, and outline variables?

    ***A***. run object
----

11. What is the difference between setting the bold variable to True, False, or None?

    ***A***. turning bold variable to tru will return statement to bold, False will un bold if it is bold and None will not do anything.
----

12. How do you create a Document object for a new Word document?

    ***A***. doc=docx.Document()
----

13. How do you add a paragraph with the text 'Hello, there!' to a Document object stored in a variable named doc?

    ***A***. doc.add_paragraph("Hello, There!")
----

14. What integers represent the levels of headings available in Word documents?

    ***A***. integers 0 to 4
----

