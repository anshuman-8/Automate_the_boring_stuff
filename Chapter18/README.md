
# Chapter 18

## Sending Email and Text Messages

## Solutions
-----
1. What is the protocol for sending email? For checking and receiving email?

    ***A***. SMTP(Simple Mail Transfer Protocol) is the main sending protocol, IMAP(Internet Message access Protocol) is the protocol used for receving checking the mail.
------

2. What four smtplib functions/methods must you call to log in to an SMTP server?

    ***A***. smtpObj=smtplib.SMTP('serverdomain.com',587)\
    smtpObj.ehlo()\
    smtpObj.login('mymail@mail.com','mypassword')

------

3. What two imapclient functions/methods must you call to log in to an IMAP server?

    ***A***. imapObj=imapclient.IMAPClient('example.com',ssl=True)
    imapObj.login('mymail@mail.com','password')
------

4. What kind of argument do you pass to imapObj.search()?

    ***A***. A list is passed in the search() containing the search argument.
------

5. What do you do if your code gets an error message that says got more than 10000 bytes?

    ***A***. To prevent this from happening we can use  imaplib._MAXLINE = 1939993 or any greater number. 
------

6. The imapclient module handles connecting to an IMAP server and finding emails. What is one module that handles reading the emails that imapclient collects?

    ***A***. .fetch() module.
------

7. When using the Gmail API, what are the credentials.json and token.json files?

    ***A***.  With credentials.json and token.json, your Python scripts can send and read emails from your Gmail account without requiring you to include your Gmail password in your source code.
------

8. In the Gmail API, what’s the difference between “thread” and “message” objects?

    ***A***. Gmail organizes emails that are replies to each other into conversation threads. Message are the content the thread holds.
------

9. Using ezgmail.search(), how can you find emails that have file attachments?

    ***A***. ezgmail.search('has:attachment')
------

10. What three pieces of information do you need from Twilio before you can send text messages?

    ***A***. 
------