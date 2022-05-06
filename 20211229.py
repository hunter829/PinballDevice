from machine import Pin,Timer
import time
led=Pin(25,Pin.OUT)
button_A=Pin(14,Pin.IN,Pin.PULL_DOWN)
button_B=Pin(12,Pin.IN,Pin.PULL_DOWN)
button_C=Pin(15,Pin.IN,Pin.PULL_DOWN)
button_D=Pin(13,Pin.IN,Pin.PULL_DOWN)
moto1=Pin(0,Pin.OUT)
moto2=Pin(1,Pin.OUT)
# moto1=Pin(2,Pin.OUT)
# em2=Pin(3,Pin.OUT)
signal1=Pin(6,Pin.IN,Pin.PULL_UP)
signal2=Pin(7,Pin.IN,Pin.PULL_UP)
ip1=Pin(16,Pin.IN,Pin.PULL_DOWN)
ip2=Pin(17,Pin.IN,Pin.PULL_DOWN)
def shutdown_1(ip1):
    print('recv req1')
    global req1
    req1+=1
    moto1.value(1)
    
def shutdown_2(signal1):
    print('中断触发')
    global req2,num
    req2+=1
    print('中断触发',req2)
    moto1.value(1)
def shutdown_3(ip2):
    print('recv req1')
    global req3
    req1+=1
    moto2.value(1)
    
def shutdown_4(signal2):
    print('中断触发')
    global req4,num2
    req2+=1
    print('中断触发',req2)
    moto2.value(1)

if __name__=='__main__':
    led.value(1)
    moto1.value(1)
    moto1.value(1)
    main_cnt=0
    old_key1=0
    old_key2=0
    start_mode=0
    t1=0
    t2=0
    global req1,req2,num1,req3,req4,num2
    req1=0
    req2=0
    num=0
    req3=0
    req4=0
    num2=0
    while True:
        #ip.irq(shutdown_1, Pin.IRQ_RISING)
        signal1.irq(shutdown_2, Pin.IRQ_FALLING)
        signal2.irq(shutdown_4, Pin.IRQ_FALLING)
        main_cnt+=1
        time.sleep(0.001)
        if main_cnt%300==0:
            key1=button_A.value()*10+button_B.value()
            if key1!=old_key1:
                print('old_key1=',old_key1)
            if key1==0 and old_key1==10:
               print("A")
               moto1.value(0)
               main_cnt=0
               start_mode=1
               #time.sleep(0.02)
            old_key1=key1
            key2=button_C.value()*10+button_D.value()
            if key2!=old_key2:
                print('old_key2=',old_key2)
            if key2==0 and old_key2==10:
               print("C")
               moto2.value(0)
               main_cnt=0
               start_mode=3
               #time.sleep(0.02)
            old_key2=key2
        if button_B.value():
            moto1.value(0)
            time.sleep(0.0005)
            moto1.value(1)
            start_mode=2 
            #print('old_key=',old_key)
            #print("-")
            
        if button_D.value():
            moto2.value(0)
            time.sleep(0.0005)
            moto2.value(1)
            start_mode=4
            #print('old_key=',old_key)
            #print("-")
        if ip1.value()==1:
            req2=0
            print("recv ip1")
            
            if not moto1.value():
                moto1.value(1)
                '''
        if ip.value()==1 and not moto1.value():
            print("rcv")
            moto1.value(1)
                '''
            while True:
                t+=1
                req2=0
                moto1.value(0)
                time.sleep(0.005)
                moto1.value(1)
                time.sleep(0.4)
                print('t=',t)
                
                if req2:
                    print('中断触发了',req2,'次')
                    req2=0
                    t=0
                    break
                '''
                if signal.value()==0 :
                    t=0
                    print('stop')
                    moto1.value(1)
                    break
                '''
        if signal1.value()==0 and start_mode==2:
            moto1.value(1)
        #if button_C.value()==1:
        if ip2.value()==1:
            req4=0
            print("recv ip")
            if not moto2.value():
                moto2.value(1)
                '''
        if ip.value()==1 and not moto1.value():
            print("rcv")
            moto1.value(1)
                '''
            while True:
                t+=1
                req4=0
                moto2.value(0)
                time.sleep(0.005)
                moto2.value(1)
                time.sleep(0.4)
                print('t=',t)
                
                if req4:
                    print('中断触发了',req4,'次')
                    req4=0
                    t=0
                    break
                '''
                if signal.value()==0 :
                    t=0
                    print('stop')
                    moto1.value(1)
                    break
                '''
        if signal2.value()==0 and start_mode==4:
            moto1.value(1)