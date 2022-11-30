
from pyautogui import *
import cv2
from datetime import time
#==========================================get cursor position======================================================================
def pos():
    while True:
        sleep(2)
        print(position())
        waitkey = cv2.waitKey(1)
        if waitkey=="q":
            break
def scrollUp():
    scroll(-300)
def scrollDown():
    scroll(300)
