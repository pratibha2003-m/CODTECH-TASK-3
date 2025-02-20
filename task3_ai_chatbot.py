import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help you?"]],
    [r"what is your name?", ["I'm a chatbot created for this internship!"]],
    [r"bye|goodbye", ["Goodbye! Have a great day!"]]
]

def chatbot():
    print("Chatbot is ready! Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
