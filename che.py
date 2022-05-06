from machine import Pin, Timer
a=Pin(0,Pin.IN,Pin.PULL_DOWN)
b=Pin(1,Pin.IN,Pin.PULL_DOWN)
j=0
counter_val0=0
counter_val1=0
def timerisr():
    j=1;                           
    v=60*20*counter_val0/150.0;    
    counter_val0=0;
    counter_val1=0;               
    print v
def counter0(a):
    counter_val0+=1
def counter1(b):
    counter_val1+=1
while True:
    tim = Timer()
    tim.init(period=50, mode=Timer.PERIODIC, callback=timerisr)
    a.irq(counter0, Pin.IRQ_FALLING)
    b.irq(counter1, Pin.IRQ_RISING)
    if j==1:
        j=0