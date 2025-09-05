from microbit import *
import utime

isWait = False
isOpen = False
a = []
for i in range(73, 40, -1):
    a.append(i)

while True:
    if button_a.is_pressed():
        for i in a:
            pin0.write_analog(i)
            sleep(20)

