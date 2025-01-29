from machine import Pin
from time import sleep
led = Pin(2, Pin.OUT)
for i in range(10):
    led.high()
    time.sleep(10)
    led.low()
