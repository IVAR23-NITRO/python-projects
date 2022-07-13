import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()#the function speak what the strig

print("Initializing shadow....") 
   

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning boss") #this function speak the current time adon 
    elif hour>=12 and hour<18:
        speak("good afternoon boss")
    else:
        speak("good evening boss")

        
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
    except Exception as e:
        print("say that again please")
        query=None
    return query    


wishMe()     
speak("what can i do for you")
query=takecommand()

if 'wikipedia' in query.lower():
    speak('searching wikipedia...')
    query=query.replace("wikipedia","")
    results=wikipedia.summary(query,sentences=2)
    print(results)
    speak(results)
elif 'youtube' in query.lower():
    webbrowser.open("youtube.com")
    
elif 'facebook' in query.lower():
    webbrowser.open("https://www.facebook.com/")

elif 'insta' in query.lower():
    webbrowser.open("https://www.instagram.com/")

elif 'whatsapp' in query.lower():
    webbrowser.open("https://web.whatsapp.com/")
    
elif 'twitter' in query.lower():
    webbrowser.open("https://twitter.com/")

elif 'weather' in query.lower():
    webbrowser.open("weather today")



'''elif 'music'or 'songs'or 'song' in query.lower():
    songs_dir="K:\LOGAN\L-Songs"
    songs=os.listdir("K:\LOGAN\L-Songs")
    os.startfile(os.path.join(songs_dir,songs[0]))'''

    
    
    

