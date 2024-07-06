import datetime, wikipedia, webbrowser, os, random
from speak_listen import *
from internet_connection import *
from wish_me import *
from general_answers import *

def response_logic(query):
    response = about_me(query)
    speak(response)
    response = condition(query)
    speak(response)
    
    if 'hello' in query or 'hi' in query:
        responses = ["Hello sir, How can i help you?", 'Hi; Welcome back sir.', 'Namaskar', 'Raam Raam']
        response = random.choice(responses)

    elif 'wikipedia' in query:
        speak('Searching Wikipedia....')
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia")
        response = results
    
    elif 'youtube' in query or 'Youtube' in query or "YouTube" in query:
        q = query.split("youtube")[0]
        webbrowser.open(f"https://www.youtube.com/results?search_query={q}")
        response = "Loading the webpage on your default browser."

    elif 'google' in query or 'web' in query or 'internet' in query or "Google" in query:
        q = query.split("google")[0]
        webbrowser.open(f"https://www.google.co.in/search?q={q}")
        response = 'Loading the webpage on your default browser.'

    elif 'email' in query:
        webbrowser.open("gmail.com")
        response = 'Loading the webpage on your default browser.'

    elif "music" in query:
        path = "C:\\Users\\Hitso\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(path)
        response = 'Opening music player for you.'

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {strTime}"

    elif ('check internet' in query) or ('connection' in query):
        internet = check_internet()

        if internet == True:
            response = "Successfully connected to internet..."
        elif internet == False:
            response = "Unable to connect to internet! Please check your connection..."
            
    elif 'bye' in query or 'exit' in query:
        responses = ["Good Bye sir, See you soon.", "I hope that i was of some help.", "Come back soon sir"]
        response = random.choice(responses)
        exit(1)
    
    else:
        response = "Unable to get that please repeat your query."

    return response
