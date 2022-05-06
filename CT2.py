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


def twinkle(signal):
    if signal.value()==0:
        em1.value(1)
        #signal.irq(twinkle, Pin.IRQ_FALLING)
if __name__=='__main__':
    led.value(1)
    em1.value(1)
    main_cnt=0
    old_key=0
    start_mode=0
    t=0
    while True:
        main_cnt+=1
        time.sleep(0.001)
        if main_cnt%300==0:
            key=button_A.value()*10+button_B.value()
            if key!=old_key:
                print('old_key=',old_key)
            if key==0 and old_key==10:
               print("A")
               em1.value(0)
               main_cnt=0
               start_mode=1
               time.sleep(0.02)
            if key==0 and old_key==1:
                em1.value(0)
                time.sleep(0.1)
                em1.value(1)
                start_mode=2
            old_key=key
            
        #print("-")
        if ip.value()==1 and start_mode==1 and em1.value()==0 :
            print("rcv")
            em1.value(1)
            
            while True :
                em1.value(0)
                time.sleep(0.01)
                em1.value(1)
                time.sleep(0.1)
                if signal.value()==0 :
                    t+=1
                    print('t=',t)
                    em1.value(1)
                    break
                   
        if signal.value()==0 and start_mode==2:
            em1.value(1)
                        
        
         
        #if button_C.value()==1:    
           