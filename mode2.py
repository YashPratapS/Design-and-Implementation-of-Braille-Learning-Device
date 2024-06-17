import RPi.GPIO as GPIO
import time
import pyttsx3

solenoid_pins = [17, 18, 22, 23, 24, 25]

solenoid_mapping = {
    ' ': [0, 0, 0, 0, 0, 0],  
    'A': [1, 0, 0, 0, 0, 0],
    'B': [1, 1, 0, 0, 0, 0],
    'C': [1, 0, 1, 0, 0, 0],
    'D': [1, 0, 1, 1, 0, 0],
    'E': [1, 0, 0, 1, 0, 0],
    'F': [1, 1, 1, 0, 0, 0],
    'G': [1, 1, 1, 1, 0, 0],
    'H': [1, 1, 0, 1, 0, 0],
    'I': [0, 1, 1, 0, 0, 0],
    'J': [0, 1, 1, 1, 0, 0],
    'K': [1, 0, 0, 0, 1, 0],
    'L': [1, 1, 0, 0, 1, 0],
    'M': [1, 0, 1, 0, 1, 0],
    'N': [1, 0, 1, 1, 1, 0],
    'O': [1, 0, 0, 1, 1, 0],
    'P': [1, 1, 1, 0, 1, 0],
    'Q': [1, 1, 1, 1, 1, 0],
    'R': [1, 1, 0, 1, 1, 0],
    'S': [0, 1, 1, 0, 1, 0],
    'T': [0, 1, 1, 1, 1, 0],
    'U': [1, 0, 0, 0, 1, 1],
    'V': [1, 1, 0, 0, 1, 1],
    'W': [0, 1, 1, 1, 0, 1],
    'X': [1, 0, 1, 0, 1, 1],
    'Y': [1, 0, 1, 1, 1, 1],
    'Z': [1, 0, 0, 1, 1, 1],
    '0': [0, 1, 1, 1, 0, 0],
    '1': [1, 0, 0, 0, 0, 0],
    '2': [1, 1, 0, 0, 0, 0],
    '3': [1, 0, 1, 0, 0, 0],
    '4': [1, 0, 1, 1, 0, 0],
    '5': [1, 0, 0, 1, 0, 0],
    '6': [1, 1, 1, 0, 0, 0],
    '7': [1, 1, 1, 1, 0, 0],
    '8': [1, 1, 0, 1, 0, 0],
    '9': [0, 1, 1, 0, 0, 0],
}

def setup():
    GPIO.setmode(GPIO.BCM)

    for pin in solenoid_pins:
        GPIO.setup(pin, GPIO.OUT)

def braille_print(character):
    if character.upper() in solenoid_mapping:
        solenoid_config = solenoid_mapping[character.upper()]
        for i, pin in enumerate(solenoid_pins):
            GPIO.output(pin, solenoid_config[i])
        time.sleep(3)  
    else:
        print(f"Character '{character}' not supported for Braille printing")

def braille_print_string(input_string):
    for char in input_string:
        braille_print(char)
        engine = pyttsx3.init()
        engine.say(char)
        engine.runAndWait()

def main():
    print("Braille Learning Device")
    print("File Text: This will be transmitted to Raspberry Pi and displayed on a Braille in 2x3 matrix")
    file = open("detected_text.txt", "r+")
    braille_print_string(file.read())
    # while True:
    #     user_input = input("Enter a string: ")
    #     if user_input:
    #         braille_print_string(user_input)

if __name__ == "__main__":
    try:
        setup()
        main()
    finally:
        GPIO.cleanup()  
