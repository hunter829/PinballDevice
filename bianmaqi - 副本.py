from machine import Pin,PWM
import time
CLK=Pin(0,Pin.IN,Pin.PULL_DOWN)
DT=Pin(1,Pin.IN,Pin.PULL_DOWN)
SW=Pin(2,Pin.IN,Pin.PULL_UP)
pwm = PWM(Pin(6))
count=0
lastCLK=0
while True:
    
    pwm.freq(1000)
    duty = 1
    '''
    direction = 1
    for _ in range(8 * 256):
        duty += direction
        if duty > 255:
            duty = 255
            direction = -1
        elif duty < 0:
            duty = 0
            direction = 1
        pwm.duty_u16(duty * duty)
        time.sleep(0.001)
        '''
    CLK_STATE=CLK.value()
    DT_STATE=DT.value()
    SW_STATE=SW.value()
    if SW_STATE==0:
        count=0
        pwm.duty(count)
        time.sleep(0.4)
    
    if lastCLK!=CLK_STATE:
        lastCLK=CLK_STATE
        if CLK_STATE!=DT_STATE:
            cha=1
        else:
            cha=-1
        count+=cha
        pwm.duty(count)