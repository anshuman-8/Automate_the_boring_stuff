
# Chapter 12

## WEB SCRAPING

## Solutions

---------------------

1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.

    ***A***. webbrowser module is used to search a link in a webbrowser and get the data, requests is used to download the data, bs4 is used to scrape data froma perticular website, and selenium module is used to work in the browser, like clicking inputing and basicly interacting with the website. 
--------
2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?

    ***A***. It contains the response the website gave for that link, to get the string value you can use .text method.
-------------
3. What requests method checks that the download worked?

    ***A***. status_code() method can be used for checking if the downloads worked.
-------------------

4. How can you get the HTTP status code of a requests response?

    ***A***. 200
---------------

5. How do you save a requests response to a file?

    ***A***. By using iter_content() method and then by using the write method of file to write in a file. 

-------------

6. What is the keyboard shortcut for opening a browser’s developer tools?

    ***A***. ctrl-shift-C
------------------

7. How can you view (in the developer tools) the HTML of a specific element on a web page?

    ***A***. By selecting the inspect element in the dveloper option.
-----------

8. What is the CSS selector string that would find the element with an id attribute of main?

    ***A***. .select('#idName')
-------

9. What is the CSS selector string that would find the elements with a CSS class of highlight?

    ***A***. .select('.highlight')
-------

10. What is the CSS selector string that would find all the \<div> elements inside another \<div> element?

    ***A***. .select('div div')
-------

11. What is the CSS selector string that would find the \<button> element with a value attribute set to favorite?

    ***A***. .select('button[value='favourite']')
-------

12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element \<div>Hello, world!\</div>. How could you get a string 'Hello, world!' from the Tag object?

    ***A***. a=soup.select('div')\
    a.get_text()
-------

13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?

    ***A***. linkElem=soup.attrs\
    this is by using attrs method
-------

14. Running import selenium doesn’t work. How do you properly import the selenium module?

    ***A***. from selenium import webdriver
-------

15. What’s the difference between the find_element_* and find_elements_* methods?

    ***A***. find_element_* returns a single web element that makes that condition, but find_elements_* returns all the web element that that meet its condition.
-------

16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?

    ***A***. By using Keys and click() method from find_element_*.
-------

17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium?

    ***A***. by directly using ckick() method.
-------

18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?

    ***A***. By using browser.back(), browser.forward() and browser.refresh() method.
-------