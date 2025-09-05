from microbit import *
import utime

isWait = False
isOpen = False

def measureDistance():
    v = 0.6 * temperature() + 331.5
    pin0.write_digital(1)
    pin0.write_digital(0)

    while pin1.read_digital() == 0:
        utime.sleep_us(1)

    t1 = utime.ticks_us()

    while pin1.read_digital() == 1:
        utime.sleep_us(1)

    t2 = utime.ticks_us()
    t = utime.ticks_diff(t2, t1)
    return int(t * v / 20000)

def openDoor():
    isWait = True
    pin2.write_analog(76)
    sleep(1000)
    isWait = False
    isOpen = True

def closeDoor():
    isWait = True
    pin2.write_analog(26)
    sleep(1000)
    isWait = False
    isOpen = False


pin2.write_digital(0)

while True:
    if isWait == False:
        if isOpen == False and measureDistance() <= 20:
            openDoor()
        elif isOpen == True:
            closeDoor()
        sleep(1000)
# ここにコードを書いてね :-)
