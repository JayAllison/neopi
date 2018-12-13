import board
import neopixel
from PIL import Image
import time

PIXEL_COUNT = 256
BRIGHTNESS = 0.5
GPIO = board.D18

pixels = neopixel.NeoPixel(GPIO, PIXEL_COUNT, brightness=BRIGHTNESS, auto_write=True)

bitmap = Image.open('bitmaps/cross.png')

width, height = bitmap.size

for x in range(width):
    for y in range(height):
        pixels[x*width ++ y] = bitmap.getpixels((x, y))[0:3]
