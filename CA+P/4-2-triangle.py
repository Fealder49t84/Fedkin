import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dec2bin(a):

    a = bin(a)[2::]
    a = a[::-1]
    return [int(i) for i in a] + [0 for i in range(8 - len(a))]

def including_GPIO(list, a):

    for i in range(8): GPIO.output(dac[i], list[i])
    time.sleep(a/512)

try:
    while True:
        a = int(input("Input period of time:"))

        for i in range(3):

            for y in range(1, 256):
                including_GPIO(dec2bin(y), a)

            for y in range(256, 0):
                including_GPIO(dec2bin(y), a)

except ValueError:

    print("Ending...")
    time.sleep(1)

finally:
    GPIO.outset(dac, 0)
    GPIO.cleanup()