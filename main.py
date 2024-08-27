import keyboard
import subprocess
from pynput.keyboard import Controller, Key
import time

keyboard_controller = Controller()

def open_vscode():
    """Open VS Code in the specified directory"""
    subprocess.run(["code", "dev/apps/fixperts"])
    print("VS Code opened in dev/apps/fixperts")

def send_gm_skype():
    """Open Skype and send 'Good Morning' message to Jad Al Shami"""
    subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe"])
    time.sleep(3)  
    keyboard_controller.type("Good Morning Mr.Jad. How are you.")
    keyboard_controller.press(Key.enter)
    keyboard_controller.release(Key.enter)
    print("Sent 'Good Morning' to Jad Al Shami on Skype")

def open_edge_tabs():
    """Open Edge browser with multiple tabs"""
    urls = [
        "https://outlook.office.com/",
        "https://mail.google.com",
        "https://supabase.com/dashboard/projects",
        "https://web.whatsapp.com",
        "https://github.com/Kythonlk?tab=repositories"
    ]
    for url in urls:
        subprocess.Popen(["start", "msedge", url], shell=True)
    print("Opened Edge with GitHub, Outlook, Gmail, Supabase, and WhatsApp Web")

def open_settings_hotspot():
    """Open Settings and turn on mobile hotspot"""
    subprocess.run(["start", "ms-settings:network-mobilehotspot"], shell=True)
    time.sleep(2)
    keyboard_controller.press(Key.space)
    keyboard_controller.release(Key.space)
    print("Mobile hotspot turned on")

keyboard.add_hotkey('ctrl+tab+v', open_vscode)
keyboard.add_hotkey('ctrl+tab+s', send_gm_skype)
keyboard.add_hotkey('ctrl+tab+e', open_edge_tabs)
keyboard.add_hotkey('ctrl+tab+h', open_settings_hotspot)

print("Hotkeys set up:")
print("CTRL+ALT+V: Open VS Code")
print("CTRL+ALT+S: Send Good Morning on Skype")
print("CTRL+ALT+E: Open Edge with multiple tabs")
print("CTRL+ALT+H: Open Settings and turn on mobile hotspot")

keyboard.wait('esc')  
