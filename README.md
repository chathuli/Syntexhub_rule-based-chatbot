# Simple Rule-Based Chatbot

A console-based chatbot built in Python that uses **keyword/pattern matching** to detect user intents (greeting, help, small talk, thanks, goodbye) and falls back to a small **knowledge base** for domain-specific questions. Every conversation is automatically logged with timestamps.

## 📌 Features

- Rule-based intent detection using keyword matching (no external NLP library required)
- Supports multiple intents: `greeting`, `help`, `smalltalk`, `thanks`, `goodbye`
- Small knowledge base for domain questions (Python, AI, Machine Learning, etc.)
- Fallback response for unrecognized input
- Interactive console loop
- Automatic conversation logging to `conversation_log.txt` with timestamps and detected intent

## 🗂️ Project Structure

```
rule-based-chatbot/
│── chatbot.py             # Main chatbot logic (intents + conversation loop)
│── knowledge_base.py       # Domain Q&A knowledge base
│── conversation_log.txt    # Auto-generated log of conversations (created on first run)
│── README.md
```

## ⚙️ How It Works

The bot follows a simple rule chain for every user message:

1. **Check intents** — Is the input a greeting, help request, small talk, thanks, or goodbye? (keyword matching)
2. **Check knowledge base** — If no intent matches, check if the input contains a known domain question.
3. **Fallback** — If neither matches, respond with a generic "I didn't understand" message.

Every exchange (user input + bot response + detected intent) is logged to `conversation_log.txt`.

## ▶️ How to Run

```bash
python chatbot.py
```

*(On Windows, you may need to use `py` instead of `python`.)*

Type `bye`, `exit`, or `quit` to end the conversation.

## 🧪 Example Conversation

```
Bot: Hello! I'm a rule-based chatbot. Type 'help' to see what I can do, or 'bye' to exit.
You: hi
Bot: Hello! How can I help you today?
You: what is python
Bot: Python is a high-level, easy-to-read programming language widely used in AI, web development, and automation.
You: thank you
Bot: You're welcome! 😊
You: bye
Bot: Goodbye! Have a great day!
```

## 📝 Conversation Log Sample

```
[2026-07-06 05:17:00] You: hi
[2026-07-06 05:17:00] Bot (greeting): Hello! How can I help you today?
[2026-07-06 05:17:00] You: what is python
[2026-07-06 05:17:00] Bot (knowledge_base): Python is a high-level, easy-to-read programming language...
```

## 🧠 Design Details

- **Matching approach:** substring/keyword matching (case-insensitive)
- **Knowledge base:** Python dictionary of question → answer pairs
- **Logging:** appends to a text file with timestamps for every exchange

## 🚀 Possible Improvements

- Use regex patterns for more flexible matching
- Integrate ChatterBot or AIML for more advanced NLP-based responses
- Add a GUI (e.g., using Tkinter or a simple web frontend)
- Expand the knowledge base with more domain topics
- Add typo tolerance (fuzzy matching)

## 🌐 Web Frontend

A browser-based version is also included (`index.html`). Just open it 
directly in any browser — no server or installation required.

## 👤 Author

Project completed as part of the SynTecXHub Internship — Week 2 Task (Project 1).