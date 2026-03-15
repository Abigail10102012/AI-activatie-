import speech_recognition as sr
import pyttsx3
import datetime
import random

# Initialize speech engine
engine = pyttsx3.init()

# Store user name
user_name = None

# Default voice
voices = engine.getProperty('voices')
current_voice = voices[0].id
engine.setProperty('voice', current_voice)

# Facts list
facts = [
    "Octopuses have three hearts.",
    "Bananas are technically berries.",
    "The Eiffel Tower can grow taller in summer due to heat expansion.",
    "Honey never spoils and can last thousands of years.",
    "Sharks existed before trees."
]


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()

        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please try again.")
            return None

        except sr.RequestError:
            speak("Speech service is unavailable.")
            return None


def process_command(command):
    global user_name, current_voice

    if command is None:
        return

    # 1. Date command
    if "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today is {today}")

    # 2. Store name
    elif "my name is" in command:
        user_name = command.replace("my name is", "").strip().title()
        speak(f"Nice to meet you, {user_name}!")

    elif "hello" in command:
        if user_name:
            speak(f"Hi {user_name}! How can I help you?")
        else:
            speak("Hello! How can I help you?")

    # 3. Fact command
    elif "fact" in command:
        fact = random.choice(facts)
        speak(fact)

    # 4. Voice customization
    elif "use male voice" in command:
        engine.setProperty('voice', voices[0].id)
        speak("Switched to male voice.")

    elif "use female voice" in command:
        engine.setProperty('voice', voices[1].id)
        speak("Switched to female voice.")

    else:
        speak("Sorry, I don't recognize that command.")


def main():
    speak("Voice assistant started. Say a command.")

    while True:
        command = listen()
        process_command(command)


if __name__ == "__main__":
    main()