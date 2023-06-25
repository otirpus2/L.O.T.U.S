from ast import Pass
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from tqdm import tqdm
import time 

#dictionary(s)
NAME = 'Robuster'
Master = ['Suprito','Parth']
BLACK   = '\033[30m'
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'
       
 
#voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id+ '\n')
engine.setProperty('voice', voices[1].id)

#progress bar
print(GREEN)
for x in tqdm(range(100)):
    time.sleep(0.01)
print(RESET)
print("\n")

def speak(audio):           #Speak Function
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\n")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...\n")

        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...")  
        speak("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('codelyctal@gmail.com', 'whatTHEfuck@4')
    server.sendmail('codelyctal@gmail.com', to, content)
    server.close()


while True:
# if 1:
    query = takeCommand().lower()

    # Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        print("\nSearching Wikipedia..." + GREEN)
        print(RESET)
        try:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak("\nAccording to Wikipedia..." + GREEN)
            print(results)
            speak(results)
        except Exception as e:
            print("No such article found please try again..." + RED)
            print(RESET)
            speak("No such article found please try again\n")
    

    elif 'open youtube' in query:
        speak("Openning YouTube")
        print("Openning YouTube...\n")
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        print("Openning Google...\n")
        speak("Openning Google")
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        print("Openning Stackoverflown...\n")
        speak("Openning Stackoverflown")
        webbrowser.open("stackoverflow.com")   

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")
        print(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        print("Openning VS code...\n")
        speak("Openning VS code")
        os.system('start code')

    elif 'open brave' in query:
        print("Openning Brave...\n")
        speak("Openning Brave")
        os.system('start brave')


    elif 'email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "suprito.eps@gmail.com"    
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak(f"Sorry my friend. I am not able to send this email")   