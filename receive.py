from microbit import*
import radio

radio.config(group=1)#無線のグループを1に設定する
radio.on()#無線通信をonにする
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
    details = radio.receive_full()#キューにある次のメッセージを表す３つの値（バイト列、RSSI、タイムスタンプ）を返します
    if details != None:#何か値が入っていれば、
        rssi = details[1]
        if rssi > -50:
            display.show(mat2)
        elif rssi  > -70:
            display.show(mat1)
        else:
            display.show(mat0)



