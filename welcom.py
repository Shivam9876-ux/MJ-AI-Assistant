from Head.mouth import speak
from Dtata.dlg_data.dlg import WELCOME_GREETINGS
import random

def welcom_g():
    speak(random.choice(WELCOME_GREETINGS))
