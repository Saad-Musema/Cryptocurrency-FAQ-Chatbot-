import random
# from google import genai

# Initialize Gemini client
# client = genai.Client(api_key="AIzaSyBHg_sD7ks5gt4adUXis0DBGN9ZPVFQDgU")  # Replace with your actual API key

def get_response(user_input, knowledge_base):
    """Retrieve a response from the knowledge base or Gemini API based on user input."""
    
    # First, try to find a match in the knowledge base (simple keyword matching)
    for term, data in knowledge_base.items():
        if term in user_input:
            return f"{data['definition']} Example: {data['example']}"
    
    # If no match is found, query Gemini API for a response
    # response = query_gemini_api(user_input)
    return response

def query_gemini_api(user_input):
    """Query the Gemini API for a response to the user's input."""
    try:
        # Using the Gemini model to generate a response
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # Model used by Gemini
            contents=user_input
        )
        
        # Returning the text of the response from the Gemini API
        return response.text
    except Exception as e:
        return f"Error connecting to the Gemini API: {e}"
