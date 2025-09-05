from microbit import *

STATUS_OFF = 0
STATUS_ON = 1

LIT_NONE = 0
LIT_BLUE = 1
LIT_YELLOW = 2
LIT_RED = 3

TIMER_BLUE = 5
TIMER_YELLOW = 2
TIMER_RED = 4

status = LIT_NONE
clock = 0

display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        status = LIT_BLUE
        clock = TIMER_BLUE

    if button_b.is_pressed():
        status = LIT_NONE
        clock = 0

    if status == LIT_NONE:
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(0)
    elif status == LIT_BLUE:
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(1)
    elif status == LIT_YELLOW:
        pin0.write_digital(0)
        pin1.write_digital(1)
        pin2.write_digital(0)
    elif status == LIT_RED:
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(0)

    sleep(1000)

    if clock > 0:
        clock = clock - 1

    if clock == 0:
        if status > LIT_NONE:
            if status == LIT_BLUE:
                status = LIT_YELLOW
                clock = TIMER_YELLOW
            elif status == LIT_YELLOW:
                status = LIT_RED
                clock = TIMER_RED
            elif status == LIT_RED:
                status = LIT_BLUE
                clock = TIMER_BLUE
