from machine import Pin
import time
CLK=Pin(0,Pin.IN,Pin.PULL_DOWN)
DT=Pin(1,Pin.IN,Pin.PULL_DOWN)
SW=Pin(2,Pin.IN,Pin.PULL_UP)
count=1
lastCLK=0
while True:
    CLK_STATE=CLK.value()
    DT_STATE=DT.value()
    SW_STATE=SW.value()
    if SW_STATE==0:
        count=0
        print('count:',count,'\r\n')
        time.sleep(0.4)
    
    if lastCLK!=CLK_STATE:
        lastCLK=CLK_STATE
        if CLK_STATE!=DT_STATE:
            cha=1
        else:
            cha=-1
        if count>0 and count<255:
            count+=cha
            print('count:',count,'\r\n')
        elif count<=0:
            count=1
            print('count:',count,'\r\n')
        elif count>=255:
            count=254
            print('count:',count,'\r\n')