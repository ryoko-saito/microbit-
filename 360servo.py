from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.Heart)
        pin2.write_analog(112)
    if button_b.is_pressed():
        pin2.write_analog(26)
    if button_a.is_pressed() and button_b.is_pressed():
        pin2.write_analog(0)
