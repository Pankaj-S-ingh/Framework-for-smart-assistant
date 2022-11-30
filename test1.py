from Utils.util import *
from Features import * 
import pyautogui,webbrowser
def irctc():
    speak("enter source and destination: ")
    source=input("enter source:")
    destination=input("enter destination: ")
    webbrowser.open("https://www.irctc.co.in/nget/train-search")
    sleep(5)
    click(1922,1440,interval=0.4)
    sleep(2)
    click(500,1066,interval=0.4)
    sleep(1)
    write(source)
    sleep(1)
    press('enter')
    sleep(1)
    click(683,1234,interval=0.4)
    sleep(1)
    write(destination)
    press('enter')
    sleep(2)
    press('enter')
    sleep(1)
    press('enter')






