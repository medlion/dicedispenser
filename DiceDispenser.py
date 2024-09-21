import PCA9685
import WS2812
import random
from gpiozero import Button
from rpi5_ws2812.ws2812 import Color
import time

NUMBER_OF_SERVOS = 5 # Gonna use this number as the number of LEDs as well, since it should(tm) match up. Mostly because I'm drinking wine though
BUTTON_GPIO = 14
LEDS_PER_UNIT = 8

PCA = PCA9685.PCA9685() # Control for the servo motors
WS = WS2812.WS2812(ledsPerUnit=LEDS_PER_UNIT, units=NUMBER_OF_SERVOS)

LIGHT_SHOW_PAUSE_LENGTH = 0.5 # In seconds, how long we chill on an individual colour
LIGHT_SHOW_LENGTH = 15 # In seconds. Weird things are gonna happen if this is less than the pause length

LED_COLOUR_ARRAY = [
    Color(0, 255, 0),
    Color(255, 0, 0),
    Color(0, 0, 255),
    Color(255, 0, 255),
    Color(0, 255, 255)
]

def getRandomNumber(max, skipIf = -1): # generate a random number between 0 and max-1
    return random.randint(0, max-1)

def goServoGo(channel): # Putting this in it's own function to standardise LED lighting and such
    lightUpChannel(channel)
    PCA.spinChannel(channel=channel)
    WS.clear()

def lightUpChannel(channel):
    WS.setUnitColour(unit=channel, colour=LED_COLOUR_ARRAY[channel])

def onButtonPress():
    chosenServo = getRandomNumber(NUMBER_OF_SERVOS)
    goServoGo(chosenServo)
    
def startup():
    for i in range(NUMBER_OF_SERVOS):
        goServoGo(i)

def doALightShow(mayNotEnd = -1):
    shouldEnd = False
    count = 0
    iterations = LIGHT_SHOW_LENGTH / LIGHT_SHOW_PAUSE_LENGTH
    channelToShow = -1
    while not shouldEnd:
        channelToShow = getRandomNumber(max=NUMBER_OF_SERVOS, skipIf=channelToShow)
        lightUpChannel(channelToShow)
        time.sleep(LIGHT_SHOW_PAUSE_LENGTH)
        WS.clear()
        count += 1
        if count > iterations and not channelToShow == mayNotEnd:
            shouldEnd = True
        

if __name__=='__main__':
    #startup()
    doALightShow()

    button = Button(BUTTON_GPIO)

    # Initialize

    while (True): # Main Loop
        button.wait_for_press()
        onButtonPress()
