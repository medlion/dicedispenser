from rpi5_ws2812.ws2812 import Color, WS2812SpiDriver

class WS2812:

    driver = 0
    ledsPerUnit = 0
    units = 0

    def __init__(self, ledsPerUnit, units) -> None:
        self.ledsPerUnit = ledsPerUnit
        self.units = units
        ledCount = ledsPerUnit*units
        self.driver = WS2812SpiDriver(spi_bus=0, spi_device=0, led_count=ledCount).get_strip()
        self.driver.set_brightness(0.25)

    def clear(self) -> None:
        self.driver.clear()

    def setUnitColour(self, unit, colour): # unit order between 0 and units-1, Colour is a color object
        startingLED = unit * self.ledsPerUnit
        for i in range (startingLED, startingLED+self.ledsPerUnit):
            self.driver.set_pixel_color(i, colour)
        self.driver.show()

    def setAllColour(self, colour):
        self.driver.set_all_pixels(colour)