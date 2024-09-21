from gpiozero import Button
button = Button(8)

button.wait_for_press()
print('You pushed me')