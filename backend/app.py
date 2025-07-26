from flask import Flask, request, jsonify
from chatbot_logic import get_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
