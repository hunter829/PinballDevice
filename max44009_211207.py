from machine import Pin,Timer,I2C
import time
MAX44009_ADDR_WT =const(0x94)
MAX44009_ADDR_RD =const(0x95)
INT_STATUS =const(0x00)
INT_ENABLE =const(0x01)
CONFIG_REG =const(0x02)
HIGH_BYTE =const(0x03)
LOW_BYTE =const(0x04)
THRESH_HIGH =const(0x05)
THRESH_LOW =const(0x06)
THRESH_TIMER =const(0x07)
MAX44009_I2C_ADD=const(0x4a)
i2c=I2C(0)
scan=i2c.scan()

buf1=bytearray(1)
buf2=bytearray(1)
def read_HIGH_BYTE():
    cmd = bytearray(3)
    cmd[0] = MAX44009_ADDR_WT
    cmd[1] = HIGH_BYTE
    cmd[2] = MAX44009_ADDR_RD
    
    i2c.writeto(MAX44009_I2C_ADD, cmd)
    i2c.readfrom_into(MAX44009_I2C_ADD, buf)
    

def read_ALL_BYTE():
    cmd = bytearray(3)
    cmd[0] = MAX44009_ADDR_WT
    cmd[1] = HIGH_BYTE
    cmd[2] = MAX44009_ADDR_RD
    
    i2c.writeto(MAX44009_I2C_ADD, cmd)
    i2c.readfrom_into(MAX44009_I2C_ADD, buf1)
    cmd[0] = MAX44009_ADDR_WT
    cmd[1] = LOW_BYTE
    cmd[2] = MAX44009_ADDR_RD
    i2c.writeto(MAX44009_I2C_ADD, cmd)
    i2c.readfrom_into(MAX44009_I2C_ADD, buf2)
while True:
    read_ALL_BYTE()
    print(buf1)
    print(buf2)
    time.sleep(1)

