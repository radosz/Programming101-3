# mousepos.py (linux only)
"""module mousepos
"""
# uses the package python-xlib
# from http://snipplr.com/view/19188/mouseposition-on-linux-via-xlib/
from Xlib import display
import os


def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    yield data["root_x"], data["root_y"]


def beep():
    os.system("play -n synth 0.1 tri 250.0")

if __name__ == "__main__":
    while True:
        for a, b in mousepos():
            if a == 0 and b == 0:
                beep()
