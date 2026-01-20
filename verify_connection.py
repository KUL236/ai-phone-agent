"""
Verify Connection - Test if phone is properly connected to AI agent
"""

from adb_handler import ADBHandler
from device_info import DeviceInfoManager

def verify_connection():
    print("=" * 60)
    print("🔍 VERIFYING AI PHONE AGENT CONNECTION")
    print("=" * 60)
    
    # Initialize
    adb = ADBHandler()
    
    # Test 1: Device Connection
    print("\n[1] Checking device connection...")
    if adb.connect_device():
        print(f"✅ Device connected! ID: {adb.device_id}")
    else:
        print("❌ No device found!")
        print("   Make sure:")
        print("   - Phone is connected via USB")
        print("   - USB Debugging is enabled")
        print("   - You tapped 'Allow' on the phone")
        return
    
    # Test 2: Get Device Info
    print("\n[2] Retrieving device information...")
    device_info = DeviceInfoManager(adb)
    info = device_info.get_device_info()
    if info:
        print("✅ Device info retrieved!")
        for key, value in info.items():
            print(f"   {key}: {value}")
    else:
        print("❌ Could not get device info")
    
    # Test 3: Access Contacts
    print("\n[3] Accessing contacts...")
    contacts = device_info.get_contacts()
    if contacts:
        print(f"✅ Found {len(contacts)} contacts!")
        print(f"   First 3 contacts: {contacts[:3]}")
    else:
        print("⚠️ No contacts found or access denied")
    
    # Test 4: Access Messages
    print("\n[4] Accessing SMS messages...")
    messages = device_info.get_messages(limit=5)
    if messages:
        print(f"✅ Found {len(messages)} messages!")
        print(f"   First message: {messages[0]}")
    else:
        print("⚠️ No messages found or access denied")
    
    # Test 5: Take Screenshot
    print("\n[5] Testing screenshot...")
    if adb.take_screenshot():
        print("✅ Screenshot saved as 'screenshot.png'")
    else:
        print("❌ Screenshot failed")
    
    # Test 6: Call Logs
    print("\n[6] Accessing call history...")
    calls = device_info.get_call_logs(limit=5)
    if calls:
        print(f"✅ Found {len(calls)} call logs!")
        print(f"   Recent calls: {calls[:2]}")
    else:
        print("⚠️ No call logs found")
    
    print("\n" + "=" * 60)
    print("✅ VERIFICATION COMPLETE")
    print("=" * 60)
    print("\nYou can now run: python main.py")
    print("And use voice commands to control your phone!")

if __name__ == "__main__":
    verify_connection()
