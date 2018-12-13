import board
from itertools import cycle
import neopixel
from PIL import ImageFont
import sprite_writer
import text_scroller
import time

X_PIXELS = 16
Y_PIXELS = 16
PIXEL_COUNT = X_PIXELS * Y_PIXELS
BRIGHTNESS = 0.5
GPIO = board.D18

messages = [
    ("Merry Christmas!", (0, 255, 0)),
    ("Happy Holidays!", (255, 0, 0)),
]

image_filenames = [
    'bitmaps/synapse.png',
    'bitmaps/star.png',
    'bitmaps/tree_and_gifts.png',
    'bitmaps/manger.png',
    'bitmaps/santa_hat.png',
    'bitmaps/snowflake.png',
]


def clear_screen(neopixels):
    neopixels.fill((0, 0, 0))


def get_next_message(msg_list):
    for m in cycle(msg_list):
        yield m


def get_next_image(filename_list):
    for f in cycle(filename_list):
        yield f


pixels = neopixel.NeoPixel(GPIO, PIXEL_COUNT, brightness=BRIGHTNESS, auto_write=False)
scroller = text_scroller.TextScroller(X_PIXELS, Y_PIXELS, ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 16))
writer = sprite_writer.SpriteWriter(X_PIXELS, Y_PIXELS)

# TODO: add some cool animation in between

message_list = get_next_message(messages)
image_list = get_next_image(image_filenames)

while True:

    filename = next(image_list)
    writer.write_sprite(pixels, filename)
    time.sleep(1)
    clear_screen(pixels)
    time.sleep(0.25)

    message = next(message_list)
    scroller.scroll_message(pixels, message[0], message[1])
    clear_screen(pixels)
    time.sleep(0.25)

    filename = next(image_list)
    writer.write_sprite(pixels, filename)
    time.sleep(1)
    clear_screen(pixels)
    time.sleep(0.25)
