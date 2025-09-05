sfrom microbit import *
import utime

def openDoor():
    a = []
    for i in range(73, 40, -1):
        a.append(i)

    for i in a:
        pin0.write_analog(i)
        sleep(20)
    sleep(1000)
    return True

def closeDoor():
    pin0.write_analog(73)
    sleep(1000)
    return False

pin0.write_analog(73)

while True:
        if button_a.is_pressed():
            openDoor()
            pin1.write_digital(1)
            pin2.write_digital(1)
        if button_b.is_pressed():
            closeDoor()
        sleep(1000)

