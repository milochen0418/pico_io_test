from machine import Pin, PWM
from time import sleep

# Hardward Connection Description 
# PICO.GP15 <-> L298N.IN1
# PICO.GP14 <-> L298N.IN2
# PICO.GP13 <-> L298N.ENA
# L298N.ENA NO jumper connected
# L298N.ENB jumper connected
# L298N.12V <-> Power supply (8V) or PICO.VBUS
# L298N.Regulator Enable Jumper connected. Use >6V power on 12V 
# When L298N.Regulator Enable Jumper is connected, you can give 5V to outside  

# Videos: 
# Running Result is here https://www.youtube.com/watch?v=kq-ivzDuK7c
# Improved by adding power supply AC 110V to DC 12V. 
#    and L298N.5V <-> PICO.VSYS. Then we have https://www.youtube.com/watch?v=NtOuNotB0Wk
# Prototype of Vacuum cleaner and show how to design https://www.youtube.com/watch?v=b9ybCF6fcZc


in1 = Pin(15, Pin.OUT)
in2 = Pin(14, Pin.OUT)

led25 = Pin(25, Pin.OUT)

ena_pwm = PWM(Pin(13))
ena_pwm.freq(1000)

led25 = Pin(25, Pin.OUT)
delay_sec = 2
# I need to give 5V to L298N with Brushed DC motor type B, 
# then the Brushed DC motor can be runned by this code.

A = [20000,25000,30000,35000,40000, 45000, 50000,55000, 60000, 65000,
     60000, 55000,50000,45000,40000,35000,30000,25000]
#duty = A[6]
#ena_pwm.duty_u16(duty)

while True:
    for duty in A:
        print("duty = "+str(duty))
        ena_pwm.duty_u16(duty)
        led25.toggle()
        in1.value(0)
        in2.value(1)
        sleep(2*delay_sec)
        led25.toggle()    
        in1.value(0)
        in2.value(0)
        sleep(delay_sec)
        led25.toggle()    
        in1.value(1)
        in2.value(0)
        sleep(2*delay_sec)
        led25.toggle()    
        in1.value(1)
        in2.value(1)
        sleep(delay_sec)