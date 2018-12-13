import board
import neopixel
import time

pixel_count = 256
pixels = neopixel.NeoPixel(board.D18, pixel_count, brightness=1)

colors = [(255,0,0), (128, 128, 0), (0,255,0), (0, 128, 128), (0,0,255), (128, 0, 128), (80,80,80)]

while True:
    for color in colors:
        for i in range(pixel_count):
            pixels[(255+i) % 256] = (0,0,0)
            pixels[i] = color
        for i in reversed(range(pixel_count)):
            pixels[((256-i) % 256)] = (0,0,0)
            pixels[i] = color
        for y in range(16):
            for x in range(16):
                if x % 2:
                    i = x*16 + 15 -y
                else:
                    i = x*16 + y
                pixels[(255+i) % 256] = (0,0,0)
                pixels[i] = color
        for y in reversed(range(16)):
            for x in reversed(range(16)):
                if x % 2:
                    i = x*16 + 15 -y
                else:
                    i = x*16 + y
                pixels[(255-i) % 256] = (0,0,0)
                pixels[i] = color
