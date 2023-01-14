import pyautogui
import time
message = 3
while message >0:
    time.sleep(2)
    pyautogui.typewrite('Where are you?')
    time.sleep(2)
    pyautogui.press('enter')
    message = message - 1