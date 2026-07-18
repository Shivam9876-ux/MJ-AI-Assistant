import pyautogui as ui
from Head.mouth import speak
import random
from Dtata.dlg_data.dlg import *

random_clo = random.choice(close_dlg)
random_log = random.choice(lock_dlg)
random_sud = random.choice(shutdown_dlg)

def close():
    speak(random_clo)
    ui.hotkey("alt", "f4")

def lock_pc():
    speak(random_log)
    ui.hotkey("win", "l")

def shutdown():
    speak(random_sud)
    ui.hotkey("win", "r")
    ui.write("shutdown /s /t 0")
    ui.press("enter")
