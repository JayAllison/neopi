import board
import neopixel
from PIL import Image, ImageFont, ImageDraw
import time

X_PIXELS = 16
Y_PIXELS = 16
PIXEL_COUNT = 256
BRIGHTNESS = 0.25
GPIO = board.D18

pixels = neopixel.NeoPixel(GPIO, PIXEL_COUNT, brightness=BRIGHTNESS, auto_write=False)

font = ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 16)
image = Image.new('RGB', (16, 100), (0, 0, 0))
canvas = ImageDraw.Draw(image)
message = "Merry Christmas!"
canvas.text((1, 1), message, font=font)

offset = 0
while offset < image.size[0]:
    for x in range(X_PIXELS):
        for y in range(Y_PIXELS):
            if x % 2:
                i = x*X_PIXELS + 15 - y
            else:
                i = x*X_PIXELS + y
            pixels[i] = canvas.getpixel((x+offset, y))[0:3]
    pixels.show()
    offset += 2
