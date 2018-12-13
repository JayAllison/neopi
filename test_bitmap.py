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
    Image.open('bitmaps/tree_and_gifts.png')
]

while True:

    for bitmap in bitmaps:

        width, height = bitmap.size

        for x in range(width):
            for y in range(height):
                if x % 2:
                    i = x*width + 15 - y
                else:
                    i = x*width + y
                pixels[i] = bitmap.getpixel((x, y))[0:3]
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)
