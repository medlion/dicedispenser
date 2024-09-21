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

    def clear(self) -> None:
        self.driver.clear()

    def setUnitColour(self, unit, colour): # unit order between 0 and units-1, Colour is a color object
        print ('Setting unit colour for unit ' + unit)
        startingLED = unit * self.ledsPerUnit
        print ('Starting at LED ' + startingLED)
        for i in range (startingLED, self.ledsPerUnit):
            print ('Setting LED colour for LED ' + i)
            self.driver.set_pixel_color(i, colour)
        self.driver.show()