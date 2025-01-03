import pyttsx3

engine = pyttsx3.init()
text = "hello Chandan sir"
engine.setProperty('rate',140)      #default rate = 200     #total 4 properties hoti hai -> rate, voice, volumn,
engine.setProperty('volume',0.5)       # volumn take float between 0 and 1
#voices
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)        # default voice is voice[0]

# engine.save_to_file()  # audio ek mp3 file bankr same directory mei save ho jayega
engine.say(text)
engine.runAndWait()