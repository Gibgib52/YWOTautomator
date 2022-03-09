"""
    Moves mouse to scroll for you in your world of text. use YWOTautomate instead
"""

import mouse
import time

sWidth = 1920
sHeight = 1080


def scroll(direction):

    if(direction == "n"):
        pass
    elif(direction == "e"):
        mouse.drag(sWidth/2, sHeight/2, (sWidth/2)+500, sHeight/2, absolute=True, duration=0.01)
    elif(direction == "s"):
        pass
    elif(direction == "w"):
        pass

mouse.on_middle_click(scroll, args=("e"))
while True:
    time.sleep(0.025)
