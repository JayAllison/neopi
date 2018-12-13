import board
import neopixel
from PIL import Image
import time

PIXEL_COUNT = 256
BRIGHTNESS = 0.25
GPIO = board.D18

pixels = neopixel.NeoPixel(GPIO, PIXEL_COUNT, brightness=BRIGHTNESS, auto_write=False)

bitmaps = [
    Image.open('bitmaps/cross.png'),
    Image.open('bitmaps/cross.png')
]

while True:

    for bitmap in bitmaps:

        width, height = bitmap.size

        for x in range(width):
            for y in range(height):
                pixels[x*width + y] = bitmap.getpixel((x, y))[0:3]

        time.sleep(1)

        pixels.fill((0, 0, 0))

        time.sleep(1)
