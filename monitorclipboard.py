import pyperclip
import keyboard
import time

def print_clipboard_data(e):
    # Check if the ctrl key is being pressed
    if keyboard.is_pressed('ctrl'):
        # Add a small delay before retrieving the clipboard data
        time.sleep(0.1)
        # Get the clipboard data
        clipboard_data = pyperclip.paste()
        print(clipboard_data)

# Register the hotkey (ctrl+c) and the associated function
keyboard.on_press_key('c', print_clipboard_data, suppress=False)

# Block the program, keep it running
keyboard.wait()