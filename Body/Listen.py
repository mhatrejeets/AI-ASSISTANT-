import speech_recognition as sr
from googletrans import Translator

# To listen :
def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I'm listening ......")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 6) #listening for 9 seconds


    try:
        print("Understanding.....")
        queery = r.recognize_google(audio, language="en")

    except:
        return ""
    
    queery = str(queery).lower()
    return queery



#To translate
def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}.")
    return data

# To connect
def MicExecution():
    queery= Listen()
    data= TranslationHinToEng (queery)
    return data


