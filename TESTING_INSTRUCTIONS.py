"""
COMPLETE TESTING GUIDE - AI PHONE AGENT
"""

print("""
╔═══════════════════════════════════════════════════╗
║      TESTING GUIDE - AI PHONE AGENT               ║
╚═══════════════════════════════════════════════════╝

OPTION 1: TEST WITHOUT PHONE (DEMO MODE)
════════════════════════════════════════

This tests the AI understanding without needing a phone.

Run:
  python demo.py

Then type commands:
  - "call mom"
  - "send message to john hello"
  - "open whatsapp"
  - "show contacts"
  - "device info"
  - "add task buy milk"
  - "show tasks"
  - "exit" to quit

What it tests:
✓ AI understands voice commands
✓ Correct intent recognition
✓ Parameter extraction
✓ Task management system


OPTION 2: VERIFY PHONE CONNECTION
═══════════════════════════════════

Before running main.py, test if phone is connected.

Requirements:
  1. Android phone with USB Debugging enabled
  2. Phone connected via USB cable
  3. Allowed the trust prompt

Run:
  python verify_connection.py

Expected output:
  ✓ Device connected
  ✓ Device info retrieved
  ✓ Contacts found (or "access denied" - ok)
  ✓ Messages found (or "access denied" - ok)
  ✓ Screenshot capability verified

If anything FAILS, troubleshoot below.


OPTION 3: TEST ALL PHONE FEATURES
═══════════════════════════════════

Comprehensive test of all features on your phone.

Run:
  python test_phone_features.py

This tests:
  ✓ Screenshots
  ✓ Device information
  ✓ Contacts access
  ✓ Messages access
  ✓ Call history
  ✓ Sending input/taps
  ✓ App opening
  ✓ Installed apps list


OPTION 4: RUN THE FULL AI AGENT
════════════════════════════════

Once verification passes, use with voice commands!

Run:
  python main.py

Then speak commands:
  🎤 "Call mom"
  🎤 "Open whatsApp"
  🎤 "Send message to john hey"
  🎤 "Show my contacts"
  🎤 "Device info"
  🎤 "Add task study python"
  🎤 "Stop" (to exit)

The agent will:
  1. Listen to your voice
  2. Understand the command
  3. Execute the action on your phone


OPTION 5: TEST BASIC AI UNDERSTANDING
══════════════════════════════════════

Test just the AI brain without phone or voice.

Run:
  python test_basic.py

This shows what commands the AI understands and how
it parses them.


QUICK TEST CHECKLIST
════════════════════

□ Step 1: python demo.py
  (Type: "call mom" → Should show: Intent: make_call)

□ Step 2: Enable USB Debugging on phone
  (Settings → Developer Options → USB Debugging ON)

□ Step 3: Connect phone via USB cable

□ Step 4: Allow trust prompt on phone

□ Step 5: python verify_connection.py
  (Should show: Device connected ✓)

□ Step 6: python test_phone_features.py
  (Should show multiple ✓ for each feature)

□ Step 7: python main.py
  (Say: "call mom" → Should dial)


TESTING DIFFERENT COMMANDS
═════════════════════════

CALLING:
  Say: "Call mom"
  Should: Dial mom's number on phone

MESSAGING:
  Say: "Send message to john hello there"
  Should: Open WhatsApp or messaging app

OPENING APPS:
  Say: "Open youtube"
  Should: Launch YouTube app

READING DATA:
  Say: "Show contacts"
  Should: Display contacts from phone

  Say: "Read messages"
  Should: Show recent SMS messages

MANAGING TASKS:
  Say: "Add task buy milk"
  Should: Save task locally

  Say: "Show tasks"
  Should: Display all tasks


TROUBLESHOOTING TESTS
═════════════════════

Issue: demo.py works but verify_connection.py fails
→ Phone not connected or USB Debugging not enabled

Issue: verify_connection.py works but main.py fails
→ Check microphone, test with demo.py

Issue: Phone says "not authorized"
→ Revoke USB permissions and reconnect phone
→ Allow the trust prompt again

Issue: "No device found"
→ Check USB cable connection
→ Enable USB Debugging: Settings → Developer Options
→ Restart ADB: adb kill-server

Issue: Commands not working
→ First test with demo.py (type instead of voice)
→ Check internet connection for speech recognition
→ Check microphone is connected

Issue: "Permission denied" for contacts/messages
→ This is normal on some Android versions
→ Agent still works for calling, messaging, apps


DETAILED TESTING FLOW
═════════════════════

1. START WITH DEMO:
   python demo.py
   Type: "call mom"
   Expected: Intent: make_call, Params: {contact: mom}

2. TEST AI PARSING:
   python test_basic.py
   Shows all command patterns and parsing

3. CHECK PHONE CONNECTION:
   python verify_connection.py
   Shows device connected and accessible

4. TEST PHONE FEATURES:
   python test_phone_features.py
   Tests screenshots, contacts, messages, etc.

5. RUN FULL AGENT:
   python main.py
   Use voice commands to control phone

6. TEST SPECIFIC COMMANDS:
   Just keep using main.py and try different commands


MANUAL TESTING
═══════════════

You can also test manually:

1. Test ADB directly:
   cd C:\\Users\\giris\\OneDrive\\Desktop\\dsa programming\\first.c\\.vscode\\platform-tools
   .\\adb.exe devices
   (Should show your phone)

2. Test voice recognition:
   python
   >>> from voice_handler import VoiceHandler
   >>> vh = VoiceHandler()
   >>> text = vh.listen()
   >>> print("You said:", text)

3. Test AI understanding:
   python
   >>> from ai_brain import AIBrain
   >>> ai = AIBrain()
   >>> intent, params = ai.understand("call mom")
   >>> print(intent, params)

4. Test task manager:
   python
   >>> from task_manager import TaskManager
   >>> tm = TaskManager()
   >>> tm.add_task("Buy groceries")
   >>> print(tm.get_pending_tasks())


SUCCESS INDICATORS
═══════════════════

✓ demo.py shows correct intents
✓ verify_connection.py shows "Device connected"
✓ test_phone_features.py shows multiple ✓
✓ main.py responds to voice commands
✓ Phone executes commands (calls, messages, apps)


FAILURE INDICATORS
═══════════════════

✗ demo.py shows "unknown" intent
  → Check ai_brain.py patterns

✗ verify_connection.py shows "No device"
  → Check USB connection and USB Debugging

✗ test_phone_features.py shows ✗ for everything
  → Check ADB path in adb_handler.py

✗ main.py doesn't recognize voice
  → Check microphone, test demo.py first

✗ main.py crashes
  → Check all imports with: python test_basic.py


NEXT STEPS AFTER TESTING
═════════════════════════

✓ If everything works:
  - Share project on GitHub (already done!)
  - Customize commands in ai_brain.py
  - Add more apps to app_controller.py
  - Add more device info in device_info.py

✓ If something fails:
  - Check troubleshooting above
  - Run verify_connection.py
  - Check the specific module that failed
  - Review error messages carefully

✓ To make improvements:
  - Add new command patterns to ai_brain.py
  - Add new apps to app_controller.py
  - Improve task management
  - Add more features


TESTING SUMMARY
════════════════

Start with:
1. python demo.py (test AI understanding)
2. python verify_connection.py (test phone connection)
3. python test_phone_features.py (test all features)
4. python main.py (test with voice)

If all pass → Your AI agent is ready! 🎉

Any failures → Check troubleshooting section above
""")

print("\n" + "="*60)
print("Ready to test? Start with:")
print("  python demo.py")
print("="*60)
