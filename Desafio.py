
from gtts import gTTS
from IPython.display import Audio
import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser
import winshell
from pygame import mixer
from time import sleep







# ================================================================================
# get mic audio

def get_audio():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.pause_threshold = 1

        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(source)

        whatYouSaid = ""

        try:

           whatYouSaid = r.recognize_google(audio)
           print(whatYouSaid)

        except sr.UnknownValueError:
            # speak("Sorry, I did not get that.")
            print("Sorry, I did not get that.")

        except sr.RequestError:
            # speak("Sorry, the service is not available")
            print("Sorry, the service is not available")

    return whatYouSaid.lower()


# ================================================================================
# speak converted audio to text

def speak(text, filename):

    tts = gTTS(text=text, lang='en')

    #filename = "voice.mp3"

    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)

    playsound.playsound(filename)


# ================================================================================
# ROTINA PRINCIPAL

def main():

    global whatYouSaid

    # Mensagem de boas-vindas
    print("Welcome!")

    # Áudio de boas-vindas
    speak("Welcome, I´m listening!", "welcome.mp3")

    counter = 0;

    while True:

        # Mensagem
        print("\n\nI am listening ... ", counter)
        
        # Captura audio e reconhece
        text = get_audio()

        print("What I understood: ", text)
        # print(whatYouSaid)
        # respond(text)

        # Encerra o loop
        if 'exit' in text:
            break

        # Joke
        if 'joke' in text:
           speak(pyjokes.get_joke(), "voice.mp3")

        # Proximo loop
        counter+= 1

    print('Encerrado')


# ================================================================================
# MAIN

if __name__ == "__main__":
    main()
