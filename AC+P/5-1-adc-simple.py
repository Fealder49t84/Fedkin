import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
levels = 256

index_of_waiting = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)

def WAIT():

    global index_of_waiting
    print(str(index_of_waiting) + ") ", end='')
    input("Press smth...")
    index_of_waiting = index_of_waiting + 1

def transfer(number):

    return [int(elem) for elem in bin(number)[2:].zfill(8)]

def transliterate(number):
    
    info = transfer(number)
    GPIO.output(dac, info)
    return info

try:
    while True:
        inputStr = input("Input a value between 0 and 255 (press q to exit): ")

        if inputStr.isdigit():
            value = int(inputStr)

            if value > levels - 1:
                print("Value is too big, try again: ")
                continue

            transliterate(value)

        elif inputStr == "q":
            break

        else:
            print("press correct integer: ")

except KeyboardInterrupt:
    print("You inputted Ctrl + C...")



# #check:
# n = int(input())
# print(transliterate(n))

WAIT()
GPIO.cleanup()