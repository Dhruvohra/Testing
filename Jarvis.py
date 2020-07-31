import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import random
import requests
import sys
import os

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices)
#print(voices[1].id)
engine.setProperty("voice",voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <=12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    elif hour>=18 and hour<=21:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    
    speak("Hi My name is Jarvis Sir, How may i help You ?")

def TakeCommand():
    #This takes input from microphone and gives string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognising....")
        query=r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")
    
    except Exception:
        #print(e)
        print("Say that again please:")
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jhontyvohra@gmail.com', 'Jhonty@23')
    server.sendmail('jhontyvohra@gmail.com', to, content)
    server.close()


def givenews():
    apiKey = '49e391e7066c4158937096fb5e55fb5d'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}"
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 10:
            break
        print(items["title"])
        to_speak = items["title"].split(" - ")[0]
        if flag:
            speak("Today's top ten Headline are : ")
            flag = False
        else:
            speak("Next news :")
        speak(to_speak)


def clear():
    # To clear the console after each command
    _ = os.system('cls')

if __name__ == "__main__":
    WishMe()

    while True:
        query=TakeCommand().lower()

        #logics for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open yahoo" in query:
            webbrowser.open("yahoo.com")

        elif "open FB" in query:
            webbrowser.open("facebook.com")
s
        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "what\'s up" in query or 'how are you' in query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
                speak(random.choice(stMsgs))

        elif "play songs" in query:
            music_dir = "C:\\Users\\DHRUV VOHRA\\Music"
            songs=os.listdir(music_dir)
            print(songs)
            #random_music = music_folder + random.choice(music) + '.mp3'
            #k=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs)-1)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            code_path="C:\\Users\\DHRUV VOHRA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif "email me" in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                to = "nishtha.aggarwal23@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                    #print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 
                
        elif 'headlines' in query or 'news' in query or 'headline' in query:
            givenews()

        elif 'jarvis quit' in query or 'exit' in query or 'close' in query:
            speak("Thanks for using Jarvis!!!")
            exit()

        elif 'awesome' in query or 'wow' in query or 'amazing' in query or 'wonderful' in query:
            speak("Thank you sir, i am here for you")

        elif 'what' in query or 'who' in query or 'where' in query or 'can you' in query:
            webbrowser.open(f"https://www.google.com/search?&q={query}")
            speak(wikipedia.summary(query, sentences=2))

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        else:
                query = query
                speak('Searching...')
                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        speak('WOLFRAM-ALPHA says - ')
                        speak('Got it.')
                        speak(results)
                        
                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak('Got it.')
                        speak('WIKIPEDIA says - ')
                        speak(results)
            
                except:
                    webbrowser.open('www.google.com')
            
        speak('Next Command! Sir!')