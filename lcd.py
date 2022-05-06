import ssd1306py as lcd
from machine import Pin
import time
led=Pin(25,Pin.OUT)
led.value(1)
time.sleep(1)
led.toggle()
lcd.init_i2c(7,6, 128, 64, 0)
lcd.text('font8x8', 0, 0, 8)
lcd.text('font16x16', 0, 20, 16)
lcd.text('font24x24', 0, 40, 24)
lcd.show()