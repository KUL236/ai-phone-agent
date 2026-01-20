"""
Test Phone Features - Test individual features one by one
"""

from adb_handler import ADBHandler
from device_info import DeviceInfoManager
from app_controller import AppController
import time

def test_features():
    print("=" * 70)
    print("🧪 TESTING AI AGENT PHONE FEATURES")
    print("=" * 70)
    
    adb = ADBHandler()
    device_info = DeviceInfoManager(adb)
    apps = AppController(adb)
    
    # Connect
    print("\n[SETUP] Connecting to device...")
    if not adb.connect_device():
        print("❌ Failed to connect! Exiting...")
        return
    print(f"✅ Connected: {adb.device_id}")
    
    # Test 1: Screenshot
    print("\n" + "─" * 70)
    print("[TEST 1] SCREENSHOT")
    print("─" * 70)
    print("📸 Taking screenshot...")
    if adb.take_screenshot():
        print("✅ Screenshot taken! Check 'screenshot.png'")
    else:
        print("❌ Screenshot failed")
    
    # Test 2: Device Info
    print("\n" + "─" * 70)
    print("[TEST 2] DEVICE INFORMATION")
    print("─" * 70)
    info = device_info.get_device_info()
    if info:
        print("✅ Device Info Retrieved:")
        for key, value in info.items():
            print(f"   📌 {key}: {value}")
    
    # Test 3: Contacts
    print("\n" + "─" * 70)
    print("[TEST 3] CONTACTS")
    print("─" * 70)
    contacts = device_info.get_contacts()
    print(f"✅ Found {len(contacts)} contacts")
    if contacts:
        print(f"   First 5 contacts:")
        for i, contact in enumerate(contacts[:5], 1):
            print(f"   {i}. {contact}")
    
    # Test 4: Messages
    print("\n" + "─" * 70)
    print("[TEST 4] SMS MESSAGES")
    print("─" * 70)
    messages = device_info.get_messages(limit=10)
    print(f"✅ Found {len(messages)} messages")
    if messages:
        print(f"   Recent messages:")
        for i, msg in enumerate(messages[:5], 1):
            print(f"   {i}. {msg}")
    
    # Test 5: Call Logs
    print("\n" + "─" * 70)
    print("[TEST 5] CALL HISTORY")
    print("─" * 70)
    calls = device_info.get_call_logs(limit=10)
    print(f"✅ Found {len(calls)} call logs")
    if calls:
        print(f"   Recent calls:")
        for i, call in enumerate(calls[:5], 1):
            print(f"   {i}. {call}")
    
    # Test 6: Send Tap Command
    print("\n" + "─" * 70)
    print("[TEST 6] SEND INPUT")
    print("─" * 70)
    print("📱 Attempting to tap screen at (500, 500)...")
    if adb.tap(500, 500):
        print("✅ Tap command sent!")
    else:
        print("❌ Tap failed")
    
    # Test 7: Open App
    print("\n" + "─" * 70)
    print("[TEST 7] OPEN APP")
    print("─" * 70)
    print("📱 Attempting to open WhatsApp...")
    if apps.open_app("whatsapp"):
        print("✅ App opened!")
    else:
        print("ℹ️ App might not be installed or ADB permission issue")
    
    # Test 8: Installed Apps
    print("\n" + "─" * 70)
    print("[TEST 8] INSTALLED APPS")
    print("─" * 70)
    apps_list = device_info.get_installed_apps()
    print(f"✅ Found {len(apps_list)} installed apps")
    print(f"   First 10 apps:")
    for app in apps_list[:10]:
        print(f"   - {app}")
    
    print("\n" + "=" * 70)
    print("✅ ALL TESTS COMPLETED!")
    print("=" * 70)
    print("\n🎤 Ready to use voice commands!")
    print("Run: python main.py")

if __name__ == "__main__":
    test_features()
