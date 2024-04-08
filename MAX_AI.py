import os
from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
from time import sleep






print(">>>>> Starting Max . Just wait for a sec.<<<<<<<")
from Body.Speak import SpeakW
from Features.clap import Tester
from newmain import MainTaskExecution
print(">>>>> Some more seconds please.<<<<<<<")

SpeakW("Hello Sir , I am ready to assist you.")
def MainExecution() :
    while True :
        Data = MicExecution()
        data=Data.lower()
        print(len(data))


        if len(data)<3 :
            continue
        
        ValueReturn = MainTaskExecution(Data)
        if ValueReturn == True :
            SpeakW("Opened.")
            pass

        if "using artificial intelligence" in data :
            writetofile(data)
            sleep(1)
            SpeakW("Done with writing.")
            continue

            
        
        if "max stop" in data:
            SpeakW("Okay, If you need me just clap. Bye.")
            break
        
        
        

    

        Data=str(Data)
        Reply = ReplyBrain(Data)
        SpeakW(Reply)


def ClapDetect():
    queery=Tester()
    if "True-Mic" in queery:
        print("\n >>>>> Clap Detected <<<<<< ")
        SpeakW("Hello ")
        MainExecution()

    else :

        pass

def writetofile(prompt):
    if not os.path.exists("Your_files"):
        os.mkdir("Your_files")

    ans = ReplyBrain(prompt)
    with open(f"Your_files/{''.join(prompt.split('intelligence')[1:])}.txt","w") as f:
        f.write(ans)

    return True




while True :
    ClapDetect()



