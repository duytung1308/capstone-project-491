"""This is work in progress
This where the user input will be processed then send to my chatbot in main.py to produce a respond"""




from flask import Flask, render_template, request, jsonify
from main import process_message
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('beta2.html')  # Update this with your HTML file

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('user_input')

    # Send the input to your chatbot and get the chatbot's response
    chatbot_response = process_with_chatbot(user_input)

    # Return the chatbot's response as JSON
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
