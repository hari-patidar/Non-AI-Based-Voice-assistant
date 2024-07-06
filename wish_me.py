import datetime, random
from time import strftime
from speak_listen import *

def initialize():
    responses = ["Establishing all required connections", "Correcting previous errors", "Setting up environment", "Configuring all data", "Initializing.", 'Recovering log files.', 'configuring memory chunks;:', 'opening required ports, and connecting them.']
    for i in range(3):
        speak(random.choice(responses))
    speak('status : active.')

def wishMe():
    responses = ['Hello', 'Namaste', 'Hii How is your day going.']
    speak(random.choice(responses))
    
    hour = int(datetime.datetime.now().hour)
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    minute = int(datetime.datetime.now().minute)
    formated_month = datetime.datetime(year, month, day)
    selected_month = formated_month.strftime("%b")


    speak(f"Today is {day} {selected_month} {year}")
    speak(f"and current time is {hour} hours {minute} minutes")

def guide():
    speak("I am here to assis you and make your work easy.")
    speak("To open and search any file i have two modes.")
    speak("Explore mode; and Open mode")
    speak("In Explore mode, i will work according to your commands.")
    speak("And in open mode i will try to search the file by myself. But it may be give little error.")
    speak("And for going on World Wide Web;")
    speak("You must say search or web in your command.")

