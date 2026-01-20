"""
AI Agent Demo - Interactive Test Mode
"""

from ai_brain import AIBrain
from task_manager import TaskManager

def demo():
    print("=" * 60)
    print("🤖 AI PHONE AGENT - DEMO MODE")
    print("=" * 60)
    print("\nThis is a demo of the AI understanding capabilities")
    print("Commands to try:")
    print("  - 'send message to john hello'")
    print("  - 'call mom'")
    print("  - 'open whatsapp'")
    print("  - 'add task buy milk'")
    print("  - 'show tasks'")
    print("  - 'screenshot'")
    print("  - 'show contacts' (access your contacts)")
    print("  - 'read messages' (access your SMS)")
    print("  - 'device info' (phone battery, model, etc)")
    print("  - 'call history' (recent calls)")
    print("  - 'exit' to quit\n")
    
    ai = AIBrain()
    tm = TaskManager()
    
    while True:
        try:
            command = input("🎤 Say a command: ").strip()
            
            if command.lower() in ['exit', 'quit', 'stop']:
                print("Goodbye! 👋")
                break
            
            if not command:
                continue
            
            # Process command
            intent, params = ai.understand(command)
            
            print(f"\n📊 Analysis:")
            print(f"  Intent: {intent}")
            print(f"  Parameters: {params}")
            
            # Simulate actions
            if intent == "send_message":
                contact = params.get('contact', 'unknown')
                message = params.get('message', 'hi')
                print(f"✅ Simulated: Sending '{message}' to {contact} via WhatsApp")
            
            elif intent == "make_call":
                contact = params.get('contact', 'unknown')
                print(f"✅ Simulated: Calling {contact}")
            
            elif intent == "open_app":
                app = params.get('app_name', 'unknown')
                print(f"✅ Simulated: Opening {app}")
            
            elif intent == "get_tasks":
                tasks = tm.get_pending_tasks()
                if tasks:
                    print(f"✅ Your pending tasks:")
                    for task in tasks:
                        print(f"   - {task['text']}")
                else:
                    print("✅ No pending tasks!")
            
            elif intent == "add_task":
                task_text = params.get('task', 'unnamed task')
                tm.add_task(task_text)
                print(f"✅ Task added!")
            
            elif intent == "screenshot":
                print(f"✅ Simulated: Taking screenshot")
            
            elif intent == "get_contacts":
                print(f"✅ Simulated: Reading contacts from phone")
            
            elif intent == "get_messages":
                print(f"✅ Simulated: Reading SMS messages from phone")
            
            elif intent == "get_device_info":
                print(f"✅ Simulated: Getting device information (model, battery, etc)")
            
            elif intent == "get_call_logs":
                print(f"✅ Simulated: Getting call history")
            
            else:
                print(f"❓ Unknown command")
            
            print()
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    demo()
