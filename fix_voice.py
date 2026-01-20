"""
Troubleshooting Voice Commands Issue
"""

TROUBLESHOOTING = """
If voice commands are not working, follow these steps:

STEP 1: Check if SpeechRecognition is installed
─────────────────────────────────────────────
Run: pip list | findstr SpeechRecognition

You should see:
SpeechRecognition 3.10.0

If NOT found, install it:
pip install SpeechRecognition pyttsx3

STEP 2: Test voice recognition alone
──────────────────────────────────────
Create a test file and run:

from voice_handler import VoiceHandler
vh = VoiceHandler()
text = vh.listen()
print("You said:", text)

STEP 3: Check if Google APIs are accessible
────────────────────────────────────────────
The agent uses Google Speech Recognition which needs internet.
Make sure your computer has internet connection.

STEP 4: Check microphone
────────────────────────
1. Go to Windows Settings → Sound
2. Check if microphone is connected and working
3. Test microphone in Sound settings

STEP 5: Use demo mode first
──────────────────────────
If voice still doesn't work, use the demo:
python demo.py

This uses text input instead of voice.
You can type commands like: "call mom"

STEP 6: If voice still fails, use input mode
──────────────────────────────────────────────
The agent falls back to text input if voice fails.
Just type your commands instead of speaking.

COMMON ISSUES:
- No internet: Google Speech needs internet
- Microphone not detected: Check Windows Settings
- Module not installed: Run pip install SpeechRecognition
- Audio permission denied: Check Windows audio settings
"""

print(TROUBLESHOOTING)

# Quick install script
import subprocess
import sys

print("\n" + "="*60)
print("Installing required packages...")
print("="*60 + "\n")

packages = ["SpeechRecognition", "pyttsx3", "requests", "python-dotenv"]

for pkg in packages:
    print(f"Installing {pkg}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

print("\n✅ All packages installed!")
