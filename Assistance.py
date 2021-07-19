import speech_recognition as sr
from time import ctime
import time
from gtts import gTTS
import playsound
import os
import random
import webbrowser




r = sr.Recognizer()  # recognizer

# record audio andreturn as string
def recordAudio(ask=False):
    with sr.Microphone(device_index=0) as source:
        if ask:
            groot_speak(ask)
        audio = r.listen(source, timeout=1, phrase_time_limit=2)
        # google speech recognition
        voice_data=' '
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            groot_speak("unknown error")
        except sr.RequestError:
            groot_speak('request error')
        return voice_data


def groot_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,100000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# return data in audio
def responce(voice_data):
    if 'what is your name' in voice_data:
        groot_speak('My name is groot')
    if 'what time is it' in voice_data:
        groot_speak(ctime()) 
    if 'search' in voice_data:
        search=recordAudio('what do u want to search')
        url='https://google.com/search?q='+ search 
        webbrowser.get().open(url)
        groot_speak('here is what i found for '+ search)   
    if 'location' in voice_data:
        location=recordAudio('what is the location')
        url='https://google.nl/maps/place/'+ location +'/&amp;' 
        webbrowser.get().open(url)
        groot_speak('here is the location '+ location) 
    if 'exit' in voice_data:
        groot_speak("  By have a nice day, I am GROOT")
        exit()     


time.sleep(1)
groot_speak('How can i help you')
while 1:
    voice_data=recordAudio()
    responce(voice_data)
