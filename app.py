from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Your verification token (found in Slack app settings)
SLACK_VERIFICATION_TOKEN = os.getenv('SLACK_VERIFICATION_TOKEN')

# Function to run a Python script
def run_script(script_name, username, password, email):
    try:
        # Use subprocess to run the script with parameters
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

    # Ensure the correct number of parameters are provided
    if len(text) != 3:
        return jsonify({'text': 'Please provide username, password, and email'}), 400

    username, password, email = text

    if command == '/run-billing':
        output = run_script('billing.py', username, password, email)
    elif command == '/run-badges':
        output = run_script('badges.py', username, password, email)
    else:
        output = 'Unknown command'

    return jsonify({'text': output})

@app.route('/slack/events', methods=['POST'])
def slack_events():
    data = request.json
    token = data.get('token')
    
    # Verify the request is from Slack
    if token != SLACK_VERIFICATION_TOKEN:
        return jsonify({'text': 'Invalid token'}), 403

    event = data.get('event')
    if event and event.get('type') == 'message' and event.get('subtype') is None:
        user_id = event.get('user')
        text = event.get('text')
        
        # Respond to the message
        if text.lower() == 'hello':
            response_text = f"Hello, <@{user_id}>!"
        else:
            response_text = f"You said: {text}"
        
        # Post a message back to Slack (you'll need to use Slack's Web API for this)
        post_message_to_slack(event.get('channel'), response_text)
        
    return jsonify({'status': 'ok'})

def post_message_to_slack(channel, text):
    from slack_sdk import WebClient
    slack_token = os.getenv('SLACK_BOT_TOKEN')
    client = WebClient(token=slack_token)
    client.chat_postMessage(channel=channel, text=text)

if __name__ == '__main__':
    app.run(port=5000)
