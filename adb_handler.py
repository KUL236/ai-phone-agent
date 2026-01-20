"""
ADB Handler - Communicates with Android device via ADB
"""

import subprocess
import os

class ADBHandler:
    def __init__(self, adb_path=None):
        """Initialize ADB handler"""
        if adb_path is None:
            # Default path for user's ADB
            adb_path = r"C:\Users\giris\OneDrive\Desktop\dsa programming\first.c\.vscode\platform-tools\adb.exe"
            if not os.path.exists(adb_path):
                # Try to find adb in PATH or default Android SDK location
                self.adb_path = self._find_adb()
            else:
                self.adb_path = adb_path
        else:
            self.adb_path = adb_path
            
        self.device_id = None
        
    def _find_adb(self):
        """Find ADB executable"""
        # Common ADB locations
        common_paths = [
            "adb",  # In PATH
            os.path.expanduser("~/.android/adb"),
            "C:\\Android\\platform-tools\\adb.exe",
            os.environ.get("ANDROID_SDK_ROOT") + "\\platform-tools\\adb.exe" if os.environ.get("ANDROID_SDK_ROOT") else None,
        ]
        
        for path in common_paths:
            if path and self._is_valid_adb(path):
                return path
        
        return "adb"  # Default to PATH
    
    def _is_valid_adb(self, path):
        """Check if path is valid ADB"""
        try:
            subprocess.run([path, "version"], capture_output=True, timeout=2)
            return True
        except:
            return False
    
    def _run_command(self, cmd):
        """Run ADB command"""
        try:
            result = subprocess.run([self.adb_path] + cmd, capture_output=True, text=True, timeout=10)
            return result.stdout.strip(), result.returncode
        except Exception as e:
            return str(e), 1
    
    def connect_device(self):
        """Connect to device"""
        output, code = self._run_command(["devices"])
        print(output)
        
        if code == 0 and "device" in output:
            # Extract device ID
            for line in output.split('\n'):
                if 'device' in line and not line.startswith('*'):
                    self.device_id = line.split('\t')[0]
                    return True
        return False
    
    def send_text(self, text):
        """Send text to device (for input fields)"""
        # Escape special characters
        text = text.replace('"', '\\"')
        output, code = self._run_command(["shell", "input", "text", text])
        return code == 0
    
    def send_key(self, key_code):
        """Send key code to device"""
        output, code = self._run_command(["shell", "input", "keyevent", str(key_code)])
        return code == 0
    
    def tap(self, x, y):
        """Tap on device screen"""
        output, code = self._run_command(["shell", "input", "tap", str(x), str(y)])
        return code == 0
    
    def open_app(self, package_name):
        """Open an app by package name"""
        output, code = self._run_command(["shell", "monkey", "-p", package_name, "-c", "android.intent.category.LAUNCHER", "1"])
        return code == 0
    
    def make_call(self, phone_number):
        """Make a call"""
        output, code = self._run_command(["shell", "am", "start", "-a", "android.intent.action.CALL", f"-d tel:{phone_number}"])
        return code == 0
    
    def send_sms(self, phone_number, message):
        """Send SMS"""
        # This is complex, might need intent-based approach
        output, code = self._run_command(["shell", "am", "start", "-a", "android.intent.action.SENDTO", "-d", f"smsto:{phone_number}", "--es", "sms_body", message])
        return code == 0
    
    def take_screenshot(self):
        """Take screenshot of device"""
        output, code = self._run_command(["shell", "screencap", "-p", "/sdcard/screen.png"])
        if code == 0:
            # Pull image from device
            output, code = self._run_command(["pull", "/sdcard/screen.png", "screenshot.png"])
            print("📸 Screenshot saved as screenshot.png")
            return True
        return False
    
    def get_screen_text(self):
        """Get text content from screen (requires OCR)"""
        # TODO: Implement OCR using pytesseract or similar
        pass
