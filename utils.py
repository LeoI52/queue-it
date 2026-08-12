"""
@author : Léo Imbert
@created : 15/10/2024
@updated : 05/05/2026
"""

#? -------------------- IMPORTATIONS -------------------- ?#

import random
import pyxel
import math

#? -------------------- COLORS -------------------- ?#

DEFAULT_PYXEL_COLORS = [0x000000, 0x2B335F, 0x7E2072, 0x19959C, 0x8B4852, 0x395C98, 0xA9C1FF, 0xEEEEEE, 0xD4186C, 0xD38441, 0xE9C35B, 0x70C6A9, 0x7696DE, 0xA3A3A3, 0xFF9798, 0xEDC7B0]
DEFAULT_PICO8_COLORS = [0x000000, 0x1D2B53, 0x7E2553, 0x008751, 0xAB5236, 0x5F574F, 0xC2C3C7, 0xFFF1E8, 0xFF004D, 0xFFA300, 0xFFEC27, 0x00E436, 0x29ADFF, 0x83769C, 0xFF77A8, 0xFFCCAA]

NORMAL_COLOR_MODE = 0
ROTATING_COLOR_MODE = 1
RANDOM_COLOR_MODE = 2

#? -------------------- DIRECTIONS -------------------- ?#

VERTICAL = 0
HORIZONTAL = 1

BOTTOM = 0
TOP = 1
LEFT = 2
RIGHT = 3
TOP_LEFT = 4
TOP_RIGHT = 5
BOTTOM_RIGHT = 6
BOTTOM_LEFT = 7
CENTER = 8

#? -------------------- FONTS -------------------- ?#

FONT_PYXEL = {
    " ":[[0,0]],

    "A":[[0,1,0],[1,0,1],[1,1,1],[1,0,1],[1,0,1]],
    "B":[[1,1,0],[1,0,1],[1,1,0],[1,0,1],[1,1,0]],
    "C":[[0,1,1],[1,0,0],[1,0,0],[1,0,0],[0,1,1]],
    "D":[[1,1,0],[1,0,1],[1,0,1],[1,0,1],[1,1,0]],
    "E":[[1,1,1],[1,0,0],[1,1,0],[1,0,0],[1,1,1]],
    "F":[[1,1,1],[1,0,0],[1,1,1],[1,0,0],[1,0,0]],
    "G":[[0,1,1],[1,0,0],[1,1,1],[1,0,1],[0,1,1]],
    "H":[[1,0,1],[1,0,1],[1,1,1],[1,0,1],[1,0,1]],
    "I":[[1,1,1],[0,1,0],[0,1,0],[0,1,0],[1,1,1]],
    "J":[[0,0,1],[0,0,1],[0,0,1],[1,0,1],[0,1,0]],
    "K":[[1,0,1],[1,0,1],[1,1,0],[1,0,1],[1,0,1]],
    "L":[[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,1,1]],
    "M":[[1,0,1],[1,1,1],[1,1,1],[1,0,1],[1,0,1]],
    "N":[[1,1,0],[1,0,1],[1,0,1],[1,0,1],[1,0,1]],
    "O":[[0,1,0],[1,0,1],[1,0,1],[1,0,1],[0,1,0]],
    "P":[[1,1,0],[1,0,1],[1,1,0],[1,0,0],[1,0,0]],
    "Q":[[0,1,0],[1,0,1],[1,0,1],[1,1,1],[0,1,1]],
    "R":[[1,1,0],[1,0,1],[1,1,1],[1,1,0],[1,0,1]],
    "S":[[0,1,1],[1,0,0],[0,1,0],[0,0,1],[1,1,0]],
    "T":[[1,1,1],[0,1,0],[0,1,0],[0,1,0],[0,1,0]],
    "U":[[1,0,1],[1,0,1],[1,0,1],[1,0,1],[0,1,1]],
    "V":[[1,0,1],[1,0,1],[1,0,1],[1,0,1],[0,1,0]],
    "W":[[1,0,1],[1,0,1],[1,1,1],[1,1,1],[1,0,1]],
    "X":[[1,0,1],[1,0,1],[0,1,0],[1,0,1],[1,0,1]],
    "Y":[[1,0,1],[1,0,1],[0,1,0],[0,1,0],[0,1,0]],
    "Z":[[1,1,1],[0,0,1],[0,1,0],[1,0,0],[1,1,1]],

    "a":[[0,0,0],[0,1,1],[1,0,1],[1,0,1],[0,1,1]],
    "b":[[1,0,0],[1,1,0],[1,0,1],[1,0,1],[1,1,0]],
    "c":[[0,0,0],[0,1,1],[1,0,0],[1,0,0],[0,1,1]],
    "d":[[0,0,1],[0,1,1],[1,0,1],[1,0,1],[0,1,1]],
    "e":[[0,0,0],[0,1,1],[1,0,1],[1,1,0],[0,1,1]],
    "f":[[0,0,1],[0,1,0],[1,1,1],[0,1,0],[0,1,0]],
    "g":[[0,0,0],[0,1,1],[1,0,1],[1,1,1],[0,0,1],[0,1,0]],
    "h":[[1,0,0],[1,1,0],[1,0,1],[1,0,1],[1,0,1]],
    "i":[[1],[0],[1],[1],[1]],
    "j":[[0,0,1],[0,0,0],[0,0,1],[0,0,1],[1,0,1],[0,1,0]],
    "k":[[1,0,0],[1,0,1],[1,1,0],[1,1,0],[1,0,1]],
    "l":[[1,1,0],[0,1,0],[0,1,0],[0,1,0],[1,1,1]],
    "m":[[0,0,0],[1,1,1],[1,1,1],[1,1,1],[1,0,1]],
    "n":[[0,0,0],[1,1,0],[1,0,1],[1,0,1],[1,0,1]],
    "o":[[0,0,0],[0,1,0],[1,0,1],[1,0,1],[0,1,0]],
    "p":[[0,0,0],[1,1,0],[1,0,1],[1,0,0],[1,1,0],[1,0,0]],
    "q":[[0,0,0],[0,1,1],[1,0,1],[1,0,1],[0,1,1],[0,0,1]],
    "r":[[0,0,0],[0,1,1],[1,0,0],[1,0,0],[1,0,0]],
    "s":[[0,0,0],[0,1,1],[1,1,0],[0,1,1],[1,1,0]],
    "t":[[0,1,0],[1,1,1],[0,1,0],[0,1,0],[0,1,1]],
    "u":[[0,0,0],[1,0,1],[1,0,1],[1,0,1],[0,1,1]],
    "v":[[0,0,0],[1,0,1],[1,0,1],[1,0,1],[0,1,0]],
    "w":[[0,0,0],[1,0,1],[1,0,1],[1,1,1],[1,1,1]],
    "x":[[0,0,0],[1,0,1],[0,1,0],[0,1,0],[1,0,1]],
    "y":[[0,0,0],[1,0,1],[1,0,1],[0,1,1],[0,0,1],[0,1,0]],
    "z":[[0,0,0],[1,1,1],[0,0,1],[0,1,0],[1,1,1]],

    "1":[[0,1],[1,1],[0,1],[0,1],[0,1]],
    "2":[[1,1,0],[0,0,1],[0,1,0],[1,0,0],[1,1,1]],
    "3":[[1,1,0],[0,0,1],[0,1,0],[0,0,1],[1,1,0]],
    "4":[[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]],
    "5":[[1,1,1],[1,0,0],[1,1,0],[0,0,1],[1,1,0]],
    "6":[[0,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]],
    "7":[[1,1,1],[0,0,1],[0,1,0],[1,0,0],[1,0,0]],
    "8":[[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]],
    "9":[[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,0]],
    "0":[[0,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,0]],
    "+":[[0,0,0],[0,1,0],[1,1,1],[0,1,0]],
    "-":[[0,0,0],[0,0,0],[1,1,1]],
    "*":[[1,0,1],[0,1,0],[1,1,1],[0,1,0],[1,0,1]],
    "/":[[0,0,1],[0,0,1],[0,1,0],[1,0,0],[1,0,0]],
    "^":[[0,1,0],[1,0,1]],
    "=":[[0,0,0],[1,1,1],[0,0,0],[1,1,1]],
    "%":[[1,0,0],[0,0,1],[0,1,0],[1,0,0],[0,0,1]],

    ",":[[0,0],[0,0],[0,0],[0,0],[0,1],[1,0]],
    ".":[[0,0],[0,0],[0,0],[0,0],[0,1]],
    ";":[[0,0],[0,0],[0,1],[0,0],[0,1],[1,0]],
    "?":[[1,1,1],[0,0,1],[0,1,0],[0,0,0],[0,1,0]],
    "!":[[0,1],[0,1],[0,1],[0,0],[0,1]],
    ":":[[0,0],[0,1],[0,0],[0,1]],
    '"':[[1,0,1],[1,0,1]],
    "'":[[0,1],[0,1]],

    "(":[[0,1],[1,0],[1,0],[1,0],[0,1]],
    ")":[[1,0],[0,1],[0,1],[0,1],[1,0]],
    "{":[[0,1,1],[0,1,0],[1,1,0],[0,1,0],[0,1,1]],
    "}":[[1,1,0],[0,1,0],[0,1,1],[0,1,0],[1,1,0]],
    "[":[[1,1],[1,0],[1,0],[1,0],[1,1]],
    "]":[[1,1],[0,1],[0,1],[0,1],[1,1]],

    "<":[[0,0,1],[0,1,0],[1,0,0],[0,1,0],[0,0,1]],
    ">":[[1,0,0],[0,1,0],[0,0,1],[0,1,0],[1,0,0]],
    "&":[[0,1,0],[1,0,1],[0,1,0],[1,0,1],[1,1,0]],
    "~":[[0,1,1],[1,1,0]],
    "#":[[1,0,1],[1,1,1],[1,0,1],[1,1,1],[1,0,1]],
    "@":[[0,1,0],[1,0,1],[1,0,1],[1,0,0],[0,1,1]],
    "|":[[0,1],[0,1],[0,1],[0,1],[0,1]],
    "_":[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[1,1,1]],
}

FONT_DEFAULT = {
    " ":[[0,0,0,0]],

    "A":[[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1]],
    "B":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,0]],
    "C":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,1,0,0,1,1],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[0,1,1,0,0,1,1],[0,0,1,1,1,1,0]],
    "D":[[0,0,0,0,0,0,0],[1,1,1,1,1,0,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[1,1,1,1,1,0,0]],
    "E":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[0,1,1,0,0,0,1],[0,1,1,0,1,0,0],[0,1,1,1,1,0,0],[0,1,1,0,1,0,0],[0,1,1,0,0,0,1],[1,1,1,1,1,1,1]],
    "F":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[0,1,1,0,0,0,1],[0,1,1,0,1,0,0],[0,1,1,1,1,0,0],[0,1,1,0,1,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "G":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,1,0,0,1,1],[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[1,1,0,0,1,1,1],[0,1,1,0,0,1,1],[0,0,1,1,1,1,1]],
    "H":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1]],
    "I":[[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1]],
    "J":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,1],[0,0,0,0,1,1,0],[0,0,0,0,1,1,0],[0,0,0,0,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,1,0,0]],
    "K":[[0,0,0,0,0,0,0],[1,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[0,1,1,1,1,0,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "L":[[0,0,0,0,0,0,0],[1,1,1,1,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,1]],
    "M":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,0,1,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "N":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,1,0,0,1,1],[1,1,1,1,0,1,1],[1,1,0,1,1,1,1],[1,1,0,0,1,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "O":[[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0]],
    "P":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "Q":[[0,0,0,0,0,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,1,1,0,1],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "R":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,1,1,0],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "S":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "T":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,0,1,1,0,1],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0]],
    "U":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "V":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0]],
    "W":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1],[1,1,0,1,0,1,1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,0,0,0,1,1]],
    "X":[[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,0,1,1]],
    "Y":[[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,1,1,1,1,0]],
    "Z":[[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,1,0,0,0,1,1],[1,0,0,0,1,1,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,1],[0,1,1,0,0,1,1],[1,1,1,1,1,1,1]],

    "a":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "b":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,0,1,1,1,0]],
    "c":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "d":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "e":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "f":[[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,1,0,1,1],[0,1,1,0,0,0],[1,1,1,1,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[1,1,1,1,0,0]],
    "g":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "h":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,1,1,0],[0,1,1,1,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "i":[[0,0,0,0],[0,1,1,0],[0,0,0,0],[1,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    "j":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,0,0],[0,0,0,1,1,1],[0,0,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "k":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[0,1,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,1,0,0,1,1]],
    "l":[[0,0,0,0],[1,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    "m":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,0,1,1,0],[1,1,1,1,1,1,1],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,0,0,0,1,1]],
    "n":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1]],
    "o":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "p":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "q":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,0,1,1],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,1,1,0],[0,0,0,0,1,1,0],[0,0,0,1,1,1,1]],
    "r":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,1,0,1,1],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "s":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "t":[[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[1,1,1,1,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[0,1,1,0,1,1],[0,0,1,1,1,0]],
    "u":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1]],
    "v":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0]],
    "w":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,1,1,1,1,1],[0,1,1,0,1,1,0]],
    "x":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1]],
    "y":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "z":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[1,0,0,1,1,0],[0,0,1,1,0,0],[0,1,1,0,0,1],[1,1,1,1,1,1]],

    "à":[[0,0,1,1,0,0,0],[0,0,0,0,1,1,0],[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "ç":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,0,1,0,0],[0,0,1,0,0,0]],
    "é":[[0,0,0,1,1,0],[0,1,1,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "è":[[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],

    "1":[[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[1,1,1,1,1,1]],
    "2":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,1,1,1,1,0],[1,1,0,0,0,0],[1,1,0,0,1,1],[1,1,1,1,1,1]],
    "3":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,0,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "4":[[0,0,0,0,0,0,0],[0,0,0,1,1,1,0],[0,0,1,1,1,1,0],[0,1,1,0,1,1,0],[1,1,0,0,1,1,0],[1,1,1,1,1,1,1],[0,0,0,0,1,1,0],[0,0,0,1,1,1,1]],
    "5":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,1,0,0,0,1],[1,1,0,0,0,0],[1,1,1,1,1,0],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "6":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "7":[[0,0,0,0,0,0],[1,1,1,1,1,1],[1,1,0,0,1,1],[0,0,0,0,1,1],[0,0,0,1,1,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0]],
    "8":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "9":[[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "0":[[0,0,0,0,0,0,0],[0,1,1,1,1,1,0],[1,1,0,0,0,1,1],[1,1,0,0,1,1,1],[1,1,0,1,0,1,1],[1,1,1,0,0,1,1],[1,1,0,0,0,1,1],[0,1,1,1,1,1,0]],
    "+":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]],
    "-":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,1]],
    "*":[[0,0,0],[1,0,1],[0,1,0],[1,0,1]],
    "/":[[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,1,0],[0,0,0,1,1,0],[0,0,1,1,0,0],[0,0,1,0,0,0],[0,1,1,0,0,0],[1,1,0,0,0,0]],
    "^":[[0,0,0],[0,1,0],[1,0,1]],
    "=":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1]],
    "%":[[0,1,0,0,0,0,0],[1,0,1,0,1,1,0],[0,1,0,0,1,0,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,0],[0,0,1,0,0,1,0],[0,1,1,0,1,0,1],[1,1,0,0,0,1,0]],

    ",":[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,1,1],[0,1,1],[1,1,0]],
    ".":[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,1],[1,1]],
    ";":[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,1,1],[0,1,1],[0,0,0],[0,1,1],[0,1,1],[1,1,0]],
    "?":[[0,0,0,0],[1,1,1,0],[1,0,1,1],[0,0,1,1],[0,1,1,0],[0,0,0,0],[0,1,1,0],[0,1,1,0]],
    "!":[[0,0],[1,1],[1,1],[1,1],[1,1],[0,0],[1,1],[1,1]],
    ":":[[0,0],[0,0],[1,1],[1,1],[0,0],[1,1],[1,1]],
    '"':[[0,0,0,0],[0,1,0,1],[0,1,0,1],[1,0,1,0],[1,0,1,0]],
    "'":[[0,0,0,0],[0,0,1,1],[0,0,1,1],[0,1,1,0],[0,1,1,0]],

    "(":[[0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[0,0,1]],
    ")":[[0,0,0],[1,0,0],[0,1,0],[0,0,1],[0,0,1],[0,0,1],[0,1,0],[1,0,0]],
    "{":[[0,0,0],[0,0,1],[0,1,0],[0,1,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1]],
    "}":[[0,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1],[0,1,0],[0,1,0],[1,0,0]],
    "[":[[0,0,0],[1,1,1],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,1,1]],
    "]":[[0,0,0],[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[1,1,1]],

    "<":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1],[0,1,1,0],[1,0,0,0],[0,1,1,0],[0,0,0,1]],
    ">":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0],[0,1,1,0],[0,0,0,1],[0,1,1,0],[1,0,0,0]],
    "&":[[0,1,1,1,0,0,0],[1,0,0,0,1,0,0],[1,0,0,0,1,0,0],[0,1,1,1,0,0,0],[1,1,0,1,1,0,0],[1,0,0,0,1,0,1],[1,1,0,0,0,1,0],[0,1,1,1,1,0,1]],
    "~":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,1],[1,0,0,1,0]],
    "#":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,1,0],[1,1,1,1,1],[0,1,0,1,0],[1,1,1,1,1],[0,1,0,1,0]],
    "@":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,0,0,0,0,1],[1,0,0,1,1,0,1],[1,0,1,0,0,1,1],[1,0,1,0,0,1,1],[1,0,0,1,1,0,0],[0,1,0,0,0,0,1],[0,0,1,1,1,1,0]],
    "|":[[1],[1],[1],[1],[1],[1],[1],[1]],
    "_":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1]],
    "°":[[1,1,1],[1,0,1],[1,1,1]],
    "€":[[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,0,0,0,1],[0,1,1,1,0,0],[1,0,0,0,0,0],[0,1,1,1,0,0],[0,1,0,0,0,1],[0,0,1,1,1,0]],
    "$":[[0,0,1,0,0],[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,0],[0,1,1,1,0],[0,0,1,0,1],[1,0,1,0,1],[0,1,1,1,0],[0,0,1,0,0]],
}

keys_to_representation = {
    pyxel.KEY_SPACE: "space",
    pyxel.KEY_A: "a",
    pyxel.KEY_B: "b",
    pyxel.KEY_C: "c",
    pyxel.KEY_D: "d",
    pyxel.KEY_E: "e",
    pyxel.KEY_F: "f",
    pyxel.KEY_G: "g",
    pyxel.KEY_H: "h",
    pyxel.KEY_I: "i",
    pyxel.KEY_J: "j",
    pyxel.KEY_K: "k",
    pyxel.KEY_L: "l",
    pyxel.KEY_M: "m",
    pyxel.KEY_N: "n",
    pyxel.KEY_O: "o",
    pyxel.KEY_P: "p",
    pyxel.KEY_Q: "q",
    pyxel.KEY_R: "r",
    pyxel.KEY_S: "s",
    pyxel.KEY_T: "t",
    pyxel.KEY_U: "u",
    pyxel.KEY_V: "v",
    pyxel.KEY_W: "w",
    pyxel.KEY_X: "x",
    pyxel.KEY_Y: "y",
    pyxel.KEY_Z: "z",
    pyxel.KEY_0: "0",
    pyxel.KEY_1: "1",
    pyxel.KEY_2: "2",
    pyxel.KEY_3: "3",
    pyxel.KEY_4: "4",
    pyxel.KEY_5: "5",
    pyxel.KEY_6: "6",
    pyxel.KEY_7: "7",
    pyxel.KEY_8: "8",
    pyxel.KEY_9: "9",
    pyxel.KEY_MINUS: "-",
    pyxel.KEY_EQUALS: "=",
    pyxel.KEY_LEFTBRACKET: "[",
    pyxel.KEY_RIGHTBRACKET: "]",
    pyxel.KEY_SEMICOLON: ";",
    pyxel.KEY_COMMA: ",",
    pyxel.KEY_PERIOD: ".",
    pyxel.KEY_SLASH: "/",
    pyxel.KEY_BACKSPACE: "backspace",
    pyxel.KEY_TAB: "tab",
    pyxel.KEY_RETURN: "enter",
    pyxel.KEY_SHIFT: "shift",
    pyxel.KEY_LCTRL: "ctrl",
    pyxel.KEY_ALT: "alt",
    pyxel.KEY_ESCAPE: "escape",
    pyxel.KEY_UP: "up",
    pyxel.KEY_DOWN: "down",
    pyxel.KEY_LEFT: "left",
    pyxel.KEY_RIGHT: "right"
}

#? -------------------- TRANSITIONS -------------------- ?#

class Transition:

    def __init__(self, new_scene_id:int, speed:int, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None, load_pyxres:bool=False):
        self.new_scene_id = new_scene_id
        self.speed = speed
        self.transition_color = transition_color
        self.new_camera_x = new_camera_x
        self.new_camera_y = new_camera_y
        self.action = action
        self.load_pyxres = load_pyxres
        self.direction = 1

class TransitionDither(Transition):

    def __init__(self, new_scene_id:int, duration:float, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None, load_pyxres:bool=False, fps:int=60):
        super().__init__(new_scene_id, 1 / (duration / 2 * fps), transition_color, new_camera_x, new_camera_y, action, load_pyxres)
        self.dither = 0

    def update(self, pyxel_manager):
        self.dither += self.speed * self.direction

        if self.dither > 1 and self.direction == 1:
            self.direction = -1
            pyxel_manager.change_scene(self.new_scene_id, self.new_camera_x, self.new_camera_y, self.action, self.load_pyxres)
        if self.dither < 0 and self.direction == -1:
            pyxel_manager.finish_transition()
            return

    def draw(self, pyxel_manager):
        pyxel.dither(self.dither)
        pyxel.rect(pyxel_manager.camera_x, pyxel_manager.camera_y, pyxel.width, pyxel.height, self.transition_color)
        pyxel.dither(1)  

class TransitionDiagonal(Transition):
    
    def __init__(self, new_scene_id:int, duration:float, transition_color:int, dir:int=TOP_LEFT, new_camera_x:int=0, new_camera_y:int=0, action=None, load_pyxres:bool=False, fps:int=60):
        self.max_pos = pyxel.width + pyxel.height
        super().__init__(new_scene_id,  self.max_pos / (duration / 2 * fps), transition_color, new_camera_x, new_camera_y, action, load_pyxres)
        self.start = self.end = 0
        self.dir = dir

    def update(self, pyxel_manager):
        if self.direction == 1:   self.end += self.speed
        else:                     self.start += self.speed

        if self.end > self.max_pos and self.direction == 1:
            self.direction = -1
            pyxel_manager.change_scene(self.new_scene_id, self.new_camera_x, self.new_camera_y, self.action, self.load_pyxres)
        if self.start > self.max_pos and self.direction == -1:
            pyxel_manager.finish_transition()
            return

    def draw(self, pyxel_manager):
        for i in range(round(self.start), round(self.end) + 1):
            if self.dir == TOP_LEFT:
                pyxel.line(pyxel_manager.camera_x, pyxel_manager.camera_y + i, pyxel_manager.camera_x + i, pyxel_manager.camera_y, self.transition_color)
            elif self.dir == TOP_RIGHT:
                pyxel.line(pyxel_manager.camera_x + pyxel.width, pyxel_manager.camera_y + i, pyxel_manager.camera_x + pyxel.width - i, pyxel_manager.camera_y, self.transition_color)
            elif self.dir == BOTTOM_LEFT:
                pyxel.line(pyxel_manager.camera_x, pyxel_manager.camera_y + pyxel.height - i, pyxel_manager.camera_x + i, pyxel_manager.camera_y + pyxel.height, self.transition_color)
            else:
                pyxel.line(pyxel_manager.camera_x + pyxel.width, pyxel_manager.camera_y + pyxel.height - i, pyxel_manager.camera_x + pyxel.width - i, pyxel_manager.camera_y + pyxel.height, self.transition_color)

#? -------------------- SCENE MANAGER -------------------- ?#

class PyxelManager:

    def __init__(self, screen_size:tuple, scenes:list, default_scene_id:int=0, fps:int=60, fullscreen:bool=False, mouse:bool=False, pyxres_path:str=None, 
                 palette:list=DEFAULT_PYXEL_COLORS, screen_mode:int=0, quit_key:int=pyxel.KEY_ESCAPE, camera_x:int=0, camera_y:int=0):
        
        self.__scenes_dict = {}
        for scene in scenes:
            if scene.pyxres_path is None:   scene.pyxres_path = pyxres_path
            if scene.palette is None:       scene.palette = palette
            if scene.screen_size is None:   scene.screen_size = screen_size
            if scene.screen_mode is None:   scene.screen_mode = screen_mode
            self.__scenes_dict[scene.id] = scene
        self.__current_scene = self.__scenes_dict[default_scene_id]
        self.__current_scene_id = default_scene_id
        self.__transition = None

        self.__cam_x = self.__cam_tx = camera_x
        self.__cam_y = self.__cam_ty = camera_y
        self.__cam_tween_x = self.__cam_tween_y = Tween(0, 0, 0)
        self.__cam_interpolation = 0.1
        self.__cam_bounds = (-float("inf"), -float("inf"), float("inf"), float("inf"))
        self.__shake_amount = 0
        self.__shake_decay = 0

        self.__fps = fps

        pyxel.init(*screen_size, fps=fps, quit_key=quit_key)
        pyxel.fullscreen(fullscreen)
        pyxel.mouse(mouse)

        self.load_current_scene()

    @property
    def camera_x(self)-> int|float:
        return self.__cam_x
    
    @property
    def camera_y(self)-> int|float:
        return self.__cam_y

    @property
    def mouse_x(self)-> int:
        return self.__cam_x + pyxel.mouse_x
    
    @property
    def mouse_y(self)-> int:
        return self.__cam_y + pyxel.mouse_y
    
    @property
    def current_scene_id(self)-> int:
        return self.__current_scene_id

    def set_camera(self, new_camera_x:int, new_camera_y:int):
        self.__cam_x = self.__cam_tx = max(self.__cam_bounds[0], min(new_camera_x, self.__cam_bounds[2] - pyxel.width))
        self.__cam_y = self.__cam_ty = max(self.__cam_bounds[1], min(new_camera_y, self.__cam_bounds[3] - pyxel.height))

    def move_camera(self, new_camera_x:int, new_camera_y:int, interpolation:float=0.1):
        self.__cam_tx = max(self.__cam_bounds[0], min(new_camera_x, self.__cam_bounds[2] - pyxel.width))
        self.__cam_ty = max(self.__cam_bounds[1], min(new_camera_y, self.__cam_bounds[3] - pyxel.height))
        self.__cam_interpolation = interpolation

    def move_camera_tween(self, new_camera_x:int, new_camera_y:int, duration:float, easing_function):
        if not self.__cam_tween_x.active and not self.__cam_tween_y.active:
            tx = max(self.__cam_bounds[0], min(new_camera_x, self.__cam_bounds[2] - pyxel.width))
            ty = max(self.__cam_bounds[1], min(new_camera_y, self.__cam_bounds[3] - pyxel.height))
            self.__cam_tween_x = Tween(self.__cam_x, tx, duration, True, easing_function, self.__fps)
            self.__cam_tween_y = Tween(self.__cam_y, ty, duration, True, easing_function, self.__fps)

    def set_camera_bounds(self, min_x:int, min_y:int, max_x:int, max_y:int):
        self.__cam_bounds = (min_x, min_y, max_x, max_y)
        self.__cam_tx = max(self.__cam_bounds[0], min(self.__cam_tx, self.__cam_bounds[2] - pyxel.width))
        self.__cam_ty = max(self.__cam_bounds[1], min(self.__cam_ty, self.__cam_bounds[3] - pyxel.height))
        self.__cam_x = max(self.__cam_bounds[0], min(self.__cam_x, self.__cam_bounds[2] - pyxel.width))
        self.__cam_y = max(self.__cam_bounds[1], min(self.__cam_y, self.__cam_bounds[3] - pyxel.height))

    def shake_camera(self, amount:int, decay:float):
        self.__shake_amount = amount
        self.__shake_decay = decay

    def load_current_scene(self, load_pyxres:bool=True):
        pyxel.resize(*self.__current_scene.screen_size)
        if self.__current_scene.pyxres_path and load_pyxres:
            pyxel.load(self.__current_scene.pyxres_path)
        pyxel.colors.clear()
        pyxel.colors.extend(self.__current_scene.palette)
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)

    def change_scene(self, new_scene_id:int, new_camera_x:int=0, new_camera_y:int=0, action=None, load_pyxres:bool=False):
        self.set_camera(new_camera_x, new_camera_y)

        self.__current_scene = self.__scenes_dict[new_scene_id]
        self.__current_scene_id = new_scene_id
        if action:
            action()

        self.load_current_scene(load_pyxres)

    def change_scene_transition(self, transition:Transition):
        self.__transition = transition

    def finish_transition(self):
        self.__transition = None

    def apply_palette_effect(self, effect_function, **kwargs):
        pyxel.colors.clear()
        pyxel.colors.extend(effect_function(self.__current_scene.palette, **kwargs))

    def reset_palette(self):
        pyxel.colors.clear()
        pyxel.colors.extend(self.__current_scene.palette)

    def update(self):
        if self.__transition:
            self.__transition.update(self)

        if self.__cam_tween_x.active or self.__cam_tween_y.active:
            self.__cam_x = self.__cam_tx = self.__cam_tween_x.update()
            self.__cam_y = self.__cam_ty = self.__cam_tween_y.update()
        else:
            self.__cam_x += (self.__cam_tx - self.__cam_x) * self.__cam_interpolation
            self.__cam_y += (self.__cam_ty - self.__cam_y) * self.__cam_interpolation

        if self.__shake_amount > 0:
            a = self.__shake_amount
            pyxel.camera(self.__cam_x + random.uniform(-a, a), self.__cam_y + random.uniform(-a, a))
            self.__shake_amount = max(0, self.__shake_amount - self.__shake_decay)
        else:
            pyxel.camera(self.__cam_x, self.__cam_y)

        if not self.__transition:
            self.__current_scene.update()

    def draw(self):
        self.__current_scene.draw()
        if self.__transition:
            self.__transition.draw(self)

    def run(self):
        pyxel.run(self.update, self.draw)

class Scene:

    def __init__(self, id:int|float, title:str, update, draw, *, pyxres_path:str=None, palette:list=None, screen_size:tuple=None, screen_mode:int=None):
        self.id = id
        self.title = title
        self.update = update
        self.draw = draw
        self.pyxres_path = pyxres_path
        self.palette = palette
        self.screen_size = screen_size
        self.screen_mode = screen_mode

#? -------------------- TWEEN -------------------- ?#

class Tween:

    def __init__(self, start:int, end:int, duration:float, autostart:bool=False, easing_function=None, fps:int=60):
        self.start = start
        self.end = end
        self.duration = duration
        self.ease = easing_function or (lambda t: t)

        self.elapsed = 0
        self.dt = 1 / fps
        self.active = autostart
        self.value = start

    def update(self)-> float:
        if not self.active:
            return self.value
        
        self.elapsed += self.dt
        t = self.ease(min(self.elapsed / self.duration, 1.0))
        self.value = self.start + (self.end - self.start) * t

        if self.elapsed >= self.duration:
            self.active = False

        return self.value
    
#? -------------------- DIALOG -------------------- ?#

class Dialog:

    def __init__(self, lines:list, background_color:int, names_colors:list|int, text_colors:list|int, border:bool=False, border_color:int=0, sound:bool=False, channel:int=0, sound_number:int=0)-> None:
        self.lines = lines
        self.background_color = background_color
        self.names_colors = names_colors
        self.text_colors = text_colors
        self.border = border
        self.border_color = border_color
        self.sound = sound
        self.channel = channel
        self.sound_number = sound_number

class DialogManager:

    def __init__(self, relative_start_x:int, relative_start_y:int, relative_end_x:int, relative_end_y:int, width:int, height:int, char_speed:int=3)-> None:
        self.__start_x = relative_start_x
        self.__start_y = relative_start_y
        self.__end_x = relative_end_x
        self.__end_y = relative_end_y
        self.__x = relative_start_x
        self.__y = relative_start_y
        self.__width = width
        self.__height = height
        self.__background_color = 0
        self.__names_colors = 0
        self.__text_colors = []
        self.__border = False
        self.__border_color = 0

        self.__started = False
        self.__open = False
        self.__dialog = None

        self.__current_line = 0
        self.__char_index = 0
        self.__char_speed = char_speed
        self.__frame_count = 0

    def is_dialog(self)-> bool:
        return self.__started

    def start_dialog(self, dialog:Dialog)-> None:
        if not self.__started:
            self.__background_color = dialog.background_color
            self.__names_colors = dialog.names_colors
            self.__text_colors = dialog.text_colors
            self.__border = dialog.border
            self.__border_color = dialog.border_color

            self.__started = True
            self.__dialog = dialog
            self.__current_line = 0
            self.__char_index = 0
            self.__frame_count = 0

    def stop_dialog(self)-> None:
        self.__started = False
        self.__open = False
        self.__dialog = None

    def update(self)-> None:
        if self.__started:
            self.__x = lerp(self.__x, self.__end_x, 0.15)
            self.__y = lerp(self.__y, self.__end_y, 0.15)

            if abs(self.__x - self.__end_x) < 1 and abs(self.__y - self.__end_y) < 1:
                self.__open = True

            if self.__open:
                if self.__char_index < len(self.__dialog.lines[self.__current_line][1]):
                    if pyxel.btnp(pyxel.KEY_E) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
                        self.__char_index = len(self.__dialog.lines[self.__current_line][1])
                        if self.__dialog.sound:
                            pyxel.play(self.__dialog.channel, self.__dialog.sound_number)
                    self.__frame_count += 1
                    if self.__frame_count % self.__char_speed == 0:
                        if self.__dialog.sound:
                            pyxel.play(self.__dialog.channel, self.__dialog.sound_number)
                        self.__char_index += 1
                else:
                    if pyxel.btnp(pyxel.KEY_E) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
                        if self.__current_line < len(self.__dialog.lines) - 1:
                            self.__current_line += 1
                            self.__char_index = 0
                            self.__frame_count = 0
                        else:
                            self.__started = False
                            self.__open = False

        else:
            self.__x = lerp(self.__x, self.__start_x, 0.15)
            self.__y = lerp(self.__y, self.__start_y, 0.15)

    def draw(self, camera_x:int=0, camera_y:int=0)-> None:
        if abs(self.__x - self.__start_x) < 1 and abs(self.__y - self.__start_y) < 1:
            return

        pyxel.rect(camera_x + self.__x, camera_y + self.__y, self.__width, self.__height, self.__background_color)
        if self.__border:
            pyxel.rectb(camera_x + self.__x, camera_y + self.__y, self.__width, self.__height, self.__border_color)
        if self.__open:
            Text(self.__dialog.lines[self.__current_line][0], camera_x + self.__x + 2, camera_y + self.__y + 2, self.__names_colors, FONT_DEFAULT).draw()
        if self.__dialog:
            visible_text = self.__dialog.lines[self.__current_line][1][:self.__char_index]
            Text(visible_text, camera_x + self.__x + 2, camera_y + self.__y + 14, self.__text_colors, FONT_DEFAULT).draw()

def lerp(start:int|float, end:int|float, speed:float=0.1)-> int|float:
    return start + (end - start) * speed

#? -------------------- PARTICLES -------------------- ?#

class Particle:

    def __init__(self, x:int, y:int, lifespan:int, speed:int, target:tuple, friction:tuple=(0, 0), acceleration:tuple=(0, 0), dither_duration:int=0, zorder:int=0):
        self.x, self.y = x, y
        self.lifespan = lifespan
        self.fx, self.fy = friction
        self.ax, self.ay = acceleration
        self.dither = 1
        self.dither_duration = max(dither_duration, 0)
        self.zorder = zorder

        dx = target[0] - x
        dy = target[1] - y
        mag = (dx ** 2 + dy ** 2) ** 0.5
        self.vx = dx / mag * speed if mag != 0 else 0
        self.vy = dy / mag * speed if mag != 0 else 0

    def update(self):
        self.lifespan -= 1

        self.vx += self.fx + self.ax
        self.vy += self.fy + self.ay
        self.x += self.vx
        self.y += self.vy

        if self.lifespan <= self.dither_duration and self.dither_duration:
            self.dither -= 1 / self.dither_duration

class ShapeParticle(Particle):

    def __init__(self, x:int, y:int, w:int, h:int, colors:int|list, lifespan:int, speed:int, target:tuple, friction:tuple=(0, 0), acceleration:tuple=(0, 0), grow:tuple=(0, 0), dither_duration:int=0, hollow:bool=False, zorder:int=0):
        super().__init__(x, y, lifespan, speed, target, friction, acceleration, dither_duration, zorder)
        self.w, self.h = w, h
        self.colors = [colors] if isinstance(colors, int) else colors
        self.colors_length = len(self.colors)
        self.current_color = 0
        self.lifespan = round(lifespan / self.colors_length) * self.colors_length
        self.initial_lifespan = self.lifespan
        self.gw, self.gh = grow
        self.hollow = hollow

    def update(self):
        super().update()

        self.w += self.gw
        self.h += self.gh

        if self.w < 1 or self.h < 1:
            self.lifespan = 0

        if self.lifespan > 0 and self.lifespan % (self.initial_lifespan / self.colors_length) == 0:
            self.current_color = (self.current_color + 1) % self.colors_length

class OvalParticle(ShapeParticle):

    def __init__(self, x:int, y:int, w:int, h:int, colors:int|list, lifespan:int, speed:int, target:tuple, friction:tuple=(0, 0), acceleration:tuple=(0, 0), grow:tuple=(0, 0), dither_duration:int=0, hollow:bool=False, zorder:int=0):
        super().__init__(x, y, w, h, colors, lifespan, speed, target, friction, acceleration, grow, dither_duration, hollow, zorder)

    def draw(self):
        pyxel.dither(self.dither)
        if self.hollow:    pyxel.ellib(self.x, self.y, self.w, self.h, self.colors[self.current_color])
        else:              pyxel.elli(self.x, self.y, self.w, self.h, self.colors[self.current_color])
        pyxel.dither(1)

class LineParticle(ShapeParticle):

    def __init__(self, x:int, y:int, lenght:int, colors:int|list, lifespan:int, speed:int, target:tuple, friction:tuple=(0, 0), acceleration:tuple=(0, 0), grow:int=0, dither_duration:int=0, zorder:int=0):
        super().__init__(x, y, 1, 1, colors, lifespan, speed, target, friction, acceleration, (1, 1), dither_duration, False, zorder)
        self.grow = grow
        self.lenght = lenght

    def update(self):
        super().update()

        self.lenght += self.grow

    def draw(self):
        vx2 = self.vx + self.fx + self.ax
        vy2 = self.vy + self.fy + self.ay
        mag = (vx2 ** 2 + vy2 ** 2) ** 0.5
        x2 = self.x + (vx2 / mag * self.lenght) if mag != 0 else self.x
        y2 = self.y + (vy2 / mag * self.lenght) if mag != 0 else self.y

        pyxel.dither(self.dither)
        pyxel.line(self.x, self.y, x2, y2, self.colors[self.current_color])
        pyxel.dither(1)

class ParticleManager:

    def __init__(self):
        self.particles = []

    def reset(self):
        self.particles = []

    def add_particle(self, new_particle):
        self.particles.append(new_particle)

    def update(self):
        for particle in self.particles:
            particle.update()

        self.particles = [particle for particle in self.particles if particle.lifespan]
        self.particles = sorted(self.particles, key=lambda particle: particle.zorder)

    def draw(self):
        for particle in self.particles:
            particle.draw()

#? -------------------- SPRITES -------------------- ?#

class Sprite:

    def __init__(self, img:int, u:int, v:int, w:int, h:int, colkey:int=None):
        self.img = img
        self.u, self.v = u, v
        self.w, self.h = w, h
        self.colkey = 0 if colkey == 0 else colkey
        self.flip_horizontal = False
        self.flip_vertical = False

class Animation:

    def __init__(self, sprite:Sprite, total_frames:int=1, frame_duration:int=20, loop:bool=True):
        self.sprite = sprite
        self.total_frames = total_frames
        self.frame_duration = frame_duration
        self.loop = loop
        self.__start_frame = pyxel.frame_count
        self.current_frame = 0
        self.__is_finished = False

    def is_finished(self)-> bool:
        return self.__is_finished and not self.loop
    
    def is_looped(self)-> bool:
        return self.loop
    
    def reset(self):
        self.__start_frame = pyxel.frame_count
        self.current_frame = 0
        self.__is_finished = False

    def update(self):
        if self.is_finished():
            return
        
        if pyxel.frame_count - self.__start_frame >= self.frame_duration:
            self.__start_frame = pyxel.frame_count
            self.current_frame += 1
            if self.current_frame >= self.total_frames:
                if self.loop:
                    self.current_frame = 0
                else:
                    self.__is_finished = True
                    self.current_frame = self.total_frames - 1

    def draw(self, x:int, y:int, anchor:int=TOP_LEFT):
        x, y = get_anchored_position(x, y, self.sprite.w, self.sprite.h, anchor)

        w = -self.sprite.w if self.sprite.flip_horizontal else self.sprite.w
        h = -self.sprite.h if self.sprite.flip_vertical else self.sprite.h
        pyxel.blt(x, y, self.sprite.img, self.sprite.u + self.current_frame * abs(self.sprite.w), self.sprite.v, w, h, self.sprite.colkey)

#? -------------------- GUIs -------------------- ?#

class Text:
    
    def __init__(self, text:str, x:int, y:int, text_colors:int|list, font:dict, font_size:int=1, anchor=TOP_LEFT, color=(HORIZONTAL, NORMAL_COLOR_MODE, 20), wave=None, shadow=None, outline_color=None, relative:bool=True):
        """
        color = (color direction, color mode, color frames)  
        wave = (amplitude, speed, character spacing)  
        shadow = (color, offset x, offset y)
        """
        self.text = text
        self.x, self.y = x, y
        self.text_colors = text_colors
        self.font_size = font_size
        self.font = font
        self.anchor = anchor
        self.color_dir = color[0]
        self.color_mode = color[1]
        self.color_frames = color[2]
        self.wave = wave
        self.shadow = shadow
        self.outline_color = outline_color
        self.relative = relative

        self.initialize()

    def initialize(self):
        self.y = get_anchored_position_y(self.y, text_height(self.text, self.font, self.font_size), self.anchor)
        self.text_colors = [self.text_colors] if isinstance(self.text_colors, int) else self.text_colors
        self.o_text_colors = [x for x in self.text_colors]
        self.__last_change_color_time = pyxel.frame_count

    def _draw_line(self, text:str, y:int, camera_x:int=0, camera_y:int=0):
        x = get_anchored_position_x(self.x, text_width(text, self.font, self.font_size), self.anchor)

        if self.relative:
            x += camera_x
            y += camera_y

        if self.outline_color != None:
            Text(text, x + self.font_size, y, self.outline_color, self.font, self.font_size, wave=self.wave).draw()
            Text(text, x - self.font_size, y, self.outline_color, self.font, self.font_size, wave=self.wave).draw()
            Text(text, x, y + self.font_size, self.outline_color, self.font, self.font_size, wave=self.wave).draw()
            Text(text, x, y - self.font_size, self.outline_color, self.font, self.font_size, wave=self.wave).draw()
        elif self.shadow:
            Text(text, x + self.shadow[1] * self.font_size, y + self.shadow[2] * self.font_size, self.shadow[0], self.font, self.font_size, wave=self.wave).draw()

        for char_index, char in enumerate(text):
            char_matrix = self.font[char]
            char_width = len(char_matrix[0]) * self.font_size
            char_height = len(char_matrix)
            char_y = y + math.cos(pyxel.frame_count / self.wave[1] + char_index * self.wave[2]) * self.wave[0] if self.wave else y
            
            for row_index, row in enumerate(char_matrix):
                for col_index, pixel in enumerate(row):
                    if pixel:

                        if self.color_dir == HORIZONTAL:
                            c = self.text_colors[char_index % len(self.text_colors)]
                        elif self.color_dir == VERTICAL:
                            c = self.text_colors[int(row_index * len(self.text_colors) / char_height)]

                        pyxel.rect(x + col_index * self.font_size, char_y + row_index * self.font_size, self.font_size, self.font_size, c)
            
            x += char_width + self.font_size

    def update(self):
        if self.color_mode != NORMAL_COLOR_MODE and pyxel.frame_count - self.__last_change_color_time >= self.color_frames:
            if self.color_mode == ROTATING_COLOR_MODE:
                self.__last_change_color_time = pyxel.frame_count
                self.text_colors = [self.text_colors[-1]] + self.text_colors[:-1]
            elif self.color_mode == RANDOM_COLOR_MODE:
                self.__last_change_color_time = pyxel.frame_count
                self.text_colors = [random.choice(self.o_text_colors) for _ in range(len(self.text))]

    def draw(self, camera_x:int=0, camera_y:int=0):
        if "\n" in self.text:
            lines = self.text.split("\n")
            y = self.y
            for line in lines:
                self._draw_line(line, y, camera_x, camera_y)
                y += text_height(line, self.font, self.font_size) + self.font_size
        else:
            self._draw_line(self.text, self.y, camera_x, camera_y)

#? -------------------- GUI FUNCTIONS -------------------- ?#

def text_size(text:str, font:dict, font_size:int=1)-> tuple:
    if not text:    return 0, 0
    lines = text.split("\n")

    width = max(sum(len(font[c][0]) for c in line) + len(line) - 1 for line in lines)

    height = sum(max(len(font[c]) for c in line) for line in lines) + len(lines) - 1

    return width * font_size, height * font_size

def text_width(text:str, font:dict, font_size:int=1)-> tuple:
    if not text:    return 0
    lines = text.split("\n")

    width = max(sum(len(font[c][0]) for c in line) + len(line) - 1 for line in lines)

    return width * font_size

def text_height(text:str, font:dict, font_size:int=1)-> tuple:
    if not text:    return 0
    lines = text.split("\n")

    height = sum(max(len(font[c]) for c in line) for line in lines if line) + len(lines) - 1

    return height * font_size

def wrap_text_width(text:str, max_width:int, font_size:int, font:dict)-> str:
    words = text.split(" ")
    output_lines = []
    current_line = ""

    for word in words:
        test_line = word if current_line == "" else current_line + " " + word
        w, _ = text_size(test_line, font, font_size)

        if w <= max_width:
            current_line = test_line
        else:
            output_lines.append(current_line)
            current_line = word

    output_lines.append(current_line)
    return "\n".join(output_lines)

#? -------------------- POSITION -------------------- ?#

def get_anchored_position(x:int, y:int, width:int, height:int, anchor:int)-> tuple:
    if anchor in [TOP_RIGHT, BOTTOM_RIGHT, RIGHT]:
        x -= width
    if anchor in [BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM]:
        y -= height
    if anchor in [TOP, BOTTOM, CENTER]:
        x -= width // 2
    if anchor in [LEFT, RIGHT, CENTER]:
        y -= height // 2
        
    return x, y

def get_anchored_position_x(x:int, width:int, anchor:int)-> int:
    if anchor in [TOP_RIGHT, BOTTOM_RIGHT, RIGHT]:
        x -= width
    if anchor in [TOP, BOTTOM, CENTER]:
        x -= width // 2

    return x

def get_anchored_position_y(y:int, height:int, anchor:int)-> int:
    if anchor in [BOTTOM_LEFT, BOTTOM_RIGHT, BOTTOM]:
        y -= height
    if anchor in [LEFT, RIGHT, CENTER]:
        y -= height // 2

    return y

#? -------------------- EASING FUNCTIONS -------------------- ?#
    
def linear(t):
    return t

#? -------------------- COLLISIONS -------------------- ?#

def collision_rect_rect(x1:int, y1:int, w1:int, h1:int, x2:int, y2:int, w2:int, h2:int)-> bool:
    return not (x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)

#? -------------------- MOTIONS -------------------- ?#

def wave_motion(value:float, amplitude:float, duration:float, time:int, fps:int=60)-> float:
    return value + math.sin((2 * math.pi) / (duration * fps) * time) * amplitude

#? -------------------- OTHER -------------------- ?#

def zone(x1:int, y1:int, x2:int, y2:int)-> list:
    return [(x,y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]