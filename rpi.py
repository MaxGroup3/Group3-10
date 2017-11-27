import pifacecad
import os
import signal
import sys

# you can ignore these three lines of code
# they are needed so that you can end the
# program by pressing Ctrl+C
def signal_handler(signal, frame):
    if sys.version_info < (3,0):
        # the python2 code forks
        os.kill(os.getppid(),9)
    os.kill(os.getpid(),9)
signal.signal(signal.SIGINT, signal_handler)

# event handler that is called after a button is
# pressed. The event handler is linked to the
# button press by listener.register(...) below

def update_pin_text(event):
        outputs = ["I am your father!",
                        "Do you feel lucky,punk?",
                        "Engage.",
                        "I'll be back.",
                        "The name is Bond."]
        event.chip.lcd.set_cursor(0, 0)
        event.chip.lcd.clear()
        event.chip.lcd.write(str(outputs[event.pin_num]))

cad = pifacecad.PiFaceCAD()
#cad.lcd.write("You pressed: ")
listener = pifacecad.SwitchEventListener(chip=cad)
# the display has eight buttons:
# five dip switchtes
# left, right and push for the three-way dip dwitch
outputs = ["I am your father!", "Do you feel lucky, punk?", "Engage.", "I/'ll b$
for i in range(5):
        listener.register(i, pifacecad.IODIR_FALLING_EDGE, update_pin_text)
listener.activate()

