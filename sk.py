
import sys
import subprocess
from pynput.keyboard import Controller, Key
import time

keyboard_controller = Controller()

def send_skype_message( message):
    """Send a custom message to a specific contact on Skype"""
    subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe"])
    time.sleep(3)
    keyboard_controller.type(message)
    keyboard_controller.press(Key.enter)
    keyboard_controller.release(Key.enter)
    print(f"Sent '{message}' to on Skype")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python send_skype_message.py <message>")
        sys.exit(1)
    
    message = sys.argv[1]
    
    send_skype_message( message)
