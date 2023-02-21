import pyautogui
import pyautogui as pag
import random
import time
pyautogui.FAILSAFE = True

while True:
    x = random.randint(600, 1000)
    y = random.randint(200, 1000)
    pag.moveTo(x, y, 1)
    time.sleep(0.2)
