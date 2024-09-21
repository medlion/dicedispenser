import PCA9685
import random
from gpiozero import Button

NUMBER_OF_SERVOS = 5
BUTTON_GPIO = 14

PCA = PCA9685.PCA9685() # Control for the servo motors

def getRandomNumber(max): # generate a random number between 0 and max-1
    return random.randint(0, max-1)

def goServoGo(channel): # Putting this in it's own function to standardise LED lighting and such
    PCA.spinChannel(channel=channel)

def onButtonPress():
    chosenServo = getRandomNumber(NUMBER_OF_SERVOS)
    goServoGo(chosenServo)
    
def startup():
    for i in range(NUMBER_OF_SERVOS):
        goServoGo(i)

if __name__=='__main__':
    startup()
    
    button = Button(BUTTON_GPIO)

    # Initialize

    while (True): # Main Loop
        button.wait_for_press()
        onButtonPress()
        # Do random LED things
        # Finish LED things
        # Spin Servo
