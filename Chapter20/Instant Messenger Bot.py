import pyautogui,time
#from PIL import Image
time.sleep(10)
pyautogui.click('Chapter20/pic0.png',duration=1)

pyautogui.click('Chapter20/pic.png',duration=1)
#pyautogui.click(441,594,duration=1)
# print(loc)
# pyautogui.moveTo(loc)
# pyautogui.click()

# pyautogui.moveTo(828,1030,duration=2)

pyautogui.click('Chapter20/typeh.png',duration=1)

pyautogui.write("hey I am not human..............error")
pyautogui.press('enter')
pyautogui.write("Hello")

pyautogui.press('enter')