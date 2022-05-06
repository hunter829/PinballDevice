from machine import Pin
import time
button_A=Pin(14,Pin.IN,Pin.PULL_DOWN)
button_B=Pin(13,Pin.IN,Pin.PULL_DOWN)
button_C=Pin(15,Pin.IN,Pin.PULL_DOWN)
emv1=Pin(0,Pin.OUT)
emv2=Pin(1,Pin.OUT)
em1=Pin(2,Pin.OUT)
em2=Pin(3,Pin.OUT)
if __name__=='__main__':
    while True:
        led.value(1)
        em1.value(0)
        em2.value(0)
        if button_A.value()==1:
            zuo.value(1)
            time.sleep(0.5)
            zuo.value(0)
        if button_B.value()==1:
            zuo.value(1)
            time.sleep(0.5)
            zuo.value(0)
        if button_C.value()==1:
            zuo.value(1)
            time.sleep(0.5)
            zuo.value(0)
        if button_D.value()==1:
            zuo.value(1)
            time.sleep(0.5)
            zuo.value(0)
        

