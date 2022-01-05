import pyautogui, random,time

try:
    while True:
        tim=random.randint(5,10)
        pyautogui.move(23,23,duration=0.5)
        time.sleep(tim)
        pyautogui.move(-23,-23,duration=0.5)
        time.sleep(tim)
except Exception:
    print("Over")

