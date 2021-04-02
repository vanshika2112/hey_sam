import pyttsx3 #python module, used to convert text to speech
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from PIL import Image

engine = pyttsx3.init('sapi5') #Speech Recoginition API by microsoft
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id) # 1 for female voice and 0 for male voice

def speak(audio):
    ''' To make Sam speak what we want '''
    engine.say(audio)
    engine.runAndWait() #it stops the other processes for some time, so that we can hear what sam is saying

def wishme():
    ''' For Greeting the user '''
    h = int(datetime.datetime.now().hour)
    if h<12:
        speak("Good Morning, Let me know what is to be done.")
    elif h>12 and h<17:
        speak("Good Afternoon, Let me know what is to be done.")
    else:
        speak("Good Evening, Let me know what is to be done.")

def takeCommand():
    ''' Converts our given command to string '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # pause taken by the user while completing a phrase.
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

  
if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching in the Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Hey, the current time is {strTime}")   

        else:
            break 
        
    