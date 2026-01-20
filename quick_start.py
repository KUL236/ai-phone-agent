"""
QUICK START - Get your AI Agent running in 5 minutes!
"""

QUICK_START = """
╔═══════════════════════════════════════════════════════════╗
║   AI PHONE AGENT - QUICK START GUIDE                      ║
║   Get it running in 5 minutes!                            ║
╚═══════════════════════════════════════════════════════════╝

PREPARATION (2 minutes)
══════════════════════════

Phone Setup:
1. Go to Settings → About Phone
2. Tap "Build Number" 7 times to enable Developer Mode
3. Go to Settings → Developer Options
4. Turn ON: "USB Debugging"
5. Connect phone to computer via USB cable
6. On phone: Tap "Allow" when asked to trust this computer

CHECK IF EVERYTHING WORKS (1 minute)
════════════════════════════════════

Run this command to verify:
$ python verify_connection.py

You should see:
✅ Device connected
✅ Device info retrieved
✅ Contacts found (or "access denied" is ok)
✅ Messages found (or "access denied" is ok)
✅ Call history found (or "access denied" is ok)

If any FAIL, read the troubleshooting below.

TEST FEATURES (1 minute)
════════════════════════

Run:
$ python test_phone_features.py

This tests all features before you use voice commands.

DEMO MODE (Optional - To practice without phone)
════════════════════════════════════════════════

Just test the AI understanding:
$ python demo.py

Try commands like:
- "call mom"
- "send message to john hello"
- "show contacts"

ACTUAL TESTING (1 minute)
═════════════════════════

Once verify_connection.py shows ✅, run:
$ python main.py

Then try voice commands:
🎤 "call mom"
🎤 "open whatsapp"
🎤 "send message to john hey"
🎤 "show contacts"
🎤 "device info"
🎤 "add task study python"
🎤 "stop" (to exit)

TROUBLESHOOTING
═══════════════

❌ "Device not found" / "Failed to connect"
───────────────────────────────────────
   Solution:
   1. Check USB cable is properly connected
   2. On phone: Settings → Developer Options → USB Debugging should be ON
   3. Try unplugging and replugging
   4. Check if there's a "Trust" dialog on phone - tap Allow
   5. Run: adb kill-server && adb devices

❌ "Permission denied"
───────────────────────
   Solution:
   1. Go to Settings → Apps → Permissions
   2. Revoke all permissions for ADB
   3. Disconnect and reconnect phone
   4. Tap "Allow" on trust prompt

❌ "Voice commands not working"
─────────────────────────────
   Solution:
   1. First run demo.py to check AI understanding works
   2. Check microphone is connected to computer
   3. Install speech recognition: pip install SpeechRecognition
   4. Test without phone first: python demo.py

❌ "Contacts/Messages not accessible"
──────────────────────────────────────
   Solution:
   1. This is often a permission issue on Android
   2. The agent will still work for other features
   3. You can still call, open apps, etc.
   4. Try allowing app permissions on phone

❌ "ADB not found"
──────────────────
   Solution:
   The path to ADB is already set in adb_handler.py
   If it still fails: 
   $ python
   >>> from adb_handler import ADBHandler
   >>> adb = ADBHandler()
   >>> adb.adb_path  # Should show the ADB path

COMMANDS REFERENCE
══════════════════

CALLING:
  - "call mom"
  - "dial john"
  - "phone dad"

MESSAGING:
  - "send message to john hello how are you"
  - "text mom i am coming"
  - "whatsapp sarah hi"

APPS:
  - "open whatsapp"
  - "launch youtube"
  - "start chrome"

TASKS:
  - "add task buy groceries"
  - "remind me to study"
  - "show tasks"

INFO:
  - "show contacts"
  - "read messages"
  - "device info"
  - "call history"
  - "battery status"

SCREENSHOTS:
  - "take screenshot"
  - "capture screen"

TIPS & TRICKS
═════════════

✓ Test with demo.py first to practice commands
✓ Use "stop" to exit the agent
✓ Say commands clearly and slowly
✓ Check demo.py output to see what the AI understood
✓ Keep phone nearby and unlocked during testing
✓ Some commands may need app permissions on phone

ADVANCED
════════

To see what's happening:
$ python test_phone_features.py  # Tests all features
$ adb shell command                # Run raw ADB commands
$ adb logcat                        # View phone logs

Feel free to modify:
- ai_brain.py: Add more command patterns
- app_controller.py: Add more apps
- device_info.py: Access more phone data

Happy testing! 🎉
"""

if __name__ == "__main__":
    print(QUICK_START)
    
    # Also save to file
    with open("QUICK_START.txt", "w") as f:
        f.write(QUICK_START)
    print("\n✅ Quick start guide saved to QUICK_START.txt")
