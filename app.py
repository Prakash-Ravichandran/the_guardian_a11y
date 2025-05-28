from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/analyze', methods=['POST'])
def analyze_post_call():
    if request.is_json:
        query = request.get_json()

        #TODO
        # 

        response_data = {
            "received_data": query,  # NEW DATA = response from OLLAMA
            "status": "success",
            "message": "Data received successfully"
        }
        return jsonify(response_data), 200
    else:
        return jsonify({ "error": "Invalid JSON" }), 400

@app.route('/', methods=['GET'])
def analyze_get_call():
    return "Wecome to the Accessibility Fixer Bot API! Use POST /analyze to send data.", 200

if __name__ == '__main__':
    app.run(debug=True)
# This is a simple Flask application that provides an API endpoint for analyzing data.