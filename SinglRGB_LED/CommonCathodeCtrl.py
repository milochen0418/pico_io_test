from machine import Pin, PWM
from time import sleep

# hardware circuit
# connect GP2->R, GP3->G, GP4->B, GND.1 -> 330Ω -> (-)
lineR = PWM(Pin(2))
lineR.freq(1000)
lineG = PWM(Pin(3))
lineG.freq(1500)
lineB = PWM(Pin(4))
lineG.freq(2000)

while True:
    for duty in range(0,65535):
		lineR.duty_u16(duty) #red
		lineG.duty_u16(duty) #green
		lineB.duty_u16(duty) #blue
		sleep(0.0001)


