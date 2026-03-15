import speech_recognition as sr
import pyttsx3
from googletrans import Translator

engine = pyttsx3.init()
translator = Translator()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak in English...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", text)
        return text

    except:
        print("Speech not recognized")
        return ""

def translate_text(text, target):
    translated = translator.translate(text, dest=target)
    return translated.text

def choose_language():

    languages = {
        "1":"hi",
        "2":"ta",
        "3":"te",
        "4":"bn",
        "5":"mr",
        "6":"gu",
        "7":"ml",
        "8":"pa",
        "9":"fr",
        "10":"nl",
        "11":"ko",
        "12":"ja"
    }

    print("1 Hindi")
    print("2 Tamil")
    print("3 Telugu")
    print("4 Bengali")
    print("5 Marathi")
    print("6 Gujarati")
    print("7 Malayalam")
    print("8 Punjabi")
    print("9 French")
    print("10 Dutch")
    print("11 Korean")
    print("12 Japaneese")

    choice = input("Select language: ")

    return languages.get(choice,"fr")

def main():

    target = choose_language()

    text = speech_to_text()

    if text:

        translated = translate_text(text,target)

        print("Translated:",translated)

        speak(translated)

main()