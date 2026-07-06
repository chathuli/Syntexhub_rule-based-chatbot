"""
Knowledge Base
---------------
A small dictionary of domain-specific questions and answers.
The chatbot will check user input against these keys to find
a matching answer (using simple substring matching).

You can customize the "domain" by changing the questions/answers below.
Currently set up as a general Programming & AI FAQ bot.
"""

knowledge_base = {
    "what is python": "Python is a high-level, easy-to-read programming language widely used in AI, web development, and automation.",
    "what is ai": "AI (Artificial Intelligence) is the field of computer science focused on building systems that can perform tasks that normally require human intelligence.",
    "what is machine learning": "Machine Learning is a subset of AI where systems learn patterns from data instead of being explicitly programmed.",
    "what is a chatbot": "A chatbot is a program designed to simulate conversation with human users, often using pattern matching or machine learning.",
    "what is github": "GitHub is a platform for hosting and collaborating on code using Git version control.",
    "what is an algorithm": "An algorithm is a step-by-step set of instructions used to solve a problem or complete a task.",
    "who created python": "Python was created by Guido van Rossum and first released in 1991.",
    "what is a variable": "A variable is a named container used to store data values in a program.",
}


def search_knowledge_base(user_input):
    """
    Checks if any knowledge base question is contained in the user's input.
    Returns the matching answer, or None if nothing matches.
    """
    user_input = user_input.lower()

    for question, answer in knowledge_base.items():
        if question in user_input:
            return answer

    return None
