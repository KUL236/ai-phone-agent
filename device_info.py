"""
Device Info Manager - Access personal information from Android device
"""

class DeviceInfoManager:
    def __init__(self, adb_handler):
        """Initialize device info manager"""
        self.adb = adb_handler
    
    def get_contacts(self):
        """Get all contacts from device"""
        # Use ADB to access contacts database
        output, code = self.adb._run_command([
            "shell",
            "content",
            "query",
            "--uri",
            "content://com.android.contacts/contacts"
        ])
        return self._parse_contacts(output)
    
    def _parse_contacts(self, output):
        """Parse contacts from ADB output"""
        contacts = []
        try:
            for line in output.split('\n'):
                if 'Row:' in line:
                    # Extract contact info
                    parts = line.split(',')
                    contact = {}
                    for part in parts:
                        if '=' in part:
                            key, value = part.split('=', 1)
                            contact[key.strip()] = value.strip()
                    if contact:
                        contacts.append(contact)
        except:
            pass
        return contacts
    
    def get_contact_by_name(self, name):
        """Search for contact by name"""
        output, code = self.adb._run_command([
            "shell",
            "content",
            "query",
            "--uri",
            "content://com.android.contacts/contacts",
            "--where",
            f"display_name LIKE '%{name}%'"
        ])
        return self._parse_contacts(output)
    
    def get_messages(self, limit=10):
        """Get recent messages/SMS"""
        output, code = self.adb._run_command([
            "shell",
            "content",
            "query",
            "--uri",
            "content://sms",
            "--sort",
            "_id DESC LIMIT " + str(limit)
        ])
        return self._parse_messages(output)
    
    def _parse_messages(self, output):
        """Parse SMS messages from ADB output"""
        messages = []
        try:
            for line in output.split('\n'):
                if 'Row:' in line:
                    msg = {}
                    parts = line.split(',')
                    for part in parts:
                        if '=' in part:
                            key, value = part.split('=', 1)
                            msg[key.strip()] = value.strip()
                    if msg:
                        messages.append(msg)
        except:
            pass
        return messages
    
    def get_calendar_events(self):
        """Get calendar events"""
        output, code = self.adb._run_command([
            "shell",
            "content",
            "query",
            "--uri",
            "content://com.android.calendar/events"
        ])
        return self._parse_events(output)
    
    def _parse_events(self, output):
        """Parse calendar events"""
        events = []
        try:
            for line in output.split('\n'):
                if 'Row:' in line:
                    event = {}
                    parts = line.split(',')
                    for part in parts:
                        if '=' in part:
                            key, value = part.split('=', 1)
                            event[key.strip()] = value.strip()
                    if event:
                        events.append(event)
        except:
            pass
        return events
    
    def get_device_info(self):
        """Get device information"""
        info = {}
        
        # Device model
        output, _ = self.adb._run_command(["shell", "getprop", "ro.product.model"])
        info['model'] = output.strip()
        
        # Android version
        output, _ = self.adb._run_command(["shell", "getprop", "ro.build.version.release"])
        info['android_version'] = output.strip()
        
        # Brand
        output, _ = self.adb._run_command(["shell", "getprop", "ro.product.brand"])
        info['brand'] = output.strip()
        
        # Serial
        output, _ = self.adb._run_command(["shell", "getprop", "ro.serialno"])
        info['serial'] = output.strip()
        
        # Battery
        output, _ = self.adb._run_command(["shell", "dumpsys", "battery"])
        info['battery'] = self._parse_battery(output)
        
        return info
    
    def _parse_battery(self, output):
        """Parse battery info"""
        battery_info = {}
        for line in output.split('\n'):
            if 'level:' in line:
                battery_info['level'] = line.split(':')[1].strip()
            elif 'status:' in line:
                battery_info['status'] = line.split(':')[1].strip()
            elif 'temperature:' in line:
                battery_info['temperature'] = line.split(':')[1].strip()
        return battery_info
    
    def get_installed_apps(self):
        """Get list of installed apps"""
        output, _ = self.adb._run_command(["shell", "pm", "list", "packages"])
        apps = []
        for line in output.split('\n'):
            if line.startswith('package:'):
                app_name = line.replace('package:', '').strip()
                apps.append(app_name)
        return apps
    
    def search_files(self, pattern="/sdcard/", file_type="*"):
        """Search for files on device"""
        output, _ = self.adb._run_command([
            "shell",
            "find",
            pattern,
            "-name",
            file_type,
            "-type",
            "f"
        ])
        files = [f.strip() for f in output.split('\n') if f.strip()]
        return files[:20]  # Return first 20 results
    
    def get_call_logs(self, limit=10):
        """Get call history"""
        output, _ = self.adb._run_command([
            "shell",
            "content",
            "query",
            "--uri",
            "content://call_log/calls",
            "--sort",
            "_id DESC LIMIT " + str(limit)
        ])
        calls = []
        try:
            for line in output.split('\n'):
                if 'Row:' in line:
                    call = {}
                    parts = line.split(',')
                    for part in parts:
                        if '=' in part:
                            key, value = part.split('=', 1)
                            call[key.strip()] = value.strip()
                    if call:
                        calls.append(call)
        except:
            pass
        return calls
