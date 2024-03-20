import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.output(dac, 0)

a = -1

while True:
    try:
        a = input("Inputting value... ")
        
        if a == "q":
            break

        a = float(a)

        # print("...\t", float(int(a)), a)

        if float(int(a)) != a:

            if a < 0:
                print("\tIt's float and it's negative, you mean?")
            else:
                print("\tIt's float and it's positive, you mean?")

        else:

            if a < 0:
                print("\tIt's int and it's negative, you mean?")
            else:
                print("\tIt's int and it's positive, you mean?")

        meaning = bin(int(round(float(a), 0)))[2::]
        meaning = meaning[::-1]

        for i in range(len(meaning)): GPIO.output(dac[i], int(meaning[i]))

        input("Press any button to end displaying... ")

    except ValueError:
        print("ERROR: Incorrect number form.")
        continue

    finally:
        GPIO.output(dac, 0)

GPIO.cleanup()