import os
import sys

#PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#if PROJECT_ROOT not in sys.path:

from Head.mouth import *
from Head.ear import *
from Head.brain import *
from function.wish import *
from function.welcom import welcom_g
from Dtata.dlg_data.dlg import *
from Traning_model.model import *
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
from Automation.open import *
from Automation.close import *
from friday.Fspeak import fspeak
from function.chack_online_offline import is_online

def mj():
    
    wish()
    while True:

        text = listen()
        

        if text is None:
            continue

        text = text.strip().lower()
        text = text.replace("mg","mj")
       
        text = text.replace("m j", "mj")
        text = text.replace("buy m", "bye mj")
        text = text.replace("buy mj", "bye mj")
        text = text.replace("by mj", "bye mj")
        text = text.replace("good by", "goodbye")
        text = text.replace("bhai","bye")
        text = text.lower().strip()


        if not text:
            continue

        if text in wake_key_word:
            welcom_g()
        
        elif text in bye_key_word:
            
            speak(random.choice(res_bye))
            break
            

        elif text.startswith("mj"):
            text = text.replace("mj",'')
            text = mind(text)
            speak(text)

        elif text.endswith(("mj"," mj")):
            text = text.replace("mj",'')
            text = mind(text)
            speak(text)
        
        elif text.startswith("open"):
            app = text.replace("open", "").strip().replace(" ", "")

            if app in SPECIAL_SITES or "." in app:
                open_website(text)
            else:
                appopen(text)
        
            continue
        elif text.startswith(('lock pc','lock my computer','lock computer')):
            lock_pc()
        
        elif text.startswith(('close','close window','exit','quit','close this')):
            close()
        
        elif text.startswith(('shutdown','shut down','power off','restart')):
            shutdown()

        else:
            pass

def check_mj():
    if is_online():
        fspeak(random.choice(online_dlg))
        mj()
    else:
       
        fspeak(random.choice(offline_dlg))

check_mj()