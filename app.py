from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Your verification token (found in Slack app settings)
SLACK_VERIFICATION_TOKEN = 'xoxb-7401649483671-7418796889140-uiJiemJUF7AksSqZccvF7hNS'

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

if __name__ == '__main__':
    app.run(port=5000)
