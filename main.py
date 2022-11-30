#============================================ Module Portion ========================================================================================
#from Jarvis import JarvisAssistant

#import pyautogui
from Features import *
import numpy as np

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import re
import sys
from datetime import datetime
import numpy as np  # for mathmatical operaton
#from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
#from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvis.features.gui import Ui_MainWindow
from Jarvis.features.func import *

from bs4 import BeautifulSoup
from pywikihow import WikiHow, search_wikihow
from path import *
# =======================================================================================================================================================
engine = pyttsx3.init('sapi5') #initialization of pyttsx3 engine and 'sapi5' is a driver name 
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
asst_name="kush"
#==================================================================================================================================

#=======================================================================================================================================================
def speak(audio):
    engine.say(audio)
    engine.runAndWait() #This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you. 
    '''Blocks while processing all currently queued commands. Invokes callbacks for engine notifications appropriately.
     Returns when all commands queued before this call are emptied from the queue.'''

#================================================================take command=================================================================================


#==============================================================================================================================================
#=================================================================================================================================================    

#==================================================================================================================================================

#==================================================================STARTING OF COMMAND SECTION ==================================================================================
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()
    asst_name="kush"
    def TaskExecution(self):
        
        #unlock()
        #startup(asst_name)
        
    
        while True:
            query =takeCommand().lower()
  #====================================================WIKIPIDIA SECTION============================================================================               
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
#============================================intro part==========================================================================================
            elif "about yourself" in query:
                speak(f"my name is {MainThread.asst_name} and i am your smart assistant.")  
                print(f"my name is {MainThread.asst_name} and i am your smart assistant.")
                aboutKush()
#==============================================OPENING WEBSITE==================================================================================
            elif 'open youtube' in query:
                speak("alright sir opening youtube")
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                speak("Alright  sir opening google")
                webbrowser.open("google.com")
            elif 'open map' in query:
                speak("Alright  sir opening google map")
                webbrowser.open("https://www.google.co.in/maps/@26.7642743,83.2184658,14z?hl=en&authuser=0")
            elif 'open drive' in query:
                speak("Alright  sir opening google drive")
                webbrowser.open("https://drive.google.com/")   
            elif 'open stack overflow' in query:
                speak("Alright  sir opening stack overflow")
                webbrowser.open("stackoverflow.com") 
            elif 'periodic table' in query:
                os.startfile(codePath)
            elif 'open calculator' in query:
                os.startfile("calculator.py")
            elif 'open notepad' in query:
                notepad1()
            elif "hydrogen" in query:
                speak("alright sir opening hydrogen")
                function.H()
                speak("task compleated sir")
            elif "nitrogen" in query:
                speak("alright sir opening nitrogen")
                function.N()
                speak("task compleated sir")
            elif "iron" in query:
                speak("alright sir opening iron")
                function.Fe()
                speak("task compleated sir")
            elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
            elif "close" in query:
                    from Dictapp import closewebapp
                    closewebapp(query)
# ====================================emergency messaging===============================================================  
            elif 'help help' in query:
                emergencyMessage()
#==============================================current time===========================================================================================
            elif 'the time' in query:

                strTime = datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
# ======================================capture image================================================================
            elif 'capture image' in query:
                capture()
#====================================================PERIODIC SECTION======================================================================================
            elif 'thank you' in query:
                speak("welcome pankaj have you nice day")
#========================================================services==============================================================================  
            elif 'write' in query:
                writeParagraph()
 #==================================================APPLICATION EXECUTION===========================================================================               
            elif re.search('launch',query):
                app = query.split(' ', 1)[1]
                path = dict_app.get(app)     #dict_app is a dictory from Feature.py
                if path is None:
                    speak('Application path not found')
                    print('Application path not found')
                else:
                    speak('Launching: ' + app + 'for you sir!')
                    #takeCommand.launch_any_app(path_of_app=path)
                    os.startfile(path)
#=================================================EXIT AND GREETING==============================================================================
            elif "goodbye" in query or "bye" in query:
                speak("Are you sure sir")
                query1=takeCommand().lower()
                if "yes"in query1:
                   speak("Alright sir, going offline. It was nice working with you")
                   sys.exit()
                if "no" in query1:
                    speak("alright sir")
            elif query in GREETINGS:
                speak("always ready for you sir!")
#======================================================SEND MESSAGE=====================================================================================
            elif "send message" in query:
                sendMessage()
#=====================================================TEMPRATURE============================================================================================
            elif "temperature" in query:
                getTemprature()
#=====================================================HOW TO DO MODE===========================================================================================
            elif "activate how to do mode" in query:
                howToDo()
#===================================================QRCODE GENERATOR=============================================================================================
            elif "generate code" in query:
                genQRCode()
#===========================================================INTRODUCTION PART=====================================================================================
            elif "your name" in query:
                print(f"my name is  {MainThread.asst_name} .")
                print(f"my name is  {MainThread.asst_name}")
#=================================================Antisleeping mode===================================================================================
            elif "activate antisleeping mode" in query or "activate driving mode" in query:
               driving_mode()
#====================================================CHANGING ASSTISTANT NAME==============================================================================================
            elif "change name" in query:
                speak("suggest a better name")
                MainThread.asst_name=takeCommand()
                print('name change successfully')
                speak("name change successfully")
#=============================================================CALLING PARTICULAR OF PERIODIC TABLE===================================================================================
            
 #============================================get network speed==============================================
            elif "speed test" in query:
                getnetworkspeed()  
                
#=========================================Screen shot==========================================================
            elif "screenshot" in query:
                speak("Alright sir taking screenshot")
                ss()
            elif "capture image" in query:
                capture()   
            elif "translate" in query:
                translate() 
#===============================shut down your system=================================================
            elif "shutdown system" in query or "shut down system" in query:
                shutdown()  
#=====================================news headline====================================================
            elif "today headline" in query or "today news" in query:
                headlineNews()
#======================================cricket score================================================
            elif "cricket score" in query or "ipl score" in query:
                scoreCard()
#===========================================focus mode===================================================
            elif "activate focus mode" in query:
                speak("alright sir activating focus mode")
                os.startfile("FocusMode.py")
#====================================google search=========================================================
            elif "google" in query or "google search" in query:
                searchGoogle(query)
#========================================youtube search======================================================
            elif "youtube" in query or "youtube search" in query:
                searchYoutube(query)
            elif "schedule my day" in query:
                pass
            elif "book ticket" in query:
                irctc()
            elif "joke" in query or "jokes" in query:
                joke()

#=============================================== GUI PORTION ====================================================================================================
startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("images\live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("images\initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
