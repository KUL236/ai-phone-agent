"""
Test basic AI agent without speech recognition
"""

from adb_handler import ADBHandler
from task_manager import TaskManager
from ai_brain import AIBrain
from app_controller import AppController

print("✅ Imports successful!")

# Test AI Brain
ai = AIBrain()

# Test some commands
test_commands = [
    "send message to john hey how are you",
    "call mom",
    "open whatsapp",
    "add task buy groceries",
    "show my tasks",
]

print("\n🧠 Testing AI Brain:")
for cmd in test_commands:
    intent, params = ai.understand(cmd)
    print(f"Command: '{cmd}'")
    print(f"  Intent: {intent}")
    print(f"  Params: {params}\n")

# Test Task Manager
print("\n📋 Testing Task Manager:")
tm = TaskManager()
tm.add_task("Drink water")
tm.add_task("Exercise 30 mins")
tasks = tm.get_today_tasks()
print(f"Today's tasks: {[t['text'] for t in tasks]}")
