# import datetime
# import random
# import os
# import sys

# PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# if PROJECT_ROOT not in sys.path:
#     sys.path.insert(0, PROJECT_ROOT)

# from Head.mouth import speak


# # ==============================
# # Greeting Database
# # ==============================

# MORNING = [
#     "Good morning, Boss! I hope you slept well.",
#     "Good morning, Boss. It's a beautiful day to achieve something amazing.",
#     "Rise and shine, Boss! MJ is ready to assist you.",
#     "Welcome back, Boss. Let's make today productive.",
# ]

# AFTERNOON = [
#     "Good afternoon, Boss! I hope your day is going well.",
#     "Welcome back, Boss. How may I assist you?",
#     "Good afternoon! MJ is online and ready.",
#     "Hope you're having a productive afternoon, Boss.",
# ]

# EVENING = [
#     "Good evening, Boss! Nice to see you again.",
#     "Welcome back, Boss. I am ready for your commands.",
#     "Good evening. Let's finish today's work together.",
#     "Evening, Boss! What can I do for you?",
# ]

# NIGHT = [
#     "Good night, Boss. Working late today?",
#     "Welcome back, Boss. MJ is always available.",
#     "Hello Boss. Burning the midnight oil again?",
#     "Good night! How may I assist you?",
# ]


# QUOTES = [
#     "Success comes from consistency, not perfection.",
#     "Small progress every day adds up to big results.",
#     "Believe in yourself and keep moving forward.",
#     "Dream big, work hard, stay focused.",
#     "Every expert was once a beginner.",
#     "Your future is created by what you do today.",
#     "Discipline beats motivation.",
#     "Never stop learning.",
#     "Stay positive and keep building.",
#     "Every day is another opportunity to improve."
# ]


# # ==============================
# # Time Functions
# # ==============================

# def get_time():
#     return datetime.datetime.now()


# def get_greeting():
#     hour = get_time().hour

#     if 5 <= hour < 12:
#         return random.choice(MORNING)

#     elif 12 <= hour < 17:
#         return random.choice(AFTERNOON)

#     elif 17 <= hour < 21:
#         return random.choice(EVENING)

#     else:
#         return random.choice(NIGHT)


# # ==============================
# # Date & Time
# # ==============================

# def tell_date():
#     now = get_time()

#     day = now.strftime("%A")
#     date = now.strftime("%d")
#     month = now.strftime("%B")
#     year = now.strftime("%Y")

#     return f"Today is {day}, {date} {month}, {year}."


# def tell_time():
#     now = get_time()

#     return now.strftime("The current time is %I:%M %p.")


# # ==============================
# # Random Quote
# # ==============================

# def motivation():
#     return random.choice(QUOTES)


# # ==============================
# # Main Wish Function
# # ==============================

# def wish():

#     greeting = get_greeting()

#     speak(greeting)
#     print(greeting)

#     date_info = tell_date()

#     speak(date_info)
#     print(date_info)

#     time_info = tell_time()

#     speak(time_info)
#     print(time_info)

#     line = "I am MJ, your personal artificial intelligence assistant."

#     speak(line)
#     print(line)

#     quote = motivation()

#     speak("Motivation for today.")
#     speak(quote)

#     print("Motivation:", quote)

#     ending = random.choice([
#         "How may I assist you today, Boss?",
#         "What would you like me to do?",
#         "Waiting for your command.",
#         "Ready whenever you are.",
#         "Please tell me your command.",
#         "Listening carefully."
#     ])

#     speak(ending)
#     print(ending)


# # ==============================
# # Test
# # ==============================

# if __name__ == "__main__":
#     wish()

# ==========================================================
# WISH FUNCTION
# ==========================================================
import datetime
import random
import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Head.mouth import speak
from Dtata.dlg_data.dlg import *


def greeting():

    hour = datetime.datetime.now().hour

    if 5 <= hour < 12:
        return random.choice(GOOD_MORNING)

    elif 12 <= hour < 17:
        return random.choice(GOOD_AFTERNOON)

    elif 17 <= hour < 21:
        return random.choice(GOOD_EVENING)

    else:
        return random.choice(GOOD_NIGHT)


def wish():

    print("\n")
    print("=" * 60)
    print("             MJ ARTIFICIAL INTELLIGENCE")
    print("=" * 60)

    # Only greeting
    speak(greeting())

    speak(random.choice(intro_dlg))

    speak(random.choice(ending_dlg))

    print("=" * 60)


if __name__ == "__main__":
    wish()