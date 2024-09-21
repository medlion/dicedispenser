import PCA9685
import WS2812
import random
from gpiozero import Button

NUMBER_OF_SERVOS = 5 # Gonna use this number as the number of LEDs as well, since it should(tm) match up. Mostly because I'm drinking wine though
BUTTON_GPIO = 14
LEDS_PER_UNIT = 8

PCA = PCA9685.PCA9685() # Control for the servo motors
WS = WS2812.WS2812(ledsPerUnit=LEDS_PER_UNIT, units=NUMBER_OF_SERVOS)

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
