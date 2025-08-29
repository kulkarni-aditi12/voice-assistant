import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, service is unavailable.")
            return ""

def handle_command(command):
    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "netflix" in command:
        speak("Opening Netflix")
        webbrowser.open("https://www.netflix.com")
    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return False
    else:
        speak("Command not recognized.")
    return True

def run_assistant():
    speak("Hi! I am your assistant. What would you like to do?")
    while True:
        command = listen()
        if command:
            if not handle_command(command):
                break

run_assistant()
