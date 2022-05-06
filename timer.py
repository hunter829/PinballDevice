from machine import Pin, Timer

# 创建LED对象
led=Pin(25, Pin.OUT)

# 闪烁回调函数
def twinkle(tim):
    # toggle方法:LED状态翻转
    led.toggle()

if __name__ == '__main__':
    # 构建定时器
    tim = Timer()
    # tim.init(period, mode, callback)
    # period:周期时间(单位为ms)
    # mode:工作模式，有Timer.ONE_SHOT(执行一次)和Timer.PERIODIC(周期性执行)两种
    # callback:定时器中断的回调函数
    tim.init(period=2000, mode=Timer.PERIODIC, callback=twinkle)