import os
import sys

# Add the MJ project folder to Python's search path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Traning_model.model import mind
from Head.mouth import speak

import wikipedia
import threading
import time
import webbrowser
from Traning_model.model import mind

def save_qa_data(file_path, qa_dict):
    with open(file_path, "w", encoding="utf-8") as f:
        for q, a in qa_dict.items():
            f.write(f"{q}:{a}\n")

def load_qa_data(file_path):
    qa_dict = {}

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Split only at the first colon
            parts = line.split(":", 1)

            if len(parts) != 2:
                continue

            q, a = parts
            qa_dict[q.strip()] = a.strip()

    return qa_dict

qa_file_path = r"C:\Users\ACER\OneDrive\Desktop\MJ\Dtata\brain_data\qna_data.txt"
qa_dict = load_qa_data(qa_file_path)

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)  # Adjust the speed of the animation

    print()  # Move to the next line after printing

def wiki_search(prompt):
    # Remove assistant name and keyword
    search_prompt = prompt.replace("mj", "")
    search_prompt = search_prompt.replace("wikipedia", "")
    search_prompt = search_prompt.strip()

    try:
        # Get a 2-sentence summary from Wikipedia
        wiki_summary = wikipedia.summary(search_prompt, sentences=2)

        # Create threads
        animate_thread = threading.Thread(
            target=print_animated_message,
            args=(wiki_summary,)
        )

        speak_thread = threading.Thread(
            target=speak,
            args=(wiki_summary,)
        )

        # Start threads
        animate_thread.start()
        speak_thread.start()

        # Wait for both threads to finish
        animate_thread.join()
        speak_thread.join()

        # Store the result in the Q&A dictionary
        qa_dict[search_prompt] = wiki_summary
        save_qa_data(qa_file_path, qa_dict)

    except wikipedia.exceptions.DisambiguationError:
        message = (
            "There is a disambiguation page for the given query. "
            "Please provide more specific information."
        )
        speak(message)
        print(message)

    except wikipedia.exceptions.PageError:
        google_search(prompt)

    except Exception as e:
        print(f"Wikipedia Error: {e}")
        speak("Sorry, I couldn't fetch information from Wikipedia.")
        google_search(prompt)
import webbrowser
import urllib.parse
import webbrowser
import urllib.parse
import os
from Head.mouth import speak
def google_search(command):
    command = command.lower().strip()

    # ---------- Google Images ----------
    if "image of" in command or "images of" in command:
        query = command.replace("image of", "").replace("images of", "").strip()
        url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(query)
        speak(f"Showing images of {query}")
        webbrowser.open(url)
        return

    # ---------- Google Maps ----------
    if "map of" in command or "location of" in command:
        query = command.replace("map of", "").replace("location of", "").strip()
        url = "https://www.google.com/maps/search/" + urllib.parse.quote_plus(query)
        speak(f"Opening map of {query}")
        webbrowser.open(url)
        return

    # ---------- Google News ----------
    if "news about" in command:
        query = command.replace("news about", "").strip()
        url = "https://news.google.com/search?q=" + urllib.parse.quote_plus(query)
        speak(f"Searching news about {query}")
        webbrowser.open(url)
        return

    # ---------- YouTube ----------
    if "youtube" in command:
        query = command.replace("youtube", "").replace("search", "").strip()

        if query:
            url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(query)
        else:
            url = "https://www.youtube.com"

        speak("Opening YouTube")
        webbrowser.open(url)
        return

    # ---------- Gmail ----------
    if "gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
        return

    # ---------- Google Search ----------
    remove_words = [
        "google",
        "search",
        "search for",
        "find",
        "look up",
        "tell me about"
    ]

    query = command

    for word in remove_words:
        query = query.replace(word, "")

    query = query.strip()

    if query:
        url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
        speak(f"Searching Google for {query}")
        print("Searching:", query)
        webbrowser.open(url)
    else:
        speak("What should I search?")
