import time
from pynput.keyboard import Controller, Listener, Key

# Starting number
counter = 1708

## Keyboard controller
keyboard = Controller()

# Flag to control the macro
running = False

def start_typing():
    global running, counter
    running = True
    while running:
        # Type the current counter value and press Enter
        keyboard.type(str(counter))
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        counter += 1
        time.sleep(2)  # Wait 2 seconds before typing the next number

def on_press(key):
    global running
    try:
        if key.char == 's':  # Start typing when 's' is pressed
            if not running:
                print("Starting typing...")
                start_typing()
        elif key.char == 'q':  # Stop typing when 'q' is pressed
            running = False
            print("Stopped typing.")
    except AttributeError:
        pass

# Listener for keyboard events
with Listener(on_press=on_press) as listener:
    print("Press 's' to start and 'q' to stop.")
    listener.join()
