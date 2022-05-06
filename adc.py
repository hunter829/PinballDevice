import machine
import utime

sensor_temp = machine.ADC(4)
x_temp=machine.ADC(1)
y_temp=machine.ADC(0)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    x_distance=x_temp.read_u16() * conversion_factor*100
    y_distance=y_temp.read_u16() * conversion_factor*100
    print('temperature=',temperature,'\r\n','X distance=',x_distance,'\r\n','Y distance=',y_distance,'\r\n')
    utime.sleep(0.5)