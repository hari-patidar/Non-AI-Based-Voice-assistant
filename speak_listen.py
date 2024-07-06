import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
    return audio


def takeCommand():
    '''
        This funtion Recognizes and listens to what you say.
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("$$$Listening...$$$")
        r.pause_threshold = 1
        r.energy_threshold = 400
        r.adjust_for_ambient_noise(source)
        audio = r.record(source, duration = 10)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
    return query
