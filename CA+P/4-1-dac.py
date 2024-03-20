import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, 0)

a = -1

try:
    a = int(input("Input decimal number: "))

except ValueError:

    try:
        a = int(input("Incorrect form of decimal number, try again: "))

    except ValueError:
        print("Ending trying to input...")

try:
    meaning = bin(a)[2::]
    meaning = meaning[::-1]

    for i in range(len(meaning)): GPIO.output(dac[i], int(meaning[i]))

    input("Press any button to end displaying... ")

except ValueError:
    print("Incorrect input.")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()