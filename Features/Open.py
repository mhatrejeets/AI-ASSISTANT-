import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def Openexe(query):
    query = str(query).lower()

    if "visit" in query :
        nameofweb = query.replace("visit ","")
        link= f"https://www.{nameofweb}.com"
        webbrowser.open(link)
        return True

    elif "launch" in query :
        nameofweb = query.replace("launch ","")
        link= f"https://www.{nameofweb}.com"
        webbrowser.open(link)
        return True


    elif "open" in query:
        nameofapp= query.replace("open","")
        pyautogui.press('win')
        sleep(0.5)
        keyboard.write(nameofapp)
        sleep(0.5)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    elif "start" in query:
        nameofapp= query.replace("start","")
        pyautogui.press('win')
        sleep(2)
        keyboard.write(nameofapp)
        sleep(1)
        keyboard.press('enter')
        sleep(1)
        return True
    
    else:
        return False
    

