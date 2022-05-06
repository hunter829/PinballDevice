from machine import UART, Pin
import time

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
button_D=Pin(4,Pin.IN,Pin.PULL_DOWN)
button_A=Pin(2,Pin.IN,Pin.PULL_DOWN)
button_B=Pin(3,Pin.IN,Pin.PULL_DOWN)
button_C=Pin(5,Pin.IN,Pin.PULL_DOWN)
zuo=Pin(6,Pin.OUT)
you=Pin(7,Pin.OUT)
led=Pin(25,Pin.OUT)
if __name__=='__main__':
    while True:
        led.value(1)
        zuo.value(1)
        if button_A.value()==1:
            zuo.value(0)
            time.sleep(0.4)
            zuo.value(1)
        if button_B.value()==1:
            zuo.value(0)
            time.sleep(0.4)
            zuo.value(1)
        if button_C.value()==1:
            zuo.value(0)
            time.sleep(0.4)
            zuo.value(1)
        if button_D.value()==1:
            zuo.value(0)
            time.sleep(0.4)
            zuo.value(1)
            
        
