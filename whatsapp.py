import pyautogui
import time
time.sleep(3)
count=0
while count<=200:
    pyautogui.typewrite("tested text" +str(count))
    pyautogui.press("enter")
    count=count+1