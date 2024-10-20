# chatbot.py

from flask import Flask, request, jsonify
import spacy

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

def get_response(user_input):
    # Process the user input
    doc = nlp(user_input.lower())
    
    # Simple responses based on user input
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "how are you" in user_input.lower():
        return "I'm just a bot, but thanks for asking! How can I help you?"
    elif "help" in user_input.lower():
        return "Sure! What do you need help with?"
    else:
        return "I'm sorry, I didn't understand that."

@app.route('/chat', methods=['POST'])
def chat():
    # Get the user's message from the request
    user_input = request.json.get('message')
    
    # Generate a response
    response = get_response(user_input)
    
    # Return the response as JSON
    return jsonify({"response": response})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
