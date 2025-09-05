# ここにコードを書いてね :-)
import random
import time

l = [0, 0, 0, 0, 0]
while True:
    for i in range(4):
        l[i] = l[i+1]

    r = random.randint(1, 100) #display.read_light_level()
    l[4] = r

    time.sleep(1)
    print("avarage:")
    avarage = sum(l)/len(l)
    print(avarage)
