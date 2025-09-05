from microbit import*

while True:
    It = display.read_light_level()
    display.show(It)
    if It < 100:
        display.show(Image.SAD)
    if It >= 100:
        display.show(Image.HAPPY)
    sleep(5000)

