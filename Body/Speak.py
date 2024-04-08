import pyttsx3

def SpeakW(Text):
    engine = pyttsx3.init("sapi5") #windows api key
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.setProperty('rate',180)# speed
    print("")
    print(f"You : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()









# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from time import sleep

# chrome_options = Options()
# chrome_options.add_argument('--log-level=3')
# chrome_options.headless = True
# Path ="Database\chromedriver.exe"
# driver = webdriver.Chrome(Path , options= chrome_options)
# driver.maximize_window()
# website = r"https://ttsmp3.com/text-to-speech/British%20English/"
# driver.get(website)
# ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
# ButtonSelection.select_by_visible_text('British English / Brian')

# def Speak(Text):
#     length=len(str(Text))
#     if length == 0:
#         pass

#     else :
#         print("")
#         print(f"Max : {Text} .")
#         print("")
#         Data = str(Text)
#         xpathofsec = '/html/body/div[4]/div[2]/form/textarea'
#         driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').send_keys(Data)
#         driver.find_element(By.XPATH,value='//*[@id="vorlesenbutton"]').click()
#         driver.find_element(By.XPATH,value='/html/body/div[4]/div[2]/form/textarea').clear()

#         if length >= 30  :
#             sleep(4)

#         elif length >= 40  :
#             sleep(6)

#         elif length >= 55  :
#             sleep(8)
        
#         elif length >= 70  :
#             sleep(10)
        
#         elif length >= 100  :
#             sleep(13)

#         elif length >= 120  :
#             sleep(14)

#         else:
#             sleep(2)
        


