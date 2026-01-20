"""
Voice Handler - Speech recognition and text-to-speech
"""

try:
    import speech_recognition as sr
    SPEECH_AVAILABLE = True
except ImportError:
    SPEECH_AVAILABLE = False

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

class VoiceHandler:
    def __init__(self):
        """Initialize voice recognition and TTS"""
        if SPEECH_AVAILABLE:
            self.recognizer = sr.Recognizer()
        else:
            self.recognizer = None
        
        if TTS_AVAILABLE:
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('rate', 150)
        else:
            self.tts_engine = None
        
    def listen(self, timeout=5):
        """Listen for voice command"""
        if not SPEECH_AVAILABLE:
            print("❌ SpeechRecognition not available. Please install it.")
            return input("Enter command instead: ")
        
        try:
            with sr.Microphone() as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.1)
                audio = self.recognizer.listen(source, timeout=timeout)
            
            # Try Google Speech Recognition
            text = self.recognizer.recognize_google(audio)
            return text
            
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that")
            return ""
        except sr.RequestError as e:
            print(f"Error with speech recognition: {e}")
            return ""
    
    def speak(self, text):
        """Convert text to speech"""
        if not TTS_AVAILABLE:
            print(f"🔊 {text}")
            return
        
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print(f"Error in speech: {e}")
    
    def listen_continuous(self):
        """Listen continuously for commands"""
        while True:
            command = self.listen()
            if command:
                yield command
