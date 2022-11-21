from machine import Pin, PWM
from time import sleep


in1 = Pin(15, Pin.OUT)
in1.value(0)
in2 = Pin(14, Pin.OUT)
in2.value(0)
sleep(0.5)

in1_pwm = PWM(Pin(15))
in1_pwm.freq(1000)

led25 = Pin(25, Pin.OUT)
delay_sec = 2
# I need to give 5V to L298N with Brushed DC motor type B, 
# then the Brushed DC motor can be runned by this code.

A = [0,5000,10000,15000,20000,25000,30000,35000,40000, 45000, 50000,55000, 60000, 65000,
     60000, 55000,50000,45000,40000,35000,30000,25000,20000,15000,10000,10000,5000]
while True:
    """
    for duty in range(0,65535,10000):
        in1_pwm.duty_u16(duty)
        led25.toggle()  
        sleep(delay_sec)
    """        
    for duty in A:
        in1_pwm.duty_u16(duty)
        led25.toggle()  
        sleep(delay_sec)
        


