"""
Web Server - AI Phone Agent
Accessible via website for anyone to use
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
from adb_handler import ADBHandler
from ai_brain import AIBrain
from device_info import DeviceInfoManager
from app_controller import AppController
from task_manager import TaskManager

app = Flask(__name__)
CORS(app)

# Initialize AI components
adb = ADBHandler()
ai_brain = AIBrain()
device_info = DeviceInfoManager(adb)
app_controller = AppController(adb)
task_manager = TaskManager()

# Store device connection status
device_connected = False

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/connect', methods=['POST'])
def connect_device():
    """Connect to Android device"""
    global device_connected
    
    try:
        device_connected = adb.connect_device()
        if device_connected:
            return jsonify({
                'status': 'success',
                'message': 'Device connected!',
                'device_id': adb.device_id
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'No device found. Check USB connection and USB Debugging.'
            }), 400
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/command', methods=['POST'])
def execute_command():
    """Execute voice command"""
    global device_connected
    
    if not device_connected:
        return jsonify({
            'status': 'error',
            'message': 'Device not connected'
        }), 400
    
    try:
        data = request.json
        command = data.get('command', '')
        
        if not command:
            return jsonify({
                'status': 'error',
                'message': 'No command provided'
            }), 400
        
        # Understand command
        intent, params = ai_brain.understand(command)
        
        result = {
            'status': 'success',
            'command': command,
            'intent': intent,
            'params': params,
            'message': f'Executed: {intent}'
        }
        
        # Execute based on intent
        if intent == "make_call":
            contact = params.get('contact', 'unknown')
            app_controller.make_call(contact)
            result['message'] = f'Calling {contact}'
        
        elif intent == "send_message":
            contact = params.get('contact', 'unknown')
            message = params.get('message', '')
            app_controller.send_message(contact, message)
            result['message'] = f'Message sent to {contact}: {message}'
        
        elif intent == "open_app":
            app_name = params.get('app_name', 'unknown')
            app_controller.open_app(app_name)
            result['message'] = f'Opened {app_name}'
        
        elif intent == "add_task":
            task = params.get('task', 'unnamed')
            task_manager.add_task(task)
            result['message'] = f'Task added: {task}'
        
        elif intent == "get_tasks":
            tasks = task_manager.get_pending_tasks()
            result['tasks'] = [t['text'] for t in tasks]
            result['message'] = f'Found {len(tasks)} tasks'
        
        elif intent == "get_device_info":
            info = device_info.get_device_info()
            result['device_info'] = info
            result['message'] = 'Device info retrieved'
        
        elif intent == "get_contacts":
            contacts = device_info.get_contacts()
            result['contacts'] = contacts[:10]  # Limit to 10
            result['message'] = f'Found {len(contacts)} contacts'
        
        elif intent == "get_messages":
            messages = device_info.get_messages()
            result['messages'] = messages[:10]  # Limit to 10
            result['message'] = f'Found {len(messages)} messages'
        
        elif intent == "get_call_logs":
            calls = device_info.get_call_logs()
            result['calls'] = calls[:10]  # Limit to 10
            result['message'] = f'Found {len(calls)} calls'
        
        elif intent == "screenshot":
            adb.take_screenshot()
            result['message'] = 'Screenshot taken'
        
        else:
            result['status'] = 'unknown'
            result['message'] = f'Unknown command: {intent}'
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    """Get connection status"""
    global device_connected
    
    return jsonify({
        'connected': device_connected,
        'device_id': adb.device_id if device_connected else None
    })

@app.route('/api/tasks', methods=['GET'])
def get_all_tasks():
    """Get all tasks"""
    tasks = task_manager.get_pending_tasks()
    return jsonify({
        'tasks': [{'id': t['id'], 'text': t['text']} for t in tasks]
    })

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def complete_task(task_id):
    """Mark task as complete"""
    try:
        task_manager.complete_task(task_id)
        return jsonify({
            'status': 'success',
            'message': f'Task {task_id} completed'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/examples', methods=['GET'])
def get_examples():
    """Get command examples"""
    examples = {
        'calling': [
            'Call mom',
            'Dial john',
            'Phone dad'
        ],
        'messaging': [
            'Send message to john hello',
            'Text mom i am coming',
            'WhatsApp sarah hi'
        ],
        'apps': [
            'Open whatsapp',
            'Launch youtube',
            'Start chrome'
        ],
        'tasks': [
            'Add task buy groceries',
            'Show tasks',
            'Remove task'
        ],
        'info': [
            'Show contacts',
            'Read messages',
            'Device info',
            'Battery status',
            'Call history'
        ]
    }
    return jsonify(examples)

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    print("=" * 60)
    print("AI PHONE AGENT - WEB SERVER")
    print("=" * 60)
    print("\nServer running at: http://localhost:5000")
    print("API Documentation at: http://localhost:5000/api/examples")
    print("\nEndpoints:")
    print("  POST /api/connect - Connect to phone")
    print("  POST /api/command - Execute command")
    print("  GET  /api/status - Check connection status")
    print("  GET  /api/tasks - Get all tasks")
    print("  GET  /api/examples - Get command examples")
    print("=" * 60)
    
    # Run the server
    app.run(debug=True, host='0.0.0.0', port=5000)
