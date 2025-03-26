# bad-pico
<img src="https://github.com/user-attachments/assets/a86fc9e2-eaeb-43d1-bf7c-59b97f7b021f" alt="IMG_01" width="900">

# Requirements
- Raspberry Pi Pico
- USB-Type-C to USB-Type-A Cable

# Setup
1. Plug the Raspberry Pi Pico into the USB-A port on your computer while pressing the `BOOT` Button
   <img src="https://github.com/user-attachments/assets/00609bc7-cc77-4fff-b4cd-5bc89dda5416" alt="IMG_02" width="400"/>
2. Download the circuit python `.UF2` from https://circuitpython.org/board/raspberry_pi_pico/
3. Copy the `.UF2` file into the root directory of `RPI-RP2`
4. Now the `RPI-RP2` should disconnect and reconnect as `CIRCUITPY`
6. To use the German keyboard layout, copy the two files inside the <a href="https://github.com/michael-koll/bad-pico/tree/4c00515756e9ed61a6abb8118db1a340638ca387/layout_files_win_gr-py">layout_files_win_gr-py</a> into the `lib` folder of `CIRCUITPY`
   (for other languages visit https://www.neradoc.me/layouts/)
8. Copy the folder <a href="https://github.com/michael-koll/bad-pico/tree/db70f938178029ae3bb420612fd6c7bf1faba3ff/adafruit_hid">adafruit_hid</a> into the `lib` folder of `CIRCUITPY`
9. At the end the `lib` folder of `CIRCUITPY` should look like this:                                                              
   <img src="https://github.com/user-attachments/assets/3431ad20-ae2b-4675-ab96-ed65198769d2" alt="IMG_05" width="400"/>
10. Copy the content of <a href="https://github.com/michael-koll/bad-pico/blob/bc51192bd2319b3314d5a06a7a27a85003dfbb65/payload.py">payload.py</a> into `code.py` of `CIRCUITPY`
11. Be careful! As soon as you save the `code.py` file, the payload will be executed on your system!

# PoC
https://github.com/user-attachments/assets/72e36a18-3666-4309-83b7-3370d165699b
