"""
TESTING GUIDE - AI Phone Agent on Your Mobile Device
=====================================================

Follow these steps to test the agent on your Android phone:
"""

print("""
╔══════════════════════════════════════════════════════════════╗
║     AI PHONE AGENT - TESTING GUIDE                           ║
╚══════════════════════════════════════════════════════════════╝

STEP 1: PREPARE YOUR PHONE
─────────────────────────
1. Go to Settings → About Phone
2. Find "Build Number" and tap it 7 times
3. Go back to Settings → Developer Options
4. Enable "USB Debugging"
5. Enable "Wireless Debugging" (optional - for wireless testing)

STEP 2: CONNECT YOUR PHONE
──────────────────────────
1. Connect phone via USB cable to your computer
2. A prompt will appear on phone asking to trust this computer
3. Tap "Allow" or "Trust"
4. Run: adb devices
   You should see your phone listed

STEP 3: VERIFY CONNECTION
─────────────────────────
Run: python verify_connection.py

This will check:
✓ Device is connected
✓ Can access contacts
✓ Can access messages
✓ Can access device info
✓ Can send commands to phone

STEP 4: TEST INDIVIDUAL FEATURES
─────────────────────────────────
Run: python test_phone_features.py

This will test:
✓ Taking screenshots
✓ Reading contacts
✓ Reading messages
✓ Getting device info
✓ Making calls
✓ Opening apps

STEP 5: TEST VOICE COMMANDS
───────────────────────────
Run: python main.py

Then say commands like:
• "call mom"
• "send message to john hello"
• "open whatsapp"
• "show my contacts"
• "read messages"
• "device info"
• "add task buy milk"

TROUBLESHOOTING
───────────────

❌ "Device not found"
   → Check if USB cable is properly connected
   → Try: adb kill-server && adb devices
   → Check phone for trust prompt

❌ "Permission denied"
   → Enable USB Debugging on phone
   → Revoke USB Debugging authorization and reconnect
   → Tap "Allow" on phone when prompted

❌ "No module named speech_recognition"
   → Run: pip install SpeechRecognition pyttsx3

❌ "Voice commands not working"
   → Check microphone is connected
   → Check audio permissions on Windows
   → Test with demo.py first

ADVANCED TESTING
────────────────
1. Test with demo.py to verify AI understanding
2. Test with test_phone_features.py before using main.py
3. Monitor ADB logcat: adb logcat | grep AI
""")
