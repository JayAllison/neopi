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

messages = [
    {
        "message": {
            "text": "Countdown to Mark's Birthday:",
            "color": (0, 0, 255)
        },
        "target_date": datetime.datetime(2019, 4, 3, 0, 0, 0),
        "date_color": (0, 255, 0),
        "image_filename": '/home/pi/neopi/bitmaps/mark-16x16.jpg'
    },
    {
        "message": {
            "text": "Countdown to Paul's Birthday:",
            "color": (255, 255, 0)
        },
        "target_date": datetime.datetime(2019, 4, 7, 0, 0, 0),
        "date_color": (255, 0, 0),
        "image_filename": '/home/pi/neopi/bitmaps/paul-16x16.jpg'
    }
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


args = parse_arguments()
time.sleep(args.timedelay)

pixels = neopixel.NeoPixel(GPIO, PIXEL_COUNT, brightness=args.brightness, auto_write=False)
scroller = text_scroller.TextScroller(X_PIXELS, Y_PIXELS,
                                      ImageFont.truetype("/home/pi/neopi/Perfect_DOS_VGA_437_Win.ttf", 16))
writer = sprite_writer.SpriteWriter(X_PIXELS, Y_PIXELS)

while True:

    for message_data in messages:

        # print("Displaying icon...")
        writer.fade_in_sprite(pixels, message_data["image_filename"], 5)
        time.sleep(2)
        writer.fade_out_sprite(pixels, message_data["image_filename"], 5)
        time.sleep(0.25)

        # print(message[0])
        scroller.scroll_message(pixels, message_data["message"]["text"], message_data["message"]["color"], 2)
        clear_screen(pixels)
        time.sleep(0.25)

        countdown = message_data["target_date"] - datetime.datetime.now()
        day_word = "day" if countdown.days == 1 else "days"
        hours = countdown.seconds // 60 // 60
        if hours < 10:
            hours = '0' + str(hours)
        minutes = countdown.seconds // 60 % 60
        if minutes < 10:
            minutes = '0' + str(minutes)
        seconds = countdown.seconds % 60 % 60
        if seconds < 10:
            seconds = '0' + str(seconds)
        countdown_string = str(countdown.days) + ' ' + day_word + ' ' + \
            str(hours) + ':' + str(minutes) + ':' + str(seconds)
        # print(countdown_string)

        scroller.scroll_message(pixels, countdown_string, message_data["date_color"], 2)
        clear_screen(pixels)
        time.sleep(0.25)
