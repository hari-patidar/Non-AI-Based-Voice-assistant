from speak_listen import *
from internet_connection import *
from wish_me import *
from response import *
from tkinter import *
from general_answers import *

if __name__ == "__main__":
    wishMe()
    internet = check_internet()

    if internet == True:
        speak("Successfully connected to internet...")
    elif internet == False:
        speak("Unable to connect to internet! Please check your connection...")

    x = 1
    while x == 1:
        speak("Listening..")
        Query = takeCommand()
        if len(Query) == 0:
            continue
        query = Query.lower() 
        response = response_logic(query)
        speak(response)
        if response in ["Good Bye sir, See you soon.", "I hope that i was of some help.", "Come back soon sir"]:
            x = 0
