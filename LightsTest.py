from rpi5_ws2812.ws2812 import Color, WS2812SpiDriver
import time

if __name__ == "__main__":

    # Initialize the WS2812 strip with 100 leds and SPI channel 0, CE0
    strip = WS2812SpiDriver(spi_bus=0, spi_device=0, led_count=40).get_strip()
    color = Color(0, 0, 255)
    for i in range (0, 40):
        strip.set_pixel_color(i=i, color=color)
        time.sleep(1)