from microbit import *
import radio//無線通信のモジュールをインポート

display.show(Image.ARROW_N)

radio.config(group=1, power=1)//1グループ、信号強度1で無線を構成します
radio.on()//無線通信をonにする

i = 0
while True://ずっと
    radio.send(str(i))//iを送信する
    display.show(Image.HEART)//ハートを表示する
