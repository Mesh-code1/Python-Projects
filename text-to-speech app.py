import speech_recognition as sr
import pyttsx3

# initialize the speech recognizer
r = sr.Recognizer()

# initialize the text-to-speech engine
engine = pyttsx3.init()

# set the voice to use
engine.setProperty('voice', 'english')

while True:
    # get input from the user
    text = input("Enter some text (or 'q' to quit): ")

    # exit if the user enters 'q'
    if text == 'q':
        break

    # convert the text to speech
    engine.say(text)
    engine.runAndWait()