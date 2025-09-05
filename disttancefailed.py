from microbit import *
import utime

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
    a = []
    for i in range(73, 40, -1):
        a.append(i)

    for i in a:
        pin2.write_analog(i)
        sleep(20)
    sleep(1000)

def closeDoor():
    pin2.write_analog(73)
    sleep(1000)

# ドアを開けておく秒数
OPEN_PERIOD = 3
timer = 0

closeDoor()
isOpen = False

while True:
    if isOpen == False:
        if measureDistance() <= 20:
            openDoor()
            isOpen = True
            timer = OPEN_PERIOD
    elif isOpen == True:
        if timer > 0 and measureDistance() <= 20:
            timer = OPEN_PERIOD
        elif timer == 0:
            closeDoor()
            isOpen = False

    sleep(1000)
    if timer > 0:
        timer -= 1


# ここにコードを書いてね :-)
