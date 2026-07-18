# import asyncio
# import threading
# import os
# import edge_tts
# import pygame

# VOICE = "en-AU-WilliamNeural"
# BUFFER_SIZE = 1024

# def remove_file(file_path):
#     max_attempts = 3
#     attempts = 0
#     while attempts < max_attempts :
#         try:
#             with open(file_path,"wb"):
#                 pass
#             os.remove(file_path)
#             break

#         except Exception as e:
#             print(f"error : {e}")
#             attempts+=1
# async def amain(TEXT,output_file) -> None:
#     try:
#         cm_text = edge_tts.Communicate(TEXT,VOICE)
#         await cm_text.save(output_file)
#         thread = threading.Thread(target=play_audio,args=(output_file))
#         thread.start()
#         thread.join()
#     except Exception as e:
#         print(f"error : {e}")    

#     finally:
#         remove_file(output_file)

# def play_audio(file_path):
#     try:
#         pygame.init()
#         pygame.mixer.init()
#         sound = pygame.mixer.Sound(file_path)
#         sound.play()
#         while pygame.mixer.get_busy():
#             pygame.time.get_ticks(10)

#             pygame.quit()

#     except Exception as e:
#         print(f"error : {e}")

# def speak(TEXT,output_file=None):
#     if output_file is None:
#         output_file = f"{os.getcwd()}/speak.mp3"
#         asyncio.run(amain(TEXT,output_file))

# speak("Welcom, to the world of MJ ")


import asyncio
import threading
import os
import time
import edge_tts
import pygame
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)
# 
VOICE = "en-IN-NeerjaNeural"
# 
# 
from colorama import Fore

def print_animated_message(message):

    print()                      # Move to next line

    print(Fore.CYAN + "MJ : ", end="", flush=True)

    for char in str(message):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)         # Faster typing (0.03 is much better)

    print()                      # Finish with a new line

def remove_file(file_path):
    """Delete file safely after audio playback."""
    for _ in range(10):
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            return
        except PermissionError:
            # File is still being used by pygame
            time.sleep(0.5)
        except Exception as e:
            print(f"Delete Error: {e}")
            return
# 
# 
def play_audio(file_path):
    """Play MP3 file using pygame."""
    try:
        pygame.mixer.init()
# 
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
# 
        clock = pygame.time.Clock()
# 
        while pygame.mixer.music.get_busy():
            clock.tick(10)
# 
    except Exception as e:
        print(f"Audio Error: {e}")
# 
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
# 
# 
async def amain(text, output_file):
    """Generate speech and play it."""
    try:
        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE
        )
# 
        await communicate.save(output_file)
# 
        audio_thread = threading.Thread(
            target=play_audio,
            args=(output_file,),
            daemon=True
        )
# 
        audio_thread.start()
        audio_thread.join()
# 
    except Exception as e:
        print(f"TTS Error: {e}")
# 
    finally:
        remove_file(output_file)
# 
# 
def speak1(text, output_file=None):
    """Main function for speaking text."""
    if output_file is None:
        output_file = os.path.join(
            os.getcwd(),
            "speak.mp3"
        )
# 
    asyncio.run(
        amain(
            text,
            output_file
        )
    )
def speak(text):

    if not text:
        return

    text = str(text)

    audio_thread = threading.Thread(
        target=speak1,
        args=(text,),
        daemon=True
    )

    audio_thread.start()

    # Print while audio is speaking
    print_animated_message(text)

    audio_thread.join()

if __name__ == "__main__":
    speak("Welcome to the world of MJ. and I am very happy to meat you shivam.")
# 
# import pyttsx3
# 
# engine = pyttsx3.init()
# 
# engine.say("Welcome to the world of MJ")
# engine.runAndWait()