import pyttsx3
import speech_recognition as sr
import webbrowser as web
import datetime
import os
import cv2
from requests import get
import wikipedia
import requests


engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# print(voices[0],id)
# engine.setProperty('voices',voices[0].id)d

def speak(audio):
    engine.setProperty('rate',130)
    engine.say(audio)
    engine.runAndWait()
    
# if __name__ == "__main__":
#     speak("THIS IS JARVIS...HELLO")

def take_Integer_input():
    r = sr.Recognizer()
    a = True
    while(a):
        
        with sr.Microphone() as source:
            speak("speak the input")
            try:
                r.pause_threshold = 5
                audio = r.listen(source , timeout=5, phrase_time_limit=5)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for speech.")
                continue
        
        try:
            
            if audio:
                print("recognizing...")
                query3 = r.recognize_google(audio, language='en-in')
                query3 = query3.lower()
                
                print(f"you said:{query3}")
                if("one" in query3 or "1" in query3):
                    return 1
                if("two" in query3):
                    return 2
                if("three" in query3):
                    return 3
                if("four" in query3):
                    return 4
                if("five" in query3):
                    return 5
                if("one hundred" in query3):
                    return 100
                if("exit" in query3):
                    a = False
                # else:
                    # if query3.isdigit():
                    #     print(f"user said:{query3}") 
                    #     return int(query3)
                    
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold = 5
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source , timeout=10, phrase_time_limit=5)
                
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")  
        # speak(query)
    
    
    # except sr.UnknownValueError:
    #     print("Sorry, I did not understant that.")
    #     return None
    
    except sr.RequestError:
        print("Service is unavailable.")
        return None
    
    except sr.WaitTimeoutError:
        return None
    
        
    except Exception as e:
        speak("anything else?")  
        return "none"        
    
    return query

def setting_menu():
    
    while True:
        speak("what would you like to change from 1 to 5")
        print("\n--- JARVIS Settings ---\n")
        print("1. Change Speech Rate\n")
        print("2. Change Volume\n")
        print("3. Change Input Device\n")
        print("4. Change Output Device\n")
        print("5. Exit Settings\n")
        
        speak("speak your choice from 1 to 5")
        # choice = input("Enter your choice (1-5): ")
        
        choice = take_Integer_input()
        
        if choice == 1:
            rate = engine.getProperty('rate')
            print(f"Current Speech Rate is {rate}")
            speak(f"Current Speech Rate is {rate}")
            speak("enter new speech rate. the defaulf rate is 200")
            # new_rate = int(input("Enter new Speech Rate (default is 200): "))
            
            rateInput = int(take_Integer_input())
            
            
            engine.setProperty('rate', rateInput)
            print(f"Speech Rate set to: {rateInput}")

def webbrowsing():
    path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        
        print("Please say something...")
        
        audio = r.listen(source)
        
        print("LISTENING...")
        
        try:
            dest = r.recognize_google(audio)
            print("You have said : "+dest)
            
            web.get(path).open(dest)
            
        except Exception as e:
            print("Error :"+str(e))
            
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if(hour >=0 and hour <=12):
        speak("GOOD MORNING SIR")
    elif(hour > 12 and hour <=18):
        speak("GOOD AFTERNOON SIR")
    else:
        speak("GOOD EVENING SIR")
    speak("JARVIS IS HERE FOR YOU....PLEASE TELL..HOW CAN I HELP YOU...")
    
def ask_chatgpt(prompt):
    api_key = "sk-e6DqKTrRDtAJc37yLI1u8zReYDuXeAzuiM5vTVrUXyT3BlbkFJuAHAJqne0NJRKNdMiMFVlj-_LGfZV5QAuDAURXew8A"  # Replace with your OpenAI API key
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",  # Specify the model you want to use
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150  # Adjust the max tokens as needed
    }
    
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error: Unable to get response from ChatGPT."
    

if __name__ == "__main__":
    wish()
    
    while True:
        
        query = takecommand().lower()
        
        if "engine setting" in query:
            setting_menu()
        
        if query is None:
            continue
        
        if "open notepad" in query:
            path = "C:\\Windows\\notepad.exe"
            speak("there you go sir")
            os.startfile(path)
            
        if "chat" in query:  # Assuming you want to trigger ChatGPT with the word "chat"
            speak("What do you want to ask ChatGPT?")
            user_question = takecommand()  # Capture user input
            
            if user_question:
                response = ask_chatgpt(user_question)
                speak(response)  # Speak out the response
                
        elif "now you can exit" in query:
            speak("okay sir...have a nice day")
            break
        
        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("according to wikipedia")
            speak(results)