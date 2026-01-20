"""
AI Phone Agent - Main Entry Point
Controls Android device via ADB, listens to voice commands, manages tasks
"""

import sys
from adb_handler import ADBHandler
from voice_handler import VoiceHandler
from task_manager import TaskManager
from ai_brain import AIBrain
from app_controller import AppController
from device_info import DeviceInfoManager

class AIPhoneAgent:
    def __init__(self):
        self.adb = ADBHandler()
        self.voice = VoiceHandler()
        self.tasks = TaskManager()
        self.ai = AIBrain()
        self.apps = AppController(self.adb)
        self.device_info = DeviceInfoManager(self.adb)
        
    def start(self):
        """Start the AI agent"""
        print("🤖 AI Phone Agent Starting...")
        print("Connecting to device via ADB...")
        
        if not self.adb.connect_device():
            print("❌ Failed to connect to device")
            return
        
        print("✅ Device connected!")
        print("Listening for voice commands... (Say 'stop' to exit)")
        
        while True:
            try:
                # Listen for voice command
                command = self.voice.listen()
                
                if command.lower() == "stop":
                    print("Goodbye!")
                    break
                
                print(f"🎤 You said: {command}")
                
                # AI understands the command
                intent, action_params = self.ai.understand(command)
                print(f"🧠 Intent: {intent}")
                
                # Execute the action
                self.execute_action(intent, action_params)
                
            except Exception as e:
                print(f"❌ Error: {e}")
                
    def execute_action(self, intent, params):
        """Execute action based on AI understanding"""
        if intent == "send_message":
            self.apps.send_message(params['contact'], params['message'])
        elif intent == "make_call":
            self.apps.make_call(params['contact'])
        elif intent == "open_app":
            self.apps.open_app(params['app_name'])
        elif intent == "get_tasks":
            tasks = self.tasks.get_today_tasks()
            print(f"📋 Today's tasks: {tasks}")
        elif intent == "add_task":
            self.tasks.add_task(params['task'])
        elif intent == "screenshot":
            self.adb.take_screenshot()
        elif intent == "get_contacts":
            contacts = self.device_info.get_contacts()
            print(f"👥 Found {len(contacts)} contacts")
            for contact in contacts[:5]:
                print(f"  - {contact}")
        elif intent == "get_messages":
            messages = self.device_info.get_messages()
            print(f"📱 Recent messages: {len(messages)}")
            for msg in messages[:5]:
                print(f"  - {msg}")
        elif intent == "get_device_info":
            info = self.device_info.get_device_info()
            print(f"📱 Device Info:")
            for key, value in info.items():
                print(f"  {key}: {value}")
        elif intent == "get_call_logs":
            calls = self.device_info.get_call_logs()
            print(f"☎️ Recent calls: {len(calls)}")
            for call in calls[:5]:
                print(f"  - {call}")
        else:
            print(f"❓ Unknown intent: {intent}")

if __name__ == "__main__":
    agent = AIPhoneAgent()
    agent.start()
