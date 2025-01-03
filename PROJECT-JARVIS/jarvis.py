import pyttsx3
import speech_recognition as sr
import webbrowser as web
import datetime
import os
import cv2
from requests import get
import wikipedia


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
        
        speak("Please say what you want to search...")
        
        audio = r.listen(source)
        
        print("LISTENING...")
        
        try:
            dest = r.recognize_google(audio)
            print("You have said : "+dest)
            
            if dest.startswith("http"):
                url = dest
            else:
                url = "https://www.google.com/search?q=" + dest
                
            
            web.get(path).open(url)
            
        except Exception as e:
            print("Error : some error occured"+str(e))
            
def wish():
    hour = int(datetime.datetime.now().hour)
    
    if(hour >=0 and hour <=12):
        speak("GOOD MORNING SIR")
    elif(hour > 12 and hour <=18):
        speak("GOOD AFTERNOON SIR")
    else:
        speak("GOOD EVENING SIR")
    speak("JARVIS IS HERE FOR YOU....PLEASE TELL..HOW CAN I HELP YOU...")
    
    

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
            
        elif "speak the same" in query:
            r = sr.Recognizer()
            a = True
            while(a):
                
                with sr.Microphone() as source:
                    speak("WHAT YOU WANT ME TO REPEAT")
                    try:
                        audio = r.listen(source , timeout=5, phrase_time_limit=5)
                    except sr.WaitTimeoutError:
                        print("Listening timed out while waiting for speech.")
                        continue
                
                try:
                    
                    if audio:
                        query3 = r.recognize_google(audio, language='en-in')
                        print(f"user said:{query3}") 
                        query3 = query3.lower()
                        
                        if("exit" in query3):
                            a = False
                        else:
                            speak(query3)
                            
                except sr.UnknownValueError:
                    print("Sorry, I didn't catch that. Please try again.")
                    speak("Sorry, I didn't catch that. Please try again.")
                    
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")
                    speak(f"Could not request results from Google Speech Recognition service; {e}")
            
        elif "open brawlhalla" in query:
            path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Brawlhalla\\BrawlhallaEAC.exe"
            path2 = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Brawlhalla\\Brawlhalla.exe"
            speak("there you go")
            os.startfile(path)
            os.startfile(path2)
            
        elif "open this PC" in query:
            path = "C:\\Users\\kashi\\OneDrive\\Desktop\\This PC.lnk"
            speak("there you go")
            os.startfile(path)
            
        elif "open discord" in query:
            # path = "C:\\Users\\kashi\\AppData\\Local\\Discord\\Update.exe"
            path = "C:\\Users\\kashi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk"
            speak("there you go")
            os.startfile(path)
            
        elif "open word" in query or "can you open word" in query:
            if query == "can you open word":
                speak("sure sir")
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("there you go")
            os.startfile(path)
            
        elif "open excel" in query:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            speak("there you go")
            os.startfile(path)
            
        elif "open command prompt" in query:
            os.system("start cmd")
            speak("there you go")
            
        elif "open browser" in query:
            speak("What you want to search... i will search it for you")
            query2 = takecommand().lower()
            if "no thanks" in query2:
                path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(path)
            elif "there is one thing" in query2 or "i want to search" in query2 or "search one thing" in query2:
                webbrowsing()
                
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            
            # custom_path = "C:\\Users\\kashi\\Pictures\\"
            
            while True:
                
                ret, frame = cap.read()
                
                if ret:
                    # a = True
                    # while a:
                        
                        cv2.imshow('WEBCAM',frame)
                        
                        # query2 = takecommand().lower()
                        # if "close camera" in query2:
                        #     speak("DONE sir")
                        #     break
                        
                        #koi bhi key press hogi toh usko check krega->
                        key = cv2.waitKey(1) & 0xFF
                        
                        
                            
                        # query2 = takecommand()  # Listen for a command
                        
                        # if "take snapshot" in query2:
                        if(key == ' '):
                            snapshot_filename = "snapshot.png"
                            cv2.imwrite(snapshot_filename,frame)
                            print(f"Snapshot taken and saved as {snapshot_filename}")
                            speak(f"Snapshot taken and saved as {snapshot_filename}")
                            
                            
                        # if "close camera" in query2:
                        if(key == 'q'):
                            speak("Closing the camera.")
                            a = False
                    
                        # Check for 'q' key to exit
                        # if key == ord('q'):
                        #     break
                                
                else:
                    break

            cap.release()
            cv2.destroyAllWindows()
            
        elif "show my ip address" in query:
            ip = get('https://api.ipify.org').text
            print(ip)
            speak(f"your IP address is {ip}")
            
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
        
        elif "open youtube"  in query:
            urlYoutube="www.youtube.com"
            path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            web.get(path).open(urlYoutube)
            
        elif "open my java course" in query:
            url = "https://www.udemy.com/course/java-se-programming/learn/lecture/18183562#overview"
            path = path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            web.get(path).open(url)
            
        elif "hello jarvis how are you" in query:
            speak("i m fine sir...how about you?")
        elif "i m also fine." in query:
            continue
        elif "are you ready to display yourself" in query:
            speak("not in a way that you wanted....but yes...i m ready")
            
        elif "then lets go" in query:
            speak("yes sir...what do you want me ..to do")
            
        elif "yes nice" in query or "nice" in query or "well done" in query or "well done jarvis" in query:
            speak("thank you sir...now what else can i do for you?")
        
    # takecommand()
    # webbrowsing()