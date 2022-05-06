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
signal=Pin(11,Pin.IN,Pin.PULL_UP)
ip=Pin(4,Pin.IN,Pin.PULL_DOWN)

def shutdown_1(ip):
    global irq1
    irq1+=1
    print('irq1*',irq1)
    em1.value(1)
def shutdown_2(signal):
    global irq2
    irq2+=1
    print('irq2*',irq2)
    em1.value(1)
        #signal.irq(twinkle, Pin.IRQ_FALLING)
if __name__=='__main__':
    led.value(1)
    em1.value(1)
    main_cnt=0
    old_key=0
    global req,irq
    irq1=0
    irq2=0
    ip.irq(shutdown_1, Pin.IRQ_RISING)
    signal.irq(shutdown_2, Pin.IRQ_FALLING)
    while True:
        main_cnt+=1
        time.sleep(0.001)
        if main_cnt%300==0:
            ip.irq(shutdown_1, Pin.IRQ_RISING)
            key=button_A.value()*10+button_B.value()
            if key!=old_key:
                print('old_key=',old_key)
            if key==0 and old_key==10:
               print("A")
               em1.value(0)
               main_cnt=0
            old_key=key
        