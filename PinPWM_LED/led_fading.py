from machine import Pin, PWM
from time import sleep

ledY = PWM(Pin(2))
ledY.freq(1000)

ledR = PWM(Pin(3))
ledR.freq(1500)

ledG = PWM(Pin(4))
ledG.freq(2000)

while True:
    for duty in range(0,65535):
		ledY.duty_u16(duty)
		ledR.duty_u16(duty)
		ledG.duty_u16(duty)
		sleep(0.0001)
