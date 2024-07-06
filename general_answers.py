import random
from speak_listen import *
from response import *

def about_me(query):
    response = ''
    questions = ['who are you', 'tell me about you', 'what is your name', 'who created you']
    for question in questions:
        if question in query:
            response = "I am virtual assistance. I can do many things which can make your work easier."
            break
    return response

def condition(query):
    response = ''
    questions = ['how are you', 'what are you doing', "what's up", "what's going"]
    for question in questions:
        if question in query:
            responses = ['Nothing just here to help you.', 'I am doing well. What about you', 'Great', 'Just fine. Tell me to do some work']
            response = random.choice(responses)
            break
    return response
        
