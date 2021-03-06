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

# TODO: add an exit handler to clear the screen when the script is stopped
# TODO: add logging to syslog (or a custom log file)
# TODO: make sure exceptions go into the syslog, too (see BlindSteering project for an example)

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
    '/home/pi/neopi/bitmaps/synapse.png',
    '/home/pi/neopi/bitmaps/star.png',
    '/home/pi/neopi/bitmaps/tree_and_gifts.png',
    '/home/pi/neopi/bitmaps/holy_family.png',
    '/home/pi/neopi/bitmaps/santa_hat.png',
    '/home/pi/neopi/bitmaps/snowflake.png',
    '/home/pi/neopi/bitmaps/candy_cane.png',
    '/home/pi/neopi/bitmaps/snowman.png'
]


def parse_arguments():
    arg_description = ""
    arg_epilog = ""
    parser = argparse.ArgumentParser(description=arg_description, epilog=arg_epilog)
    parser.add_argument('-b', '--brightness', action='store', dest="brightness", type=float,
                        default=BRIGHTNESS, help="Brightness level (0.0-1.0)")
    parser.add_argument('-t', '--timedelay', action='store', dest="timedelay", type=int,
                        default=BRIGHTNESS, help="Startup time delay")
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
time.sleep(args.timedelay)
pixels = neopixel.NeoPixel(GPIO, PIXEL_COUNT, brightness=args.brightness, auto_write=False)
scroller = text_scroller.TextScroller(X_PIXELS, Y_PIXELS, ImageFont.truetype("/home/pi/neopi/Perfect_DOS_VGA_437_Win.ttf", 16))
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
