from machine import Pin, PWM
from time import sleep
import random
# hardware circuit
# connect GP2->R, GP3->G, GP4->B, GND.1 -> 330Ω -> (-)
lineR = PWM(Pin(2))
lineR.freq(1000)
lineG = PWM(Pin(3))
lineG.freq(1000)
lineB = PWM(Pin(4))
lineG.freq(1000)

count = 0
while True:
    v = 65536
    dutyR = random.randint(0,v)
    dutyG = random.randint(0,v)
    dutyB = random.randint(0,v)
    A = [dutyR, dutyG, dutyB]
    for i in range(3):
        if i != count:
            A[i] = 0
    lineR.duty_u16(A[0])
    lineG.duty_u16(A[1])
    lineB.duty_u16(A[2])
    count = (count + 1)%3;
    sleep(0.7)