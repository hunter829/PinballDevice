from machine import Pin
import time
led=Pin(25,Pin.OUT)
trig=Pin(0,Pin.OUT)
echo=Pin(1,Pin.IN,Pin.PULL_DOWN)
start=0
while True:
    led.value(1)
    trig.value(0)
    time.sleep(0.002)
    trig.value(1)
    if echo.value()==1:
        start=time.ticks_ms()
    time.sleep(0.01)
    trig.value(0)
    if echo.value()==0:
        end=time.ticks_ms()
    juli=time.ticks_diff(end,start)
    
    print('距离：',juli*17/10000)
    time.sleep(1)