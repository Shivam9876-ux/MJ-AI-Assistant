import os
import sys
import re
import webbrowser

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import pyautogui as ui
import time
import random
from Head.mouth import speak
from Dtata.dlg_data.dlg import *




def appopen(text):
    text = text.replace("open","")
    text = text.strip()
    random_dlg = random.choice(open_dlg)
    speak(random_dlg + text)
    ui.press("win")
    time.sleep(0.5)
    ui.write(text)
    time.sleep(0.5)
    ui.press("enter")
    random_succ = random.choice(success_open)
    speak(random_succ)


def open_website(command):
    command = command.lower().strip()

    # Remove common words
    command = re.sub(
        r"\b(open|website|site|web|browser|please|launch|start)\b",
        "",
        command,
    ).strip()

    if not command:
        speak("Which website should I open?")
        return

    # Remove spaces (e.g. "stack overflow" -> "stackoverflow")
    name = command.replace(" ", "")

    if name in SPECIAL_SITES:
        url = SPECIAL_SITES[name]
    elif "." in name:
        # User said: github.io, python.org, bbc.co.uk
        url = f"https://{name}"
    else:
        # Default
        url = f"https://www.{name}.com"
    random_dlg = random.choice(open_dlg)
    speak(random_dlg + command)
    webbrowser.open(url)
    random_succ = random.choice(success_open)
    speak(random_succ)

