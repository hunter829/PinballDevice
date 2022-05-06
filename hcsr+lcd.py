import ssd1306py as lcd
from hcsr04 import HCSR04
from machine import Pin
import time
led=Pin(25,Pin.OUT)
led.value(1)
sensor = HCSR04(trigger_pin=0, echo_pin=1, echo_timeout_us=10000)
while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    time.sleep(1)
    lcd.init_i2c(5,4, 128, 64, 0)
    lcd.text('Distance:', 0, 0, 8)
    lcd.text(str(distance)+'cm', 0, 10, 8)
    lcd.show()