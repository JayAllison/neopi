#!/usr/bin/python3

import argparse
import board
import effects
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
    'bitmaps/holy_family.png',
    'bitmaps/santa_hat.png',
    'bitmaps/snowflake.png',
    'bitmaps/candy_cane.png',
    'bitmaps/snowman.png'
]


def parse_arguments():
    arg_description = ""
    arg_epilog = ""
    parser = argparse.ArgumentParser(description=arg_description, epilog=arg_epilog)
    parser.add_argument('-b', '--brightness', action='store', dest="brightness", type=float,
                        default=BRIGHTNESS, help="Brightness level (0.0-1.0)")
    return parser.parse_args()


def clear_screen(neopixels):
    neopixels.fill((0, 0, 0))


def get_next_message(msg_list):
    for m in cycle(msg_list):
        yield m


def get_next_image(filename_list):
    for f in cycle(filename_list):
        yield f


args = parse_arguments()
pixels = neopixel.NeoPixel(GPIO, PIXEL_COUNT, brightness=args.brightness, auto_write=False)
scroller = text_scroller.TextScroller(X_PIXELS, Y_PIXELS, ImageFont.truetype("Perfect DOS VGA 437 Win.ttf", 16))
writer = sprite_writer.SpriteWriter(X_PIXELS, Y_PIXELS)
effector = effects.EffectsGenerator()

message_list = get_next_message(messages)
image_list = get_next_image(image_filenames)

while True:

    filename = next(image_list)
    writer.fade_in_sprite(pixels, filename, 5)
    time.sleep(2)
    writer.fade_out_sprite(pixels, filename, 5)
    time.sleep(0.25)

    message = next(message_list)
    scroller.scroll_message(pixels, message[0], message[1])
    clear_screen(pixels)
    time.sleep(0.25)

    filename = next(image_list)
    writer.fade_in_sprite(pixels, filename, 5)
    time.sleep(2)
    writer.fade_out_sprite(pixels, filename, 5)
    time.sleep(0.25)

    effector.sparkle(pixels, percent=5, rgb=(64, 64, 64))
