import pyttsx3
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import webbrowser as wb

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    list1 = ['at your service sir', 'for you sir, always', 'as always sir, a great  pleasure watching you work']
    speak(list1[random.randint(0, len(list1) - 1)])


def end():
    list2 = ['all wrapped up here, sir', 'enjoy yourself, sir', 'as always sir, a great  pleasure watching you work']
    speak(list2[random.randint(0, len(list2) - 1)])


def who_r_u():
    speak('Alexa')


def takecomand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said {query}')
        print('aaaaaaaaaaaaaaa')
        return query
    except Exception as e:
        print(e)
        print('please say again')
        return 'None'


if __name__ == '__main__':

    wishme()
    t = 0

    while True:
        query = takecomand().lower()
        print(query)

        if query == 'none':
            t += 1
            print(t)
            if t == 30:
                exit()

        elif 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=1)
            speak('according to wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query:
            wb.open('youtube.com')

        elif 'play my playlist' in query:
            wb.open('')

        elif 'open google' in query:
            wb.open('google.com')

        elif 'play songs' in query:
            movies = '...'  # Enter link to open
            speak('Enjoy the music sir')
            wb.open(movies)  # can use random

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir, the time is {strtime}')

        elif 'open file' in query:
            codepath = 'c:\\..............................'
            os.startfile(codepath)

        elif 'open gmail' in query:
            wb.open('...')  # Enter your prefered E-mail ID

        elif 'who are you' in query:
            who_r_u()
        elif 'quit' or 'stop' in query:
            end()
            exit()

        else:
            pass
        t = 0
