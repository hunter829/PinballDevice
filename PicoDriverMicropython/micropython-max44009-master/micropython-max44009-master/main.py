import max44009
from machine import I2C, Pin
i2c=I2C(0)
sensor = max44009.MAX44009(i2c)
sensor.continuous = 1

sensor.manual = 0

sensor.current_division_ratio = 0

sensor.integration_time = 3

sensor._read_config()