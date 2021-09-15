import pyautogui
import time
time.sleep(5)
f = open("beemovie", 'r')
for word in f:
    pyautogui.typrewrite(word)
    pyautogui.press("enter")