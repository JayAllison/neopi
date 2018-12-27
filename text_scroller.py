from PIL import Image, ImageDraw


class TextScroller(object):

    def __init__(self, x_size, y_size, font):
        self.x_size = x_size
        self.y_size = y_size
        self.font = font

    def scroll_message(self, pixels, message, color, rate=1):
        text_size = self.font.getsize(message)
        image_width = text_size[0] + 2*self.x_size + 1
        image_height = (text_size[1] // self.y_size + 1) * self.y_size
        image = Image.new('RGB', (image_width, image_height), (0, 0, 0))
        canvas = ImageDraw.Draw(image)
        canvas.text((self.x_size, 1), message, fill=color, font=self.font)

        offset = 0
        while (offset+16) < image.size[0]:
            for x in range(self.x_size):
                for y in range(self.y_size):
                    if x % 2:
                        i = x*self.x_size + 15 - y
                    else:
                        i = x*self.x_size + y
                    pixels[i] = image.getpixel((x+offset, y))[0:3]
            pixels.show()
            offset += rate
