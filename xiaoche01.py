from machine import Pin,PWM
import time
led=Pin(25,Pin.OUT)

a=Pin(0,Pin.OUT)
b=Pin(1,Pin.OUT)
'''
pwm1=PWM(Pin(0))
pwm2=PWM(Pin(1))
'''
CLK=Pin(2,Pin.IN,Pin.PULL_DOWN)
DT=Pin(3,Pin.IN,Pin.PULL_DOWN)
pwm1.freq(500)
pwm1.duty_u16(65536)
pwm2.freq(500)
pwm2.duty_u16(65536)
lastCLK=0
count=0
while True:
    led.value(1)
    
    a.value(0)
    b.value(1)
    
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