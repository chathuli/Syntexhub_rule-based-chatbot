"""
Simple Rule-Based Chatbot
--------------------------
A console chatbot that uses keyword/pattern matching to detect intents
(greeting, help, small talk, goodbye) and falls back to a knowledge base
for domain-specific questions. Every conversation is logged to a file.
"""

import datetime
from knowledge_base import search_knowledge_base

# ---------------------------------------------------------
# Intent patterns: each intent maps to a list of trigger keywords
# ---------------------------------------------------------
intents = {
    "greeting": ["hi", "hello", "hey", "good morning", "good evening"],
    "help": ["help", "what can you do", "options", "commands"],
    "smalltalk": ["how are you", "what's up", "how is it going"],
    "thanks": ["thank you", "thanks", "appreciate it"],
    "goodbye": ["bye", "goodbye", "exit", "quit", "see you"],
}

# Sample responses for each intent (a real rule engine could randomize these)
responses = {
    "greeting": "Hello! How can I help you today?",
    "help": (
        "I can chat with you about greetings, small talk, and answer some "
        "domain questions (try asking 'what is python' or 'what is AI'). "
        "Type 'bye' to exit."
    ),
    "smalltalk": "I'm just a program, but I'm running smoothly! How about you?",
    "thanks": "You're welcome! 😊",
    "goodbye": "Goodbye! Have a great day!",
    "fallback": "Sorry, I didn't quite understand that. Type 'help' to see what I can do.",
}


def match_intent(user_input):
    """
    Checks the user input against each intent's keyword list.
    Returns the matching intent name, or None if nothing matches.
    """
    user_input = user_input.lower()

    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent

    return None


def get_response(user_input):
    """
    Determines the chatbot's response using a two-step rule chain:
    1. Check for a matching intent (greeting, help, small talk, etc.)
    2. If no intent matches, check the knowledge base for domain questions
    3. If neither matches, return the fallback response
    """
    intent = match_intent(user_input)

    if intent:
        return responses[intent], intent

    kb_answer = search_knowledge_base(user_input)
    if kb_answer:
        return kb_answer, "knowledge_base"

    return responses["fallback"], "fallback"


def log_conversation(user_input, bot_response, intent, log_file="conversation_log.txt"):
    """
    Appends the exchange (with timestamp and detected intent) to a log file.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] You: {user_input}\n")
        f.write(f"[{timestamp}] Bot ({intent}): {bot_response}\n")


def run_chatbot():
    """
    Main interactive loop. Reads user input from the console,
    generates a response, prints it, and logs the exchange.
    """
    print("Bot: Hello! I'm a rule-based chatbot. Type 'help' to see what I can do, or 'bye' to exit.")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        bot_response, intent = get_response(user_input)
        print(f"Bot: {bot_response}")

        log_conversation(user_input, bot_response, intent)

        if intent == "goodbye":
            break


if __name__ == "__main__":
    run_chatbot()
