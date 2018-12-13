from PIL import Image


class SpriteWriter(object):

    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size

    def write_sprite(self, pixels, filename):

        bitmap = Image.open(filename)
        image_width, image_height = bitmap.size
        width = self.x_size if self.x_size < image_width else image_width
        height = self.y_size if self.y_size < image_height else image_height

        for x in range(width):
            for y in range(height):
                if x % 2:
                    i = x*width + 15 - y
                else:
                    i = x*width + y
                pixels[i] = bitmap.getpixel((x, y))[0:3]
        pixels.show()
