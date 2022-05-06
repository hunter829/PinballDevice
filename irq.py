from machine import Pin
import utime

#配置按键
key = Pin(0, Pin.IN, Pin.PULL_UP)

def external_interrupt(key):
    # 消除抖动
    utime.sleep_ms(100)
    # 再次判断按键是否被按下
    if key.value() == 0:
        print('The button is pressed')

if __name__ == '__main__':
    # KEY.irq(handler,trigger)
    # handler:中断执行的回调函数
    # trigger:触发中断的方式，分别为Pin.IRQ_FALLING(下降沿触发)、
    # Pin.IRQ_RISING(上升沿触发)、Pin.IRQ_LOW_LEVEL(低电平触发)和
    # Pin.IRQ_HIGH_LEVEL(高电平触发)四种
    # 定义中断，下降沿触发
    key.irq(external_interrupt, Pin.IRQ_FALLING)