import json
import random
from utils import get_response

def load_knowledge_base():
    """Load the knowledge base from the JSON file."""
    with open('data/crypto_terms.json', 'r') as file:
        return json.load(file)

def start_chat():
    """Start the chatbot and handle user interaction."""
    knowledge_base = load_knowledge_base()
    
    print("Welcome to the Cryptocurrency Basics Chatbot!")
    print("Ask me anything about cryptocurrencies. Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'exit':
            print("Goodbye!")
            break
        
        response = get_response(user_input, knowledge_base)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    start_chat()
