#!/usr/bin/python3

import argparse
import board
import datetime
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

message = ("Countdown to Walt Disney World:", (128, 255, 128))
target_date = datetime.datetime(2019, 3, 16, 6, 0, 0)
date_color = (128, 128, 255)
image_filename = 'bitmaps/white_mickey_16x16.bmp'


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


args = parse_arguments()
time.sleep(args.timedelay)

pixels = neopixel.NeoPixel(GPIO, PIXEL_COUNT, brightness=args.brightness, auto_write=False)
scroller = text_scroller.TextScroller(X_PIXELS, Y_PIXELS, ImageFont.truetype("/home/pi/neopi/Perfect_DOS_VGA_437_Win.ttf", 16))
writer = sprite_writer.SpriteWriter(X_PIXELS, Y_PIXELS)

while True:

    # print("Displaying icon...")
    writer.fade_in_sprite(pixels, image_filename, 5)
    time.sleep(2)
    writer.fade_out_sprite(pixels, image_filename, 5)
    time.sleep(0.25)

    # print(message[0])
    scroller.scroll_message(pixels, message[0], message[1])
    clear_screen(pixels)
    time.sleep(0.25)

    countdown = target_date - datetime.datetime.now()
    hours = countdown.seconds // 60 // 60
    minutes = countdown.seconds // 60 % 60
    seconds = countdown.seconds  % 60 % 60
    countdown_string = str(countdown.days) + ' days, ' + \
        str(hours) + ':' + str(minutes) + ':' + str(seconds)
    # print(countdown_string)

    scroller.scroll_message(pixels, countdown_string, date_color)
    clear_screen(pixels)
    time.sleep(0.25)
