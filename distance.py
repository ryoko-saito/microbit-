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
    pin2.write_analog(76)
    sleep(3000)

def closeDoor():
    pin2.write_analog(26)


if __name__ == "__main__":
    pin0.write_digital(0)

    while True:
        if measureDistance() <= 20:
            openDoor()
        else:
            closeDoor()

        utime.sleep(1)
