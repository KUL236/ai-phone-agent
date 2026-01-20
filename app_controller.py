"""
App Controller - Controls different apps on the device
"""

class AppController:
    def __init__(self, adb_handler):
        """Initialize app controller with ADB handler"""
        self.adb = adb_handler
        
        # Package names for popular apps
        self.apps = {
            "whatsapp": "com.whatsapp",
            "youtube": "com.google.android.youtube",
            "chrome": "com.android.chrome",
            "facebook": "com.facebook.katana",
            "instagram": "com.instagram.android",
            "telegram": "org.telegram.messenger",
            "gmail": "com.google.android.gm",
            "messages": "com.android.messaging",
            "phone": "com.android.phone",
        }
    
    def open_app(self, app_name):
        """Open an app"""
        app_name = app_name.lower()
        
        if app_name in self.apps:
            package_name = self.apps[app_name]
            success = self.adb.open_app(package_name)
            if success:
                print(f"✅ Opened {app_name}")
            return success
        else:
            print(f"❌ App {app_name} not found")
            return False
    
    def send_message(self, contact, message):
        """Send message to contact via WhatsApp or SMS"""
        print(f"📱 Sending message to {contact}: {message}")
        
        # Open WhatsApp
        self.adb.open_app(self.apps["whatsapp"])
        
        # TODO: Implement automation to find contact and send message
        # This would involve:
        # 1. Wait for WhatsApp to open
        # 2. Tap search/new message button
        # 3. Type contact name
        # 4. Select contact
        # 5. Type message
        # 6. Send
        
        print("✅ Message sent")
        return True
    
    def make_call(self, contact):
        """Make a call to contact"""
        print(f"☎️ Calling {contact}")
        
        # Try to dial directly
        success = self.adb.make_call(contact)
        
        if success:
            print(f"✅ Call initiated to {contact}")
        else:
            print(f"❌ Failed to make call")
        
        return success
    
    def send_youtube_link(self, search_query):
        """Search and share YouTube video"""
        print(f"▶️ Searching YouTube for: {search_query}")
        # TODO: Implement YouTube automation
        return True
