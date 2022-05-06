from machine import Pin,PWM
import time
CLK=Pin(0,Pin.IN,Pin.PULL_DOWN)
DT=Pin(1,Pin.IN,Pin.PULL_DOWN)
SW=Pin(2,Pin.IN,Pin.PULL_UP)
pwm=PWM(Pin(6))
led=Pin(25,Pin.OUT)
pwm.freq(500)
pwm.duty_u16(65536)
count=255
lastCLK=0
while True:
    led.value(1)
    CLK_STATE=CLK.value()
    DT_STATE=DT.value()
    SW_STATE=SW.value()
    if SW_STATE==0:
        if count<255:
            count=255
            pwm.duty_u16(count*count)
            time.sleep(0.5)
        else:
            count=122
            pwm.duty_u16(count*count)
            time.sleep(0.5)
    if lastCLK!=CLK_STATE:
        lastCLK=CLK_STATE
        if CLK_STATE!=DT_STATE:
            cha=-10
        else:
            cha=10
        if count>=0 and count<=255:
            count+=cha
            pwm.duty_u16(count*count)
            time.sleep(0.001)
        elif count<0:
            count=0
            pwm.duty_u16(count*count)
            time.sleep(0.001)
        elif count>255:
            count=255
            pwm.duty_u16(count*count)
            time.sleep(0.001)