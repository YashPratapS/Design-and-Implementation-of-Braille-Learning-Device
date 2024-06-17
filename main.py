import subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
mode_pins = [2, 3, 4, 17]

for pin in mode_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def mode_1():
    subprocess.call(['python', 'mode1.py'])

def mode_2():
    subprocess.call(['python', 'mode2.py'])

def mode_3():
    subprocess.call(['python', 'mode3.py'])

def main():
    while True:
        print("\nSelect a mode:")
        print("1. Mode 1")
        print("2. Mode 2")
        print("3. Mode 3")
        print("4. Exit")

        for i, pin in enumerate(mode_pins):
            if GPIO.input(pin) == GPIO.LOW:
                if i == 0:
                    mode_1()
                elif i == 1:
                    mode_2()
                elif i == 2:
                    mode_3()
                elif i == 3:
                    break

if __name__ == "__main__":
    main()
