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
    details = radio.receive_full()#キューにある3つの値を返します（メッセージのバイト列、信号強度、タイムスタンプ）
    if details != None:#もしキューに何か値があれば
        rssi = details[1]#バイト列をrssiにいれます
        if rssi > -60:#-60よりも大きな数字（1m圏内）だったら殆ど点灯
            display.show(mat2)
        elif rssi  > -70:#-70よりも大きな数字（3M圏内）
            display.show(mat1)
        else:
            display.show(mat0)



