#=============================import all module same as main file========================================
from email import message
from socket import timeout
import subprocess
from turtle import title
from geopy.geocoders import Nominatim
#import pywhatkit
from pyautogui import *
from pyttsx3 import *

import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import time

from datetime import datetime
import cv2  # for camera manupulation
import numpy as np  # for mathmatical operaton
import face_recognition #for identifying your face
#from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Jarvis.features.gui import Ui_MainWindow
from Jarvis.features.func import *
import requests
from bs4 import BeautifulSoup
from pywikihow import WikiHow, search_wikihow
import qrcode
from googletrans import Translator
from playsound import playsound
from gtts import gTTS
from path import *
#===========================================dictonary of lanching app======================================================================================
dict_app = {'chrome':"C:\Program Files\Google\Chrome\Application\chrome",
                'firefox':"C:\Program Files\Mozilla Firefox\Firefox.exe",
                'reader':"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Reader XI.lnk",
                'player':"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN\VLC media player.lnk",
                'paint':"C:\Program Files\WindowsApps\Microsoft.Paint_11.2206.6.0_x64__8wekyb3d8bbwe\PaintApp\mspaint.exe",
                'excel':"D:\smart assistant\JARVIS-master\Res\Excel 2016.lnk",
                'word':"D:\smart assistant\JARVIS-master\Res\Word 2016.lnk",
                'powerpoint':"D:\smart assistant\JARVIS-master\Res\PowerPoint 2016.lnk"
                                }
GREETINGS = ["hello  ", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]
#================================================================take command=================================================================================
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6 #Speech_Recognition engine timeout
        audio = r.listen(source)
        '''Remove this line: r.pause_threshold = 0.6 and try this one instead: r.listen(source,timeout=2).'''
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query
#============================================================open notepad==================================================================================
def notepad1():
    subprocess.Popen("notepad.exe")
def notepad():
    time.sleep(1)
    hotkey('win','r')
    click(327,1708)
    hotkey('ctrl','a')
    hotkey('backspace')
    write("notepad")
    click(405,1945,duration=0.50)
    doubleClick()
#==============================================write any thing===============================================================================================   
def writeParagraph():
    speak("what you want to write ")
    write(takeCommand(),interval=0.25)
    speak("done")
def writeParagraph1():
    write(takeCommand(),interval=0.25)
    speak("done")
#=============================================startup or welcome===============================================================
def startup(a):
    speak(f"Initializing {a}")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
name=""
#=============================================face recgonition unlock==============================================================
def unlock():
    while True:
        name=""
        path="D:\smart assistant\JARVIS-master\images\imgforlock"
        images=[]
        personName=[]
        myList=os.listdir(path)
        #print(myList)
        for cu_img in myList:
            current_Img=cv2.imread(f'{path}/{cu_img}')
            images.append(current_Img)
            personName.append(os.path.splitext(cu_img)[0])
        #print(personName)
#--------------------------------------------------------------------------------------------------------------
        def faceEncodings(images):
            encodeList=[]
            for img in images:
                img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                encode= face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList
        encodeListKnown=(faceEncodings(images))
        print("All encoding complete")


        cap=cv2.VideoCapture(0)


        ret,frame=cap.read()
        faces=cv2.resize(frame,(0,0),None,0.25,0.25)
        faces=cv2.cvtColor(faces,cv2.COLOR_BGR2RGB)

        facesCurrentFrame=face_recognition.face_locations(faces)
        encodesCurrentFrame=face_recognition.face_encodings(faces,facesCurrentFrame)

        for encodeFace,faceloc in zip(encodesCurrentFrame,facesCurrentFrame):
                matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
                faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
                matchIndex=np.argmin(faceDis)
                speak("recognising your face")
                if matches[matchIndex]:
                    name=personName[matchIndex]
                    print(name)
                    #speak(name)
                    #asst_name=name
        if name in personName:
            break
        else:
            speak("face not match")
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(f" hi {name}. you are looking nice. I am your assistant. Please tell me how may I help you")
#============================================antisleeping mode=================================================================
def driving_mode():
    from playsound import playsound
    eye_cascPath = 'haarcascade_eye_tree_eyeglasses.xml'  #eye detect model
    face_cascPath = 'haarcascade_frontalface_alt.xml'  # detect model
    faceCascade = cv2.CascadeClassifier(face_cascPath)
    eyeCascade = cv2.CascadeClassifier(eye_cascPath)

    cap = cv2.VideoCapture(0)
    pagal=0
    while 1:
                    ret, img = cap.read()
                    if ret:
                        frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        # Detect faces in the image
                        faces = faceCascade.detectMultiScale(
                            frame,
                            scaleFactor=1.1,
                            minNeighbors=5,
                            minSize=(30, 30),
                            # flags = cv2.CV_HAAR_SCALE_IMAGE
                        )
                        # print("Found {0} faces!".format(len(faces)))
                        if len(faces) > 0:
                            # Draw a rectangle around the faces
                            for (x, y, w, h) in faces:
                                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            frame_tmp = img[faces[0][1]:faces[0][1] + faces[0][3], faces[0][0]:faces[0][0] + faces[0][2]:1, :]
                            frame = frame[faces[0][1]:faces[0][1] + faces[0][3], faces[0][0]:faces[0][0] + faces[0][2]:1]
                            eyes = eyeCascade.detectMultiScale(
                                frame,
                                scaleFactor=1.1,
                                minNeighbors=5,
                                minSize=(30, 30),
                                # flags = cv2.CV_HAAR_SCALE_IMAGE
                            )
                            if len(eyes) == 0:
                                print('no eyes!!!  \"Press q for exit\"')
                                countdown(5)
                                pagal+=2
                            else:
                                #print('eyes!!!')
                                print("your eye is open   \"Press q for exit\"")
                                pagal=0
                            if pagal>2:
                                file = "alarm_sound.mp3"
                            # print('playing sound using native player')
                                pathi="C:\\Users\\Dell\\Desktop\\ResultantIMG\\alarm_sound.mp3"
                                playsound(pathi)
                                print("abe oo sale mr jayega")
                                cv2.destroyAllWindows()
                            frame_tmp = cv2.resize(frame_tmp, (400, 400), interpolation=cv2.INTER_LINEAR)
                            cv2.imshow('Face Recognition', frame_tmp)
                        waitkey = cv2.waitKey(1)
                        if waitkey == ord('q') or waitkey == ord('Q'):
                            cv2.destroyAllWindows()
                            break
#===============================================timer=================================================================
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

#==========================================exit and minimize fullscreen window===============================================================================
def exitFullscreenWindow():
    click(3788,37,duration=0.20)
def minimizeFullscreenWindow():
    click(3544,38,duration=0.20)
#=============================================abhut kush=============================================================================
def aboutKush():
                speak("i am able to display all periodic table element and lanching any software  in offline mode.")
                print("i am able to display all periodic table element and lanching any software  in offline mode.")
                speak("i have how to do mode to know what you want")
                print("i have how to do mode to know what you want")
                speak("i am able to open any website all over internet and generating qrcode of any message")
                print("i am able to open any website all over internet and generating qrcode of any message")
                speak("i am able to fetch information from wikipidia")
                print("i am able to fetch information from wikipidia")
                speak("we contain some more infomation like current time and temprature.")
                print("we contain some more infomation like current time and temprature.") 
                speak("you can sent message easyly with whatsapp or without whatsapp")
                print("you can sent message easyly with whatsapp or without whatsapp")
                speak("anti sleeping mode or driving mode is also avilable")
#==============================================wikipedia search============================================================================
def wikipedia1():
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
#==========================================send message to me==================================================================================
def sendMessage():
                speak('sir,what should i say')
                msz=takeCommand().lower()
                from twilio.rest import Client
                account_sid = 'AC80d85d88fa1f6cb29e42f733841f2509'
                auth_token = 'f152bca5a48c695835e4c3a53e7131cb'
                client = Client(account_sid, auth_token)
                message = client.messages \
                    .create(
                        body=msz,
                        from_='+19783969589',
                        to='+919532696461'
                    )
                print(message.sid)
                speak("message send succesfully")
#==============================================get environment temprature=============================================================================
def getTemprature():
                search="temperature in gorakhpur"
                url=f"https://www.google.com/search?q={search}"
                r=requests.get(url)
                data=BeautifulSoup(r.text,"html.parser")
                temp=data.find("div",class_="BNeawe").text
                print(f"current {search} is {temp}")
                speak(f"current {search} is {temp}")
#================================================how to do mode=============================================================================
def howToDo():
                speak("how to do mode is activated")
                from pywikihow import search_wikihow
                while True:
                    speak("please tell me what you to know")
                    how=takeCommand().lower()
                    try:
                        if "close" in how or "stop" in how :
                            speak("okey sir , how to do mode is closed")
                            break
                        else:
                            max_results =1 
                            how_to =search_wikihow(how,max_results)
                            assert len(how_to)==1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry sir, i am not able to find this")
#=================================================generate qrcode======================================================================================
def genQRCode():
                speak(f"QR code generating process in progress..   please wait  ")
                speak("what you want to write in QRcode ")
                data=takeCommand()
                img=qrcode.make(data)
                npathi=qrPath
                img.save(npathi)
                speak("image saved successfully")
#=================================================emergency messaging system=====================================================================================
def emergencyMessage():
    address, latlong=currentLocation()
    msz=f"my current location is {address}.\nlatitude and longitude is {latlong}\n Please help me as soon as possible"
    from twilio.rest import Client
    account_sid = 'AC80d85d88fa1f6cb29e42f733841f2509'
    auth_token = 'f152bca5a48c695835e4c3a53e7131cb'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
         body=msz,
         from_='+19783969589',
         to='+919532696461'
                    )
    print(message.sid)
    speak("message send succesfully on your phone")
    # pywhatkit.sendwhatmsg('+919532696461', msz, 18, 52)
# ===================================getLocationByName======================================================================

def getLocationByName(locName):
    # importing geopy library
    
    # calling the Nominatim tool
    loc = Nominatim(user_agent="GetLoc")

    # entering the location name
    getLoc = loc.geocode(locName)

    # printing address
    print(getLoc.address)

    # printing latitude and longitude
    print("Latitude = ", getLoc.latitude, "\n")
    print("Longitude = ", getLoc.longitude)
# ========================================current location====================================================================
def currentLocation():
    geoLoc = Nominatim(user_agent="GetLoc")
    str1="26.7393017,83.269247"
    locname = geoLoc.reverse(str1)
    print(locname.address)
    return locname.address , str1
# =======================================capture image====================================================
def capture():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Image capturing")
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
    cv2.imshow("test", frame)
   # k = cv2.waitKey(1) 
    img_name = "opencv_frame.png"
    cv2.imwrite(capture_img_path, frame)
    # save_path = f"C:\\Users\\Dell\\Desktop\\ResultantIMG\\{img_name}"
    # frame.save(save_path)
    print("{} written!".format(img_name))
    cam.release()
    cv2.destroyAllWindows()
# ================================================network speed========================================================
def getnetworkspeed():
        import speedtest
        s = speedtest.Speedtest()
        s.get_best_server()
        print("checking...")
        d=s.download()
        u=s.upload()
        print(f"your downloading speed is {d}. \nAnd your uploading speed id {u}")
        speak(f"your downloading speed is {d}. \nAnd your uploading speed id {u}")      
#===============================================screenShot==========================================================
def ss():
    from PIL import ImageGrab
    snapshot = ImageGrab.grab()
    snapshot.save(save_path)
    speak("done")
#=================================translator===========================================================
def translate():
    from googletrans import Translator
    from playsound import playsound
    from gtts import gTTS
    speak("ok sir")
    speak("speak sentance")
    query2=takeCommand().lower()
    b="hi"
    translator = Translator()
    translation = translator.translate(query2, dest='hi')
    text=translation.text
    speakg1=gTTS(text=text,lang=b,slow=False)
    pathi=hindiTranslation
    speakg1.save(pathi)
    try:
        speakg1=gTTS(text=text,lang=b,slow=False)
        speakg1.save(pathi)
        playsound(pathi)
        sleep(5)
        os.remove(pathi)
    except:
        speak("unable to translate")
#========================================speak in hindi================================================================
def speakInHindi(text):
        translator = Translator()
        translation = translator.translate(text, dest='hi')
        text=translation.text
        pathi=hindiTranslation
        speakg1=gTTS(text=text,lang='hi',slow=False)
        speakg1.save(pathi)
        playsound(pathi)
        os.remove(pathi)
#================================================shut down==================================================
def shutdown():
    speakInHindi("may i shut down your system?")
    shutdown=takeCommand().lower()
    if shutdown=="yes" or shutdown=="ha" or shutdown=="haa" or shutdown=="han":
        speakInHindi("ok Tata tata bye bye")
        os.system("shutdown /s /t 1")
    if shutdown=="no" or shutdown=="nhi" or shutdown=="nhii" or shutdown=="nahin" or shutdown=="nahi":
        speakInHindi("ok, it doesn't matter")
    else:
        pass
#=================================headline News======================================================
def headlineNews():
    import requests
    from bs4 import BeautifulSoup

    url='https://www.bbc.com/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    ns=""
    for x in headlines:
        speakInHindi(x.text.strip())
        ns+=x.text
#======================================scorecard============================================================
def scoreCard():
    from plyer import notification
    import requests
    from bs4 import BeautifulSoup
    url="https://www.cricbuzz.com/"
    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    team1=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
    team2=soup.find_all(class_="cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
    team1_score=soup.find_all(class_="cb-ovr-flo")[9].get_text()
    team2_score=soup.find_all(class_="cb-ovr-flo")[13].get_text()

    print(f"{team1}: {team1_score}")
    print(f"{team2}: {team2_score}")

    notification.notify(title="CRICKET SCORE:-",
        message=f"{team1}: {team1_score}\n{team2}: {team2_score}",
        timeout=10
        )
#==================================youtube search====================================================================

#=========================================google search========================================================
def scrollUp():
    scroll(-300)
def scrollDown():
    scroll(300)
#==============================================================================================================
def searchYoutube(query):
    speak("This is what i found for your search ")
    query=query.replace("youtube search","")
    query=query.replace("youtube","")
    query=query.replace("jarvis","")
    web="https://www.youtube.com/results?search_query=" +query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done, sir")
def searchGoogle(query):
    
        import wikipedia as googleScrap
        query=query.replace("jarvis","")
        query=query.replace("google search","")
        query=query.replace("google","")
        speak("This is what i found on google")

        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query,1)
            speak(result)
        except :
            speak("No speakable output available")
#====================================Irctc===========================================================================
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

#=====================================joke=============================================================
def joke():
    import pyjokes
    My_joke = pyjokes.get_joke(language="en", category="neutral")
    print(My_joke)
    speakInHindi(My_joke)
#===========================================Recorder==================================================================
def recorder():

    import sounddevice
    from scipy.io.wavfile import write
    fs=44100
    second=int(input("Enter time duration in second:"))
    print("Recording....\n")
    record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
    sounddevice.wait()
    with open("C:/Users/Dell/Desktop/ResultantIMG","w")as file:
        file.write("out.wav",fs,record_voice)
        print("Finished................")
#====================================================Video to audio converter=======================================

def videoToAudio(path):
    import moviepy
    import moviepy.editor
    video=moviepy.editor.VideoFileClip(path)
    audio=video.audio
    newfilename=f"newAudio.mp3"
    audio.write_audiofile(newfilename)

