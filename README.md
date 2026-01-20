# AI Phone Agent

Control your Android phone with voice commands from your computer!

## Features

- **Voice Commands** - Talk to control your phone (e.g., "Call mom", "Open WhatsApp")
- **Make Calls & Send Messages** - Call contacts or send text messages
- **App Control** - Open any app installed on your phone
- **Task Management** - Add and manage daily tasks
- **Access Phone Data** - Read contacts, messages, call history
- **Device Info** - Check battery, device model, Android version
- **Screenshots** - Capture device screen automatically

## Requirements

- Windows PC with Python 3.8+
- Android phone with USB Debugging enabled
- ADB (Android Debug Bridge) - included in Android SDK
- USB cable to connect phone to PC

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-phone-agent.git
   cd ai-phone-agent
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Android phone:**
   - Go to Settings → About Phone
   - Tap "Build Number" 7 times to enable Developer Mode
   - Go to Settings → Developer Options
   - Enable "USB Debugging"
   - Connect phone to PC via USB
   - Allow the trust prompt on your phone

4. **Verify connection:**
   ```bash
   python verify_connection.py
   ```

## Usage

### Start the AI Agent

```bash
python main.py
```

Then speak commands naturally:

**Calling:**
- "Call mom"
- "Dial john"
- "Phone dad"

**Messaging:**
- "Send message to john hello how are you"
- "Text mom i am coming"
- "WhatsApp sarah hi"

**Apps:**
- "Open WhatsApp"
- "Launch YouTube"
- "Start Chrome"

**Tasks:**
- "Add task buy groceries"
- "Remind me to study"
- "Show tasks"

**Information:**
- "Show contacts"
- "Read messages"
- "Device info"
- "Call history"
- "Battery status"

**Other:**
- "Take screenshot"
- "Stop" (to exit)

### Test Without Phone

To test the AI understanding without a phone:

```bash
python demo.py
```

Type commands instead of speaking.

### Verify Phone Connection

```bash
python verify_connection.py
```

### Test All Features

```bash
python test_phone_features.py
```

## Project Structure

```
ai-phone-agent/
├── main.py                 # Main entry point
├── adb_handler.py         # ADB communication
├── voice_handler.py       # Speech recognition & TTS
├── ai_brain.py            # Intent recognition
├── app_controller.py      # App automation
├── task_manager.py        # Task management
├── device_info.py         # Phone data access
├── demo.py                # Demo mode
├── verify_connection.py   # Connection verification
├── test_phone_features.py # Feature testing
└── requirements.txt       # Python dependencies
```

## Troubleshooting

### Device Not Found
- Check USB cable connection
- Enable USB Debugging on phone
- Try unplugging and replugging
- Allow the trust prompt on phone

### Voice Commands Not Working
- Install SpeechRecognition: `pip install SpeechRecognition pyttsx3`
- Check microphone is connected
- Check internet connection (for Google Speech API)
- Test with `python demo.py` first

### Contacts/Messages Not Accessible
- Check app permissions on Android
- This is a common Android permission issue
- Agent will still work for other features

### Permission Denied
- Revoke USB Debugging and reconnect phone
- Allow the trust prompt again

## Configuration

Edit these files to customize:

- `ai_brain.py` - Add more command patterns
- `app_controller.py` - Add more app support
- `device_info.py` - Access different phone data
- `adb_handler.py` - Change ADB path if needed

## Examples

### Example 1: Make a Call
```
User: "Call mom"
Agent: Dials mom's number on the phone
```

### Example 2: Send a Message
```
User: "Send message to john hey how are you"
Agent: Opens WhatsApp and sends message to john
```

### Example 3: Manage Tasks
```
User: "Add task buy groceries"
Agent: Saves task locally
User: "Show tasks"
Agent: Displays all pending tasks
```

## Limitations

- Voice recognition requires internet connection
- Some features need app permissions on Android
- Works with phones connected via USB
- Wireless debugging support coming soon

## Future Enhancements

- WiFi/Wireless debugging support
- Email integration
- Calendar event management
- More detailed task scheduling
- Better NLU with machine learning
- Mobile app for easier control

## Contributing

Feel free to:
- Add more command patterns
- Support more apps
- Improve voice recognition
- Add new features

Just fork, modify, and submit a pull request!

## License

MIT License - feel free to use this project

## Author

Created for controlling Android devices via voice commands

## Support

If you encounter issues:
1. Check the troubleshooting section
2. Run `python verify_connection.py`
3. Check `quick_start.py` for detailed guide

Enjoy controlling your phone with voice! 🎉
