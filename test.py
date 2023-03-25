
from audioop import add
from winsound import PlaySound
from googletrans import *
from gtts import *
from importlib.resources import path
from Features import * 
import pywhatkit
from playsound import *
from googletrans import Translator
# def Irctc():
#     webbrowser.open("https://www.irctc.co.in/nget/train-search")
#     time.sleep(10)
#     click(1905,1663,duration=0.5)
#     click(475,1044,duration=0.50)
#     speak("source location")
#     # writeParagraph1()
#     write("gorakhpur",interval=0.2)
#     hotkey('enter')
#     click(1232,1374,duration=0.50)
#     click(397,1225,duration=0.50)
#     # writeParagraph1()
#     write("lucknow",interval=0.2)
#     hotkey('enter')
#     tripleClick(1550,1062,duration=0.5)
#     hotkey('backspace')
#     click(1550,1062,duration=0.5)
#     write("31/08/2022")
#     doubleClick(1700,1062,duration=0.5)
#     click(492,1709,duration=0.5)
# # Irctc()
# # print(press("enter"))
# def enterDate():
#     window=Tk()
#     window.title('Enter current Date')
#     lbl=Label(window, text="Enter Journy Date.(dd/mm/yyyy)", fg='black', font=("Comic Sans MS", 16),bg='misty rose')
#     lbl.place(x=20,y=100)
#     txtfld=Entry(window, bd=5)
#     txtfld.place(x=270, y=400)
#     window.geometry("900x800+10+10")
#     window.mainloop()
# # enterDate()
# Irctc()
# program to capture single image from webcam in python

# importing OpenCV library

import cv2


def capture():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Image capturing")
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
    cv2.imshow("test", frame)
   # k = cv2.waitKey(1) 
    img_name = "opencv_frame.png"
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    cam.release()
    cv2.destroyAllWindows()


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
    pywhatkit.sendwhatmsg('+919532696461', msz, 18, 52)

def sendWhatappMessage():
    # hr=datetime.now().hour
    # min=datetime.now().minute+2
    pywhatkit.sendwhatmsg('+919532696461',"msz",20,26)
    # print(type(hr),type(min))
    # type(min)
#sendWhatappMessage()
def getnetworkspeed():
    import speedtest
    st = speedtest.Speedtest()
    st.get_best_server()
    a=st.download()
    print("your downloading speed is",a)
    speak(f"your downloading speed is {a}")
    b=st.upload()
    print("your uploading speed is",b)
    speak(f"your uploading speed is {b}")
# getnetworkspeed()
def click_photo():
    import pyautogui as pg
    pg.hotkey("win")
    pg.sleep(2)
    pg.typewrite("camera")
    pg.hotkey("enter")
    pg.sleep(2)
    speak("smile please")
    pg.sleep(2)
    pg.hotkey("enter")
    os.system(f"taskill /f /im/ camera.exe")
# click_photo()
def translate():
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
def speakInHindi(text):
        translator = Translator()
        translation = translator.translate(text, dest='hi')
        text=translation.text
        pathi=hindiTranslation
        speakg1=gTTS(text=text,lang='hi',slow=False)
        speakg1.save(pathi)
        playsound(pathi)
        os.remove(pathi)
def shutdown():
    speakInHindi("may i shut down your system?")
    shutdown=takeCommand().lower()
    if shutdown=="yes" or shutdown=="ha" or shutdown=="haa":
        speakInHindi("ok Tata tata bye bye")
        os.system("shutdown /s /t 1")
    if shutdown=="no" or shutdown=="nhi" or shutdown=="nhii" or shutdown=="nahin" or shutdown=="nahi":
        speakInHindi("ok, it doesn't matter")
    else:
        pass
def headlineNews():
    import requests
    from bs4 import BeautifulSoup
    import json
    def print_headlines(response_text):
        soup = BeautifulSoup(response_text, 'lxml')
        headlines = soup.find_all(attrs={"itemprop": "headline"})
        for headline in headlines:
            print(headline.text)
            speakInHindi(headline.text)
    url = 'https://inshorts.com/en/read'
    response = requests.get(url)
    print_headlines(response.text)
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

def recorder():

    import sounddevice
    from scipy.io.wavfile import write
    fs=44100
    second=int(input("Enter time duration in second:"))
    print("Recording....\n")
    record_voice=sounddevice.rec(int(second*fs),samplerate=fs,channels=2)
    sounddevice.wait()
    write("out.wav",fs,record_voice)
    print("Finished................")


def videoToAudio(path):
    import moviepy
    import moviepy.editor
    video=moviepy.editor.VideoFileClip(path)
    audio=video.audio
    newfilename=f"newAudio.mp3"
    audio.write_audiofile(newfilename)

def speakInHindi(text):
        translator = Translator()
        translation = translator.translate(text, dest='hi')
        text=translation.text
        pathi=hindiTranslation
        speakg1=gTTS(text=text,lang='hi',slow=False)
        speakg1.save(pathi)
        playsound(pathi)
        os.remove(pathi)
headlineNews()