from machine import Pin
import time
CLK=Pin(0,Pin.IN,Pin.PULL_DOWN)
DT=Pin(1,Pin.IN,Pin.PULL_DOWN)
SW=Pin(2,Pin.IN,Pin.PULL_UP)
count=0
lastCLK=0
lastDT=0
lastSW=1
while True:
    CLK_STATE=CLK.value()
    DT_STATE=DT.value()
    SW_STATE=SW.value()
    if lastCLK!=CLK_STATE or lastDT!=DT_STATE or lastSW!=SW_STATE:
        count=count+1
        print('第',count,'次电平变化','CLK',CLK_STATE,' ','DT',DT_STATE,' ','SW',SW_STATE,'\r\n')
        lastCLK=CLK_STATE
        lastDT=DT_STATE
        lastSW=SW_STATE