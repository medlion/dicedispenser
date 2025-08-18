from gpiozero import Button
import DiceDispenser
button = Button(14)

button.wait_for_press()
print('You pushed me')
DiceDispenser.goServoGo(0)