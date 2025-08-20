import random
import string
from datetime import datetime


def preprocess(text):
    """Lowercase, remove punctuation, strip spaces"""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.strip()

# simple rules to handle user input
greetings = ["hello", "hi", "hey", "good morning", "good evening"]
farewells = ["bye", "goodbye", "see you", "quit", "exit"]
how_are_you = ["how are you", "how are you doing", "whats up", "how do you feel"]
about_bot = ["your name", "who are you", "what are you"]
time_queries = ["time", "current time", "what time is it"]
date_queries = ["date", "today's date", "what day is it"]

# chatbot response
greeting_responses = [
    "Hello there! How can I help you today?",
    "Hi! Nice to see you. What's up?",
    "Hey! How are you doing?"
]

farewell_responses = [
    "Goodbye! Take care",
    "See you soon. Bye!",
    "It was nice chatting with you. Bye!"
]

how_are_you_responses = [
    "I'm just a bot, but I'm doing great! Thanks for asking.",
    "All systems running smoothly! How about you?",
    "I'm always happy to chat with you."
]

about_bot_responses = [
    "I am a simple chatbot created using Python and rule-based NLP.",
    "I'm ChatBot – a project to demonstrate basic NLP concepts.",
    "I'm not very smart, but I can hold a basic conversation!"
]


def chatbot():
    print("ChatBot: Hello! I am a simple chatbot. Type 'bye' or 'exit' to quit.")

    while True:
        user_input = input("You: ")
        processed = preprocess(user_input)

        if processed in greetings:
            print("ChatBot:", random.choice(greeting_responses))

        elif processed in farewells:
            print("ChatBot:", random.choice(farewell_responses))
            break

        elif any(q in processed for q in about_bot):
            print("ChatBot:", random.choice(about_bot_responses))

        elif any(q in processed for q in how_are_you):
            print("ChatBot:", random.choice(how_are_you_responses))

        elif any(q in processed for q in time_queries):
            now = datetime.now().strftime("%H:%M:%S")
            print("ChatBot: The current time is", now)

        elif any(q in processed for q in date_queries):
            today = datetime.now().strftime("%A, %d %B %Y")
            print("ChatBot: Today's date is", today)

        elif "help" in processed:
            print("ChatBot: You can ask me things like:\n"
                  "- Greetings (hello, hi)\n"
                  "- Ask about me (who are you)\n"
                  "- Ask time/date\n"
                  "- Say bye to exit")

        else:
            print("ChatBot: Sorry, I don't understand that. Try asking something else!")


if __name__ == "__main__":
    chatbot()
