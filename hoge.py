from microbit import *

display.show(Image.HAPPY)

while True:
    pin2.write_analog(26)
    sleep(1000)
    pin2.write_analog(128)
    sleep(1000)
