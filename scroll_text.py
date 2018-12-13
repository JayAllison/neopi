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
messages = [
    ("Merry Christmas!", (0, 255, 0)),
    ("Happpy Holidays!", (255, 0, 0)),
]

while True:
    for message in messages:
        text_size = font.getsize(message[0])
        image_width = (text_size[0] // X_PIXELS + 2) * X_PIXELS
        image_height = (text_size[1] // Y_PIXELS + 1) * Y_PIXELS
        image = Image.new('RGB', (image_width, image_height), (0, 0, 0))
        canvas = ImageDraw.Draw(image)
        canvas.text((X_PIXELS, 1), message[0], fill=message[1], font=font)

        offset = 0
        while (offset+16) < image.size[0]:
            for x in range(X_PIXELS):
                for y in range(Y_PIXELS):
                    if x % 2:
                        i = x*X_PIXELS + 15 - y
                    else:
                        i = x*X_PIXELS + y
                    pixels[i] = image.getpixel((x+offset, y))[0:3]
            pixels.show()
            offset += 1
