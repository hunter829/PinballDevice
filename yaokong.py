from machine import UART, Pin
import time

uart1 = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart0 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
button_D=Pin(4,Pin.IN,Pin.PULL_DOWN)
button_A=Pin(2,Pin.IN,Pin.PULL_DOWN)
button_B=Pin(3,Pin.IN,Pin.PULL_DOWN)
button_C=Pin(5,Pin.IN,Pin.PULL_DOWN)

while True:
    if button_A.value()==1:
        txData = b'you press button A\n\r'
        uart1.write(txData)
        time.sleep(0.4)
        rxData = bytes() #bytes()创建一个空数组
        #.any有一个不为0的元素就返回true
        while uart0.any() > 0:
                rxData += uart0.read(1)
        print(rxData.decode('utf-8'))

    
    if button_B.value()==1:
        txData = b'you press button B\n\r'
        uart1.write(txData)
        time.sleep(0.4)
        rxData = bytes() #bytes()创建一个空数组
        #.any有一个不为0的元素就返回true
        while uart0.any() > 0:
            rxData += uart0.read(1)
        print(rxData.decode('utf-8'))
    if button_C.value()==1:
        txData = b'you press button C\n\r'
        uart1.write(txData)
        time.sleep(0.4)
        rxData = bytes() #bytes()创建一个空数组
        #.any有一个不为0的元素就返回true
        while uart0.any() > 0:
            rxData += uart0.read(1)
        print(rxData.decode('utf-8'))
    if button_D.value()==1:
        txData = b'you press button D\n\r'
        uart1.write(txData)
        time.sleep(0.4)
        rxData = bytes() #bytes()创建一个空数组
        #.any有一个不为0的元素就返回true
        while uart0.any() > 0:
            rxData += uart0.read(1)
        print(rxData.decode('utf-8'))
            