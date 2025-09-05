from microbit import *
import radio#無線通信のモジュールをインポート

radio.config(group=1, power=1)#1グループ、信号強度1で無線を構成します
#radio.on()#config()を呼び出すと自動でオンになるので、radio.on()は不要

i = 0
while True:#ずっと
    radio.send(str(i))#iを送信する
    display.scroll(str(i))
    i=i+1
    sleep(100) 
