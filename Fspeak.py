import pyttsx3
from colorama import Fore, init

init(autoreset=True)

friday_engine = pyttsx3.init("sapi5")

voices = friday_engine.getProperty("voices")

# Select a strong female voice
for voice in voices:
    if "zira" in voice.name.lower():
        friday_engine.setProperty("voice", voice.id)
        break

# Strong and clear voice
friday_engine.setProperty("rate", 170)
friday_engine.setProperty("volume", 1.0)


def fspeak(text):
    print()
    print(
        f"{Fore.LIGHTMAGENTA_EX}Friday : {text}",
        end="",
        flush=True
    )

    friday_engine.say(text)
    friday_engine.runAndWait()
