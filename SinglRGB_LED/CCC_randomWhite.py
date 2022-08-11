# The CCC in file name is mean CommonCathodeControl
from machine import Pin, PWM
from time import sleep
import random
# random for line RGB and change status for each 0.2 second
# hardware circuit
# connect GP2->R, GP3->G, GP4->B, GND.1 -> 330Ω -> (-)
lineR = PWM(Pin(2))
lineR.freq(1000)
lineG = PWM(Pin(3))
lineG.freq(1000)
lineB = PWM(Pin(4))
lineB.freq(1000)

led25 = Pin(25, Pin.OUT)
while True:
    led25.toggle()
    v = random.randint(0,65536)    
    lineR.duty_u16(int(v/2))
    lineG.duty_u16(v)
    lineB.duty_u16(v)
    sleep(0.5)

