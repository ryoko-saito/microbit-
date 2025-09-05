from microbit import *
import radio

display.show(Image.ARROW_N)

radio.config(group=1, power=1)
radio.on()
# ここにコードを書いてね :-)
i = 0
while True:
    radio.send(str(i))
    display.show(Image.HEART)
