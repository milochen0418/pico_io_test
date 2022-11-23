from machine import Pin, PWM
from time import sleep

# Hardward Connection Description 
# PICO.GP15 <-> L298N.IN1
# PICO.GP14 <-> L298N.IN2
# L298N.12V <-> Power supply or PICO.VBUS
# L298N.ENA jumper connected
# L298N.ENB jumper connected
# L298N.Regulator Enable Jumper connected. Use >6V power on 12V 
# When L298N.Regulator Enable Jumper is connected, you can give 5V to outside  
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

A = [0, 10000,15000,20000,25000,30000,35000,40000, 45000, 50000,55000, 60000, 65000,
     60000, 55000,50000,45000,40000,35000,30000,25000,20000,15000,10000]

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
        


