from machine import Pin
import utime
in1 = Pin(15, Pin.OUT)
in2 = Pin(14, Pin.OUT)
led25 = Pin(25, Pin.OUT)
delay_sec = 2
# I need to give 5V to L298N with Brushed DC motor type B, 
# then the Brushed DC motor can be runned by this code.
while True:
    led25.toggle()
    in1.value(0)
    in2.value(0)
    utime.sleep(delay_sec)
    led25.toggle()    
    in1.value(0)
    in2.value(0)
    utime.sleep(delay_sec)
    led25.toggle()    
    in1.value(1)
    in2.value(0)
    utime.sleep(delay_sec)
    led25.toggle()    
    in1.value(1)
    in2.value(1)
    utime.sleep(delay_sec)

    

