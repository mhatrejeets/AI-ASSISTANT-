import speech_recognition as sr

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I,m Listening in wakeup...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8) # Listening Mode.....
    
    try:
        print("Understanding...")
        queery = r.recognize_google(audio,language="en")

    except:
        return ""
    
    queery = str(queery).lower()
    print(queery)
    return queery

def WakeupDetected():

    while True:

        queery = Listen().lower()

        if "wake up" in queery:
            print("Im Jeet")
            print("Wake up")
            return "True-Mic"
        
        else:
            pass

