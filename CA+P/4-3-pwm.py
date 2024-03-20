import RPi.GPIO as GPIO

out = 2
duty_cycle = 0
dac = [8, 11, 7, 1, 0, 5, 12, 6]
LEDS = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(LEDS, GPIO.OUT)

GPIO.setup(24, GPIO.OUT)

pvm = GPIO.PWM(out, 1000)
pvm_out = GPIO.PWM(24, 1000)

pvm.start(duty_cycle)
pvm_out.start(duty_cycle)

try:
    while True:
        duty_cycle = float(input("duty_cycle? "))
        print(3.3*duty_cycle/100)
        
        pvm_out.ChangeDutyCycle(duty_cycle)
        pvm.ChangeDutyCycle(duty_cycle)
        

except ValueError:
    print("Ending...")

finally:
    pvm.stop()
    pvm_out.stop()
    GPIO.output(dac, 0)
    GPIO.output(LEDS, 0)
    GPIO.cleanup()