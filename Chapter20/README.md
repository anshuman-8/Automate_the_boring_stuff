
# Chapter 20

##  Controlling the Keyboard and Mouse with GUI Automation

## Solutions
-----
1. How can you trigger PyAutoGUI’s fail-safe to stop a program?

    ***A***. Therer are two ways to do it,
    * quickly dragging the cursor to the screen corner
    * Stopping the program by ctrl+Alt+Del
------

2. What function returns the current resolution()?

    ***A***. pyautogui.sixe()
------

3. What function returns the coordinates for the mouse cursor’s current position?

    ***A***. pyautogui.position()
------

4. What is the difference between pyautogui.moveTo() and pyautogui.move()?

    ***A***. .moveTo rakes the position on the screen and instantly take the cursor to that position, .move() goes to the direction relative to the current position of the cursor.
------

5. What functions can be used to drag the mouse?

    ***A***. .drag() and .dragTo() can be used to drag the mouse cursor.
------

6. What function call will type out the characters of "Hello, world!"?

    ***A***. pyautogui.write("Hello World!!")
------

7. How can you do keypresses for special keys such as the keyboard’s left arrow key?

    ***A***. pyautogui.write(['left'])
------

8. How can you save the current contents of the screen to an image file named screenshot.png?

    ***A***.
    ```python 
    imag=pyautogui.screenshot()
    imag.save('screenshot.png')
------

9. What code would set a two-second pause after every PyAutoGUI function call?

    ***A***. by using time.sleep(2) after importing time library.
------

10. If you want to automate clicks and keystrokes inside a web browser, should you use PyAutoGUI or Selenium?

    ***A***. PyAutoGUI
------

11. What makes PyAutoGUI error-prone?

    ***A***. 
------

12. How can you find the size of every window on the screen that includes the text Notepad in its title?

    ***A***. 
------

13. How can you make, say, the Firefox browser active and in front of every other window on the screen?

    ***A***. 
------