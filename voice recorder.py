from os import name
from gtts import gTTS
import os
import speech_recognition as sr
r = sr.Recognizer() # making a object named r which is the recognizer

if __name__ == "__main__":
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        title = input("Enter the file title: ")
        file = gTTS(query) # makes the file
        file.save(f'{title}.mp3')# saves the file
        os.startfile(f'{title}.mp3') # opens the file
    except Exception as w:
        print(w)

    