import argparse
import board
import neopixel

pixel_count = 256


def parse_arguments_into_color():
    arg_description = ""
    arg_epilog = ""
    parser = argparse.ArgumentParser(description=arg_description, epilog=arg_epilog)
    parser.add_argument('red_level', metavar='R', type=int, help='Red Level (0-255)')
    parser.add_argument('green_level', metavar='G', type=int, help='Green Level (0-255)')
    parser.add_argument('blue_level', metavar='B', type=int, help='Blue Level (0-255)')
    args = parser.parse_args()
    return args.red_level, args.green_level, args.blue_level


def fill_screen(neopixels, color):
    neopixels.fill(color)


pixels = neopixel.NeoPixel(board.D18, pixel_count, brightness=1)
color = parse_arguments_into_color()
fill_screen(pixels, color)
