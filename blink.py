from machine import Pin
from time import sleep
led = Pin(2, Pin.OUT)
for i in range(10):
    led.high()
    time.sleep(5)
    led.low()
