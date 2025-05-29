from flask import Flask, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from knowledge import INSTRUCTIONS  # Import the variable

app = Flask(__name__)

# Configure the Gemini API key (Langchain will automatically pick it up)
if not os.environ["GOOGLE_API_KEY"]:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")

# Initialize the Langchain ChatGoogleGenerativeAI model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

#import instructions

@app.route('/analyze', methods=['POST'])
def analyze_post_call():
    if request.is_json:
        query = request.get_json().get('query')

        if not query:
            return jsonify({"error": "Missing 'query' in JSON payload"}), 400

       
        # Add the instructions to the query
        user_prompt = f"{INSTRUCTIONS}\n\nUser Query: {query}"

        # Connect to GEMINI and send the query to GEMINI
        try:
            response = llm.invoke(user_prompt)
            gemini_response = response.content

            response_data = {
            "input_data": query,  # Input data sent to the GEMINI
            "gemini_response": gemini_response,  # Response from GEMINI
            "status": "success",
            "message": "Data received successfully"
            }
            print("Response from Gemini:", gemini_response)
            # Return the response as JSON
            return jsonify(response_data), 200
        except Exception as e:
            error_message = f"Error communicating with Gemini (via Langchain): {e}"
            print(error_message)
            return jsonify({"error": error_message}), 500
    else:
        return jsonify({ "error": "Invalid JSON" }), 400

@app.route('/', methods=['GET'])
def analyze_get_call():
    return "Wecome to the Accessibility Fixer Bot API! Use POST /analyze to send data.", 200

if __name__ == '__main__':
    app.run(debug=True)
# This is a simple Flask application that provides an API endpoint for analyzing data.