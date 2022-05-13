import time
from machine import Pin
led = Pin(25, Pin.OUT)
ledY = Pin(2, Pin.OUT)
ledR = Pin(3, Pin.OUT)
ledG = Pin(4, Pin.OUT)
while(True):
    led.toggle()
    time.sleep(0.1)
    ledY.toggle()
    led.toggle()
    time.sleep(0.1)
    ledR.toggle()    
    led.toggle()
    time.sleep(0.1)
    ledG.toggle()        
    led.toggle()
    time.sleep(0.1)