from machine import Pin,Timer,PWM
import time
led=Pin(25,Pin.OUT)
button_A=Pin(14,Pin.IN,Pin.PULL_DOWN)
button_B=Pin(12,Pin.IN,Pin.PULL_DOWN)
button_C=Pin(15,Pin.IN,Pin.PULL_DOWN)
button_D=Pin(13,Pin.IN,Pin.PULL_DOWN)
moto0=Pin(0,Pin.OUT)
moto1=Pin(1,Pin.OUT)
moto2=Pin(2,Pin.OUT)
moto3=Pin(3,Pin.OUT)
signal0=Pin(6,Pin.IN,Pin.PULL_UP)
signal1=Pin(7,Pin.IN,Pin.PULL_UP)
switch0=Pin(16,Pin.IN,Pin.PULL_DOWN)
switch1=Pin(17,Pin.IN,Pin.PULL_DOWN)
moto0_pwm=PWM(moto0)
moto1_pwm=PWM(moto1)
moto0_pwm.freq(500)
moto0_pwm.freq(500)
moto0_pwm.duty_u16(65536)
moto0_pwm.duty_u16(65536)
if __name__=='__main__':
    led.value(1)
    moto0.value(1)
    moto1.value(1)
    moto2.value(1)
    moto3.value(1)
    if switch0.value():
        print(1)
        time.sleep(0.3)