import streamlit as st
import json
from utils import get_response

# Function to load the knowledge base
def load_knowledge_base():
    """Load the knowledge base from the JSON file."""
    with open('data/crypto_terms.json', 'r') as file:
        return json.load(file)

def main():
    # Set the Streamlit page configuration
    st.set_page_config(page_title="Crypto Basics Chatbot", page_icon="💬")

    # Display the header
    st.title("Welcome to the Cryptocurrency Basics Chatbot 💬")
    st.write("Ask me anything about cryptocurrencies and blockchain!")

    # Load the knowledge base
    knowledge_base = load_knowledge_base()

    # User input
    user_input = st.text_input("Your Question:", "")

    if user_input:
        # Get the response from the chatbot
        response = get_response(user_input, knowledge_base)

        # Display the response from the chatbot
        st.write(f"**Bot's Answer:** {response}")

    # Footer (Optional)
    st.markdown("---")
    st.write("Built with ❤️ using Streamlit")

if __name__ == "__main__":
    main()
