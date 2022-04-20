#Virtual Assistance

import pyttsx3            #pip install pyttsx   #pip install pyttsx3
import speech_recognition as sr      #pip install speech_recognition
import datetime
import wikipedia       #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!") 

    v= "Jarvis -A virtual Asistant"
    print("\n\n\t\t\t\t"+v) 
    speak("I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        speak("Pardon, Say that again please...") 
        print("Pardon, Say that again please...") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ravi***@gmail.com', 'your-password')
    server.sendmail('ravi***@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:                                             # to open youtube
            webbrowser.open("youtube.com")

        elif 'open google' in query:                                               # to open google
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:                                        # to open stackoverflow
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:                                              # to open github
            webbrowser.open("www.github.com")

        elif 'about yourself' in query:
            speak('Hello , what would you like to know about myself')               #about jarvis @tell me about yourself..
            d={'Name' : 'People call me Genius but my name is jarvis',
            'Age' : 'I was programmed in jan 2022 but I am still as smart as Gentleman and as childish as a small baby. ',
            'Yourself' : 'Hello I am your virtual assistance. I am programmed by my boss Mister Abhishek in VS code environment. You can call me Jarvis. I can help you to complete your task on your voice command.'
            }
            while True:
                content = takeCommand().lower()
                if 'name' in content:
                    speak(d['Name'])
                elif 'age' in content:
                    speak(d['Age'])
                elif 'what can you do' in content:
                    speak(d['Yourself'])
                elif 'ok thank you' in content:
                    break 

        elif 'play music' in query:                                              # to play music
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'          # dir location
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:                                                # to check system time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'restart this system' in query:                             #to restart this system
            speak("Do you really want to restart this system")
            content = takeCommand()
            if content == "yes":
                os.system("shutdown /r /t 1")
            else:
                break

        elif 'shut down this system' in query:                            #to shutdown this system
            speak("Do you really want to turn off this system")
            content = takeCommand()
            if content == "yes":
                os.system("shutdown /s /t 1")
            else:
                break        

        elif 'open code' in query:                                          #to close vs code
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to me' in query:                                       # to send mail
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"                #receivers address
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this mail") 

        elif 'thank you' in query:
            speak("welcome, I'm honoured to serve...... jarvis is going to sleep")
            exit()           
