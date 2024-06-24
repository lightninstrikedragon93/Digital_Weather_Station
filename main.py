from machine import Pin, I2C
import time
import ssd1306
import bme280

#oled
i2c1_display = I2C(1, scl=Pin(15), sda=Pin(14))
print('Scanning I2C0 bus...')
devices1 = i2c1_display.scan()

if devices1:
    for device in devices1:
        print(f'Device found at address: {hex(device)} on I2C1')
else:
    print('No I2C devices found on I2C1')
    
#senzor
i2c0_senzor = I2C(0, scl=Pin(17), sda=Pin(16))
print('Scanning I2C0 bus...')
devices0 = i2c0_senzor.scan()
if devices0:
    for device in devices0:
        print(f'Device found at address: {hex(device)} on I2C0')
else:
    print('No I2C devices found on I2C0')

WIDTH = 128    # OLED display width
HEIGHT = 32    # OLED display height

oled = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c1_display)
bme280_address = 0x76
bme = bme280.BME280(i2c=i2c0_senzor, address=bme280_address)
while True:
    # Read temperature, pressure, and humidity
    temperature = bme.temperature
    pressure = bme.pressure
    humidity = bme.humidity
    
    # Print the sensor readings
    print("\nMeasurement Values are:")
    print("Pressure =", pressure)
    print("Temperature =", temperature)
    print("Humidity =", humidity)
    

    # Clear OLED display
    oled.fill(0)
    oled.show()
    
    # Display BME data on OLED
    temp="Temp:"+str(temperature) 
    oled.text(temp , 0, 1)
    presr="Pres:"+str(pressure)
    oled.text(presr , 1, 12)
    hmd="Humidity:"+str(humidity)
    oled.text(hmd , 1, 23)
    oled.show()
    time.sleep(4)
    
    # Clear OLED display
    oled.fill(0)
    oled.show()