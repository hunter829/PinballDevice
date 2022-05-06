import max44009
from machine import I2C
import time
i2c=I2C(0)
sensor = max44009.MAX44009(i2c)
sensor.continuous = 1
sensor.manual = 1
sensor.current_division_ratio = 0
sensor.integration_time = 3
sensor._read_config()
while True:
    print('highlux=',sensor.lux)
    print('lowlux=',sensor.lux_fast)
    time.sleep(1)