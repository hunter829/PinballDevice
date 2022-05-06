from machine import Pin,PWM
import time
led=Pin(25,Pin.OUT)

a=Pin(0,Pin.OUT)
b=Pin(1,Pin.OUT)
ns=Pin(4,Pin.OUT)
CLK=Pin(2,Pin.IN,Pin.PULL_DOWN)
DT=Pin(3,Pin.IN,Pin.PULL_DOWN)

lastCLK=0
count=0
while True:
    led.value(1)
    
    a.value(0)
    b.value(1)
    ns.value(1)
    CLK_STATE=CLK.value()
    DT_STATE=DT.value()
    if lastCLK!=CLK_STATE:
        lastCLK=CLK_STATE
        if CLK_STATE!=DT_STATE:
            cha=-1
        else:
            cha=1
        if count>=0 and count<=255:
            count+=cha
            print('count:',count,'\r\n')
            
            time.sleep(0.001)
        elif count<0:
            count=0
            print('count:',count,'\r\n')
            
            time.sleep(0.001)
        elif count>255:
            count=255
            print('count:',count,'\r\n')
            
            time.sleep(0.001)