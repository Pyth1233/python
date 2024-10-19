import speech_recognition as sr
import pyttsx3
import pywhatkit

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',130)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak('hello,there I am your voice assistant,How are you')

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('listening')
    audio= r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if 'what' and 'about' and 'you' in text:
    speak('i am also having good day')

speak('what can i do for you???')

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None

def main():
    speak("ask me anything!.")
    
    while True:
        command = listen()

        if command is None:
            continue

        command = command.lower()

        if 'play' in command:
            song = command.replace('play', '').strip()
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'stop' in command:
            speak("Goodbye!")
            break

        else:
            speak("I can only play songs. Please ask me to play something.")

if __name__ == "__main__":
    main()
