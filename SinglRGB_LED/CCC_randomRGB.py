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
lineG.freq(1500)
lineB = PWM(Pin(4))
lineG.freq(2000)

while True:
    v = 65536
    dutyR = random.randint(0,v)
    dutyG = random.randint(0,v)
    dutyB = random.randint(0,v)
    lineR.duty_u16(dutyR)
    lineG.duty_u16(dutyG)
    lineB.duty_u16(dutyB)
    sleep(0.2)


