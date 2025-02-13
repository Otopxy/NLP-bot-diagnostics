# NLP-Powered Chatbot for Robot Diagnostics

This project is an NLP-powered chatbot built to assist with robot diagnostics and troubleshooting. The chatbot uses GPT-2, a transformer-based language model, to generate responses to common robot issues such as status checks and error troubleshooting. The chatbot can help users identify and resolve issues with robots by providing relevant solutions and instructions based on error messages and robot statuses.

The project leverages Python, Flask, and WebSockets for real-time communication, making it an ideal tool for building web-based automation systems and troubleshooting interfaces in robotics environments.

## Table of Contents
Installation
Features
Usage
Technologies
License
Installation
Prerequisites
Python 3.x
Pip (Python's package installer)

1. Clone the Repository
```
git clone https://github.com/otopxy/nlp-bot-diagnostics.git
cd nlp-bot-diagnostics
```
2. Install Dependencies
Use pip to install the necessary dependencies:

```
pip install -r requirements.txt
```

3. Run the Application
You can start the application by running the following command:

```
python app.py
```

The app will run on ``` http://localhost:5001. ``` Open the URL in your web browser to interact with the chatbot.

## Features
NLP-based Chatbot: Uses GPT-2 to generate dynamic responses for common robot diagnostics queries.
Real-time Communication: WebSocket integration allows for real-time user interactions.
Robot Status: Users can check the status of robots (e.g., robot1, robot2) and get information about errors or performance issues.
Troubleshooting Guides: Provides step-by-step troubleshooting instructions for issues like motor failure, sensor malfunctions, and more.
Extensible: The project is easily extendable to integrate with other robot diagnostic tools, databases, or external systems.

## Usage
Once the app is running, you can open the front-end interface in your web browser. The chatbot listens for user inputs, such as:

```
Checking robot status: "What is the status of robot1?"
Requesting troubleshooting advice: "How do I fix motor failure?"
Asking for general diagnostic information: "robot2 issues"
Sample Interaction
vbnet
Copy
Edit
You: robot1
Bot: Robot robot1 is running with errors: motor failure

You: How do I fix robot1 motor failure?
Bot: To troubleshoot a motor failure:
1. Check the motor's power supply: Ensure that the motor is receiving power.
2. Inspect wiring: Look for any loose or damaged wiring.
3. Check the motor's control system: Verify if the motor controller is working properly.
4. Test the motor: If possible, perform a continuity test or swap the motor with a known working one.
5. Look for overheating: Ensure the motor is not overheating and causing thermal shutdown.
```

## Technologies
Python 3.x: Core programming language used for building the application.
Flask: Lightweight web framework to serve the app and handle WebSocket connections.
WebSocket: For real-time communication between the frontend and backend.
GPT-2: Pre-trained transformer-based language model used for generating troubleshooting responses.
Hugging Face Transformers: Python library for using pre-trained models like GPT-2.
PyTorch: Deep learning framework used to run GPT-2.

