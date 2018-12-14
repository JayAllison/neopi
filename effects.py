import random


class EffectsGenerator(object):

    def __init__(self):
        pass

    def sparkle(self, pixels, passes=10, percent=10, rgb=(128, 128, 128)):
        pixels.fill((0, 0, 0))
        pixels.show()

        pixel_count = len(pixels)
        for _i in range(passes):
            pixels.fill((0, 0, 0))
            for _j in range(pixel_count*percent//100):
                pixels[random.randint(0, pixel_count-1)] = rgb
            pixels.show()
