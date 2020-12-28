import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
from gtts import gTTS
import playsound
import os

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():

    try:
        with sr.Microphone() as source:
            print('আমি শুনতেছি আপনি বলুন.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Ekhon somoy' + time)

    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'group  ' in command:
        tts = gTTS(text='হ্যাঁ আমি সবাইকে ধন্যবাদ জানাচ্ছি হ্যালো বন্ধুরা তোমাদের সবাইকে আমার পক্ষ থেকে ধন্যবাদ', lang='bn')
        tts.save("g.mp3")
        os.system("mpg321 g.mp3")
        playsound.playsound('g.mp3', True)


    elif 'game' in command:
        tts = gTTS(text='আমি তোমার সাথে ব্যাডমিন্টন খেলতে চাই ', lang='bn')
        tts.save("goo.mp3")
        os.system("mpg321 goo.mp3")
        playsound.playsound('goo.mp3', True)

    elif 'bangabandhu' in command:
        tts = gTTS(text='শেখ মুজিবুর রহমানের জন্ম ১৯২০ সালের ১৭ই মার্চ গোপালগঞ্জের টুঙ্গিপাড়ায়।', lang='bn')
        tts.save("l.mp3")
        os.system("mpg321 l.mp3")
        playsound.playsound('l.mp3', True)

    elif 'aunty' in command:
        tts = gTTS(text='হ্যাঁ সুমা আন্টিকে আমি চিনি তার হবু বরের নাম পললোব', lang='bn')
        tts.save("go.mp3")
        os.system("mpg321 go.mp3")
        playsound.playsound('go.mp3', True)

    elif 'ki' in command:
        tts = gTTS(text='হ্যা, ঝংকার মাহবুব একজন প্রোগ্রামার, ইউটিউবার, লেখক। উনার লাইফের উল্লেখযোগ্য অর্জনের মধ্যে অন্যতম হচ্ছে-- ক্লাস সেভেনে থাকার সময়, স্ট্যান্ডআপ কমেডিতে দ্বিতীয় স্থান দখল', lang='bn')
        tts.save("m.mp3")
        os.system("mpg321 m.mp3")
        playsound.playsound('m.mp3', True)


    else:
        tts = gTTS(text='এই তথ্যটি আমার কাছে নেই আমাকে একটু সময় দিন আমি গুগলে সার্চ করে দেখছি ', lang='bn')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        playsound.playsound('good.mp3', True)
        pywhatkit.search(command)

while True:
    run_alexa()
