from machine import Pin,Timer
import time
led=Pin(25,Pin.OUT)

st1=Pin(0,Pin.OUT)
st2=Pin(1,Pin.OUT)
ns=Pin(4,Pin.OUT)
a=Pin(2,Pin.IN,Pin.PULL_DOWN)
b=Pin(3,Pin.IN,Pin.PULL_DOWN)
j=0
counter_val0=0
counter_val1=0
def timerisr():
    j=1                     
    v=60*20*counter_val0/150.0  
    counter_val0=0
    counter_val1=0              
    return v
def counter0(a):
    global counter_val0+=1
def counter1(b):
    global counter_val1+=1
while True:
    led.value(1)
    st1.value(0)
    st2.value(1)
    ns.value(1)
    tim = Timer()
    tim.init(period=50, mode=Timer.PERIODIC, callback=timerisr)
    a.irq(counter0, Pin.IRQ_FALLING)
    b.irq(counter1, Pin.IRQ_RISING)
    if j==1:
        j=0