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

moto2_pwm=PWM(moto2)
moto1_pwm=PWM(moto1)
moto2_pwm.freq(500)
moto1_pwm.freq(500)
moto2_pwm.duty_u16(65536)
moto1_pwm.duty_u16(65536)
'''
def switch0_close(switch1):
    global req1
    if not req1:
        print('recv req1')
        req1+=1
        moto1.value(1)
        time.sleep(0.1)
def switch1_close(swicth2):
    global req3
    if not req3:
        print('recv req3')
        req3+=1
        moto2.value(1)
        time.sleep(0.1)
'''
def signal0_close(signal0):
    moto0.value(1)
    print('信号中断0触发')
    global signal0_triggle
    signal0_triggle+=1

def signal1_close(signal1):
    moto0.value(1)
    print('信号中断1触发')
    global signal1_triggle
    signal1_triggle+=1
    
    

if __name__=='__main__':
    led.value(1)
    moto0.value(1)
    moto1.value(1)
    moto2.value(1)
    moto3.value(1)
    main_cnt=0
    old_key1=0
    old_key2=0
    start_mode=0
    global signal0_triggle，signal1_triggle
    signal0_triggle=0
    signal1_triggle=0
    
    while True:
        #ip1.irq(shutdown_1, Pin.IRQ_RISING)
        #ip2.irq(shutdown_3, Pin.IRQ_RISING)
        signal0.irq(signal0_close, Pin.IRQ_FALLING)
        signal1.irq(signal1_close, Pin.IRQ_FALLING)
        
        main_cnt+=1
        time.sleep(0.001)
        if main_cnt%300==0:
            key1=button_A.value()*10+button_B.value()
            if key1!=old_key1:
                print('old_key1=',old_key1,',key2=',key2)
            if key1==0 and old_key1==10:
               print("A1")
               moto0.value(0)
               print('A2')
               main_cnt=0
               start_mode=1
               #time.sleep(0.02)
            if key1==0 and old_key1==1:
                print("B")
                pwm_moto0.duty_u16(25*25)
                main_cnt=0
                start_mode=1
            old_key1=key1
            key2=button_C.value()*10+button_D.value()
            if key2!=old_key2:
                print('old_key2=',old_key2,',key2=',key2)
            if key2==0 and old_key2==10:
               print("C")
               moto1.value(0)
               main_cnt=0
               start_mode=3
               #time.sleep(0.02)
            if key2==0 and old_key2==1:
                print("D")
                pwm_moto1.duty_u16(25*25)
                main_cnt=0
                start_mode=1
            old_key2=key2
       
        if switch0.value():
            signal0_triggle=0
            print("recv switch0")
            time.sleep(0.1)
            if not moto0.value():
                moto0.value(1)
                print('stop')
                time.sleep(0.1)
                #碰到开关 moto0输出电平由0为1 电机停止
            while True:
                print('start')
                time.sleep(0.1)
                signal0_triggle=0
                moto2.value(0)
                time.sleep(0.05)
                moto2.value(1)
                time.sleep(1)
                if signal0_triggle:
                    print('中断触发了',signal0_triggle,'次')
                    signal0_triggle=0
                    break
             
        if switch1.value():
            signal1_triggle=0
            print("recv switch1")
            if not moto1.value():
                moto1.value(1)
                #碰到开关 moto1输出电平由0为1 电机停止
            while True:
                signal1_triggle=0
                pwm_moto1.duty_u16(25*25)
                if signal1_triggle:
                    print('中断触发了',signal1_triggle,'次')
                    signal0_triggle=1
                    break



