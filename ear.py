'''
import speech_recognition as sr  #pip install SpeechRecognition
import os                        #no need to insatll
import threading
from mtranslate import translate              #it is used to convert hindi to english for assistant #pip install mtranslate
from colorama import Fore,Style,init
# 
init(autoreset=True)   #Automaticaly resat colors
# 
def print_loop():
    while True:
        print(Fore.LIGHTGREEN_EX + "I an Listning....",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        print("",end="",flush=True)
# 
def Trans_hindi_to_english(txt):
    english_txt= translate(txt,to_language="en_in")
    return english_txt
# 
def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 1000
    recognizer.dynamic_energy_adjustment_damping = 0.02    #you voice to lisin a computer
    recognizer.dynamic_energy_ratio = 1.5      # if you start speack to continuty to lisin computer
    recognizer.pause_threshold = 0.8       # it is depand you speed itna less utni speed
    recognizer.operation_timeout = None
    recognizer.non_speaking_duration = 0.1
# 
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
# 
        while True:
            print(Fore.LIGHTGREEN_EX + "I am Listning....",end="",flush=True)
# 
            try:
                audio = recognizer.listen(source,timeout=None)
                print('\r'+Fore.LIGHTBLUE_EX + "Got it , Recognizing...",end="",flush=True)
                recognizer_txt = recognizer.recognize_google(audio).lower()
                if recognizer_txt:
                    translated_txt = Trans_hindi_to_english(recognizer_txt)
                    print('\r'+Fore.LIGHTYELLOW_EX + "Boss : " + translated_txt)
                    return translated_txt
                else:
                    return ""
            except sr.UnknownValueError :
                recognizer_txt = ""
# 
            finally:
                print('\r',end="",flush=True)
            # 
        os.system("cls" if os.name == "nt" else "clear")
#
        #threading part
#
        listen_thread = threading.Thread(target=listen)
        print_thread = threading.Thread(target=print_loop)
        listen_thread.start()
        print_thread.start()
        listen_thread.join()
        print_thread.join()   
'''
'''
new code 
'''
"""
===========================================
MJ AI Assistant - Ear Module
Author : Shivam Singh
Purpose: Listen to the user's voice
Python : 3.13+
===========================================
"""
import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, init
import threading
import time

init(autoreset=True)

# ------------------------------------------
# Translate Hindi → English
# ------------------------------------------

def translate_to_english(text: str) -> str:
    try:
        return translate(text, "en")
    except Exception:
        return text


# ------------------------------------------
# Loading Animation
# ------------------------------------------

stop_animation = False


def listening_animation():
    dots = ""

    while not stop_animation:
        dots += "."
        if len(dots) > 3:
            dots = ""

        print(
            "\r"
            + Fore.LIGHTGREEN_EX
            + f"MJ : Listening{dots}      ",
            end="",
            flush=True,
        )

        time.sleep(0.35)


# ------------------------------------------
# Recognizer
# ------------------------------------------

recognizer = sr.Recognizer()

recognizer.dynamic_energy_threshold = True
recognizer.non_speaking_duration = 0.3
recognizer.pause_threshold = 0.8 
recognizer.phrase_threshold = 0.3  
recognizer.operation_timeout = None 
recognizer.dynamic_energy_threshold = False 
recognizer.energy_threshold = 1000

# ------------------------------------------
# Microphone (Create Once)
# ------------------------------------------

mic = sr.Microphone()
# 
# print(Fore.CYAN + "MJ : Calibrating microphone...")
# 
with mic as source:
    recognizer.adjust_for_ambient_noise(source, duration=2)
# 
# print(Fore.GREEN + "MJ : Microphone Ready.\n")
 

# ------------------------------------------
# Listen
# ------------------------------------------

def listen():

    global stop_animation

    with mic as source:

        stop_animation = False

        animation = threading.Thread(
            target=listening_animation,
            daemon=True
        )

        animation.start()

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )

            stop_animation = True
            animation.join()

            print(
                "\r"
                + Fore.CYAN
                + "MJ : Recognizing...                ",
                end="",
                flush=True,
            )

            text = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            text = text.strip().lower()

            if text == "":
                return ""

            text = translate_to_english(text)
            print("\r" + " " * 80, end="\r", flush=True)

            print(Fore.YELLOW + "Boss :", text)
            return text

        except sr.WaitTimeoutError:

            stop_animation = True
            animation.join()

            return ""

        except sr.UnknownValueError:

            stop_animation = True
            animation.join()

            return ""

        except sr.RequestError:

            stop_animation = True
            animation.join()

            print(
                Fore.RED
                + "MJ : Internet connection required."
            )

            return ""

        except Exception as e:

            stop_animation = True
            animation.join()

            print(
                Fore.RED
                + f"MJ Error : {e}"
            )

            return ""


# ------------------------------------------
# Test
# ------------------------------------------

if __name__ == "__main__":

    while True:

        query = listen()

        if query:

            print(
                Fore.GREEN
                + "You Said ->",
                query
            )