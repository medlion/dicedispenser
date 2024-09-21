import PCA9685
import random
from gpiozero import Button

NUMBER_OF_SERVOS = 5
BUTTON_GPIO = 14

def getRandomNumber(max): # generate a random number between 0 and max-1
    return random.randint(0, max-1)

def onButtonPress():
    chosenServo = getRandomNumber(NUMBER_OF_SERVOS)
    print(chosenServo)

if __name__=='__main__':
    PCA = PCA9685.PCA9685 # Control for the servo motors
    button = Button(BUTTON_GPIO)

    # Initialize

    while (True): # Main Loop
        button.wait_for_press()
        onButtonPress()
        # Do random LED things
        # Finish LED things
        # Spin Servo
