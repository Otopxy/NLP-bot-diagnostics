import openai
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import re
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize the GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Set your OpenAI API key (if still using GPT-3 for other tasks)
openai.api_key = "your-openai-api-key-here"

app = Flask(__name__)
socketio = SocketIO(app)

# Mock robot diagnostics database
robot_data = {
    "robot1": {"status": "running", "errors": []},
    "robot2": {"status": "stopped", "errors": ["motor failure"]},
}

@app.route('/')
def index():
    return render_template('index.html')  # Frontend page

@app.route('/get_robot_status/<robot_id>', methods=['GET'])
def get_robot_status(robot_id):
    if robot_id in robot_data:
        return robot_data[robot_id]
    else:
        return {"status": "unknown", "errors": ["Robot not found"]}

# WebSocket handler to handle real-time communication
@socketio.on('message')
def handle_message(message):
    # Check if the message is asking for a robot's status
    if "status" in message.lower():
        # Use regular expression to capture the robot ID (e.g., "robot1", "robot2")
        match = re.search(r"(robot\d+)", message.lower())
        if match:
            robot_id = match.group(1)
            
            # Fetch robot status from mock database
            robot_status = robot_data.get(robot_id, {"status": "unknown", "errors": []})
            
            # Return a structured response based on the robot data
            response_text = f"Robot {robot_id} is {robot_status['status']} with errors: {', '.join(robot_status['errors'])}"
        else:
            # If no robot ID is found, give a default response
            response_text = "Robot ID not recognized. Please specify a valid robot."
    
    # Check if the message is asking about specific troubleshooting (e.g., motor failure)
    elif "motor failure" in message.lower():
        response_text = """
        To troubleshoot a motor failure:
        1. Check the motor's power supply: Ensure that the motor is receiving power.
        2. Inspect wiring: Look for any loose or damaged wiring.
        3. Check the motor's control system: Verify if the motor controller is working properly.
        4. Test the motor: If possible, perform a continuity test or swap the motor with a known working one.
        5. Look for overheating: Ensure the motor is not overheating and causing thermal shutdown.
        """
    
    # Handle more general troubleshooting with GPT-2
    else:
        # Encode the input message
        input_ids = tokenizer.encode(message, return_tensors="pt")

        # Generate a response using GPT-2
        output = model.generate(input_ids, max_length=150, num_return_sequences=1)

        # Decode the response
        response_text = tokenizer.decode(output[0], skip_special_tokens=True)

        # If the response is too long or too vague, refine it further
        if len(response_text) > 300:
            response_text = "The response seems too long. Here's a more concise version: " + response_text[:300]

    # Send the response back to the frontend
    emit('response', {'data': response_text})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
