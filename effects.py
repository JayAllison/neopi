import random


class EffectsGenerator(object):

    def __init__(self):
        pass

    def sparkle(self, pixels, count=10):
        pixels.clear()
        pixels.show()

        pixel_count = len(pixels)
        for _i in range(count):
            for _j in range(pixel_count/10):
                pixels[random.randint(0, pixel_count)] = (128, 128, 128)
            pixels.show()
