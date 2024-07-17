from flask import Flask, request, jsonify
import subprocess
import os
from slack_sdk import WebClient

app = Flask(__name__)

# Read the Slack verification token and bot token from environment variables
SLACK_VERIFICATION_TOKEN = os.getenv('SLACK_VERIFICATION_TOKEN')
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')

# Initialize Slack client
client = WebClient(token=SLACK_BOT_TOKEN)

# Function to run a Python script
def run_script(script_name, username, password, email):
    try:
        result = subprocess.run(['python', script_name, username, password, email], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.route('/slack/command', methods=['POST'])
def slack_command():
    data = request.form
    token = data.get('token')

    # Verify the request is from Slack
    if token != SLACK_VERIFICATION_TOKEN:
        return jsonify({'text': 'Invalid token'}), 403

    command = data.get('command')
    text = data.get('text').split()

    if len(text) != 3:
        return jsonify({'text': 'Please provide your NetID, Password, and Email'}), 400

    username, password, email = text

    if command == '/run-billing':
        output = run_script('billing.py', username, password, email)
    elif command == '/run-badges':
        output = run_script('badges.py', username, password, email)
    else:
        output = 'Unknown command'

    return jsonify({'text': output})

@app.route('/slack/clearances', methods=['POST'])
def slack_clearances():
    data = request.form
    token = data.get('token')

    # Verify the request is from Slack
    if token != SLACK_VERIFICATION_TOKEN:
        return jsonify({'text': 'Invalid token'}), 403

    command = data.get('command')
    text = data.get('text').split()

    if len(text) < 3:
        return jsonify({'text': 'Please provide NetID, Password, and at least one NetID to clear.'}), 400

    username = text[0]
    password = text[1]
    netid_list = text[2:]

    if command == '/run-clearances':
        output = run_script('clearances.py', username, password, netid_list)
    else:
        output = 'Unknown command'
    
    return jsonify({'text': output})

@app.route('/slack/interactive', methods=['POST'])
def slack_interactive():
    data = request.json
    return jsonify({'text': 'Interactive component received'})

@app.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.json
    token = data.get('token')

    if token != SLACK_VERIFICATION_TOKEN:
        return jsonify({'text': 'Invalid token'}), 403

    event = data.get('event')
    if event and event.get('type') == 'message' and event.get('subtype') is None:
        user_id = event.get('user')
        text = event.get('text')

        if text.lower() == 'hello':
            response_text = f"Hello, <@{user_id}>!"
        else:
            response_text = f"You said: {text}"

        client.chat_postMessage(channel=event.get('channel'), text=response_text)

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(port=5000)
