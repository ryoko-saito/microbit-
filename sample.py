from microbit import*
import radio

radio.config(group=1)
radio.on()

mat0 = Image("00000:"
            "00000:"
            "00000:"
            "00000:"
            "00000:")

mat1 = Image("00000:"
            "00000:"
            "00000:"
            "99999:"
            "99999:")

mat2 = Image("00900:"
            "09990:"
            "09990:"
            "99999:"
            "99999:")

while True:
    details = radio.receive_full()
    if details != None:
        rssi = details[1]
        if rssi > -60:
            display.show(mat2)
        elif rssi  > -70:
            display.show(mat1)
        else:
            display.show(mat0)



