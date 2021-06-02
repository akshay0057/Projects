import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import platform
import os
import random
import subprocess
import googlesearch


engine = pyttsx3.init('sapi5') ''' sapi5 provide the voice , sapi5=>windows, nsss=>mac,
espeak => every oter platform'''
voices = engine.getProperty('voices')  ''' There are two voices in the system first is male voice
and second is feamle voice
#print(voices[0].id)  # This is male voice (DAVID VOICE)
#print(voices[1].id) # Tis is female voice (ZIRA VOICE)'''
engine.setProperty('voice', voices[1].id,) # Here we set voice
engine.setProperty('rate', 200) # set the voice rate

def speak(audio):
    '''
    This function takes the input as audio and speak them
    '''
    engine.say(audio)
    engine.runAndWait() # While other process is executing till it wait

def wish():
    '''
    This function is used to wish to the user, according to the current date and time
    '''
    hour = int(datetime.datetime.now().hour) # This will tell you current time in hour (0-24)
    if hour < 12:
        speak('Good Morning!')
    elif hour <= 17:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('Please tell, how may i help you?')

def takeCommand():
    # take audio from the user with microphone and convert it into a string

    r = sr.Recognizer() # Recognizer is a class which help to recognige audio
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try: # try is used for an error
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User Said : {query}\n')
    except Exception as e:  # e is a error
        print('Say that again please...')
        return  'None' # if there is any problem in listening then it return None string

    return query

if __name__ == "__main__":
    speak('Hey, i am jarvis.')
    wish()
    while True:
        query = takeCommand().lower()
        #webbrowser.open(str(googlesearch.search(query, num = 1, stop = 1, pause = 1)))
        '''
        a = googlesearch.search(query, num = 1, stop = 1, pause = 1)
        a = list(a)
        webbrowser.open(a[0])
        '''    
        if 'about yourself' in query:
            speak('Hii, I am Jarvis. J.A.R.V.I.S. (Just A Rather Very Intelligent System) is a fictional artificial intelligence that first appeared in the Marvel Cinematic Universe where he was voiced by Paul Bettany in Iron Man, Iron Man 2, The Avengers, Iron Man 3, and Avengers: Age of Ultron.')
            
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('google')

        elif "open python" in query:
            webbrowser.open("http://www.python.org")

        elif "system information" in query or 'about system' in query:
            system_info = platform.uname()
            print(f"Operating System Name: {system_info.system}")
            speak(f"The windows install in this system is ,{system_info.system}")

            print(f"Version : {system_info.version}")
            speak(f"and its version is ,{system_info.version}")

            print(f"Machine Name: {system_info.node}")
            speak(f"The name of this system is ,{system_info.node}")

            print(f"Machine Type: {system_info.machine}")
            speak(f"and its type is ,{system_info.machine}")

            print(f"Processor : {system_info.processor}")
            speak(f"and finally the system processor is ,{system_info.processor}")

        elif "play music" in query:
            music_dir = "D:\\video songs"
            songs = os.listdir(music_dir)
            indexOfSong = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[indexOfSong]))

        elif "open calculator" in query:
            calc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')

        elif 'close calculator' in query:
            calc.kill()

        elif 'open notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

        

        
            
            

