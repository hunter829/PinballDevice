from machine import Pin,Timer
import time
led=Pin(25,Pin.OUT)
button_A=Pin(14,Pin.IN,Pin.PULL_DOWN)
button_B=Pin(13,Pin.IN,Pin.PULL_DOWN)
button_C=Pin(15,Pin.IN,Pin.PULL_DOWN)
emv1=Pin(0,Pin.OUT)
emv2=Pin(1,Pin.OUT)
em1=Pin(2,Pin.OUT)
em2=Pin(3,Pin.OUT)
ip=Pin(4,Pin.IN,Pin.PULL_DOWN)
signal=Pin(11,Pin.IN,Pin.PULL_UP)

if __name__=='__main__':
    led.value(1)
    em1.value(1)
    main_cnt=0
    
    while True:
        main_cnt+=1
        time.sleep(0.01)
        if main_cnt%1000==0 and em1.value()==0:
            em1.value(1)
        #print("-")
        if signal.value()==0:
            print('recv signal')
            em1.value(1)
        if ip.value() and not em1.value():
            em1.value(1)
        if main_cnt%30==0:    #每0.3s检测一次
            if button_A.value()==1:
                print("A")
                em1.value(0)
                main_cnt=0
            if button_B.value()==1:
                print("B")
                em1.value(0)
                time.sleep(0.01)
                em1.value(1)
            
  