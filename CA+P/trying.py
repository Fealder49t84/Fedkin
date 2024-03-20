import RPi.GPIO as GPIO
import time

N = 8

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, 0)

k = GPIO.PWM(N, 5)
k.start(1)
input("press any buttom to stop: ...")
k.stop()

time.sleep(1)

p = [GPIO.PWM(dac[i], 10) for i in range(0, len(dac), 2)]
for i in range(len(p)): p[i].start(1)
time.sleep(2)
for i in range(len(p)): p[i].stop()

GPIO.output(dac, 1)
time.sleep(1)

GPIO.cleanup()