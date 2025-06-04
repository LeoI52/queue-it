"""
@author : Léo IMBERT & Eddy MONGIN
@created : 14/05/2025
@updated : 17/05/2025
"""

import random
import pyxel
import math
import time

DEFAULT_PYXEL_COLORS = [0x000000, 0x2B335F, 0x7E2072, 0x19959C, 
                        0x8B4852, 0x395C98, 0xA9C1FF, 0xEEEEEE, 
                        0xD4186C, 0xD38441, 0xE9C35B, 0x70C6A9, 
                        0x7696DE, 0xA3A3A3, 0xFF9798, 0xEDC7B0]

characters_matrices = {
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
    "g":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "h":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,1,1,0],[0,1,1,1,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[1,1,1,0,0,1,1]],
    "i":[[0,0,0,0],[0,1,1,0],[0,0,0,0],[1,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    "j":[[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,0,0],[0,0,0,1,1,1],[0,0,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "k":[[0,0,0,0,0,0,0],[1,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,1,1],[0,1,1,0,1,1,0],[0,1,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,1,0,0,1,1]],
    "l":[[0,0,0,0],[1,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,1,1,1]],
    "m":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,0,1,1,0],[1,1,1,1,1,1,1],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,0,0,0,1,1]],
    "n":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1]],
    "o":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0]],
    "p":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,0,0,1,1],[0,1,1,0,0,1,1],[0,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "q":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,1,1,0,1,1],[1,1,0,0,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,1,1,0],[0,0,0,0,1,1,0],[0,0,0,1,1,1,1]],
    "r":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,1,1,1,0],[0,1,1,1,0,1,1],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[1,1,1,1,0,0,0]],
    "s":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,0,0],[0,1,1,1,1,0],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "t":[[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[1,1,1,1,1,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[0,1,1,0,1,1],[0,0,1,1,1,0]],
    "u":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1]],
    "v":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,1,1,0,0]],
    "w":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[1,1,0,1,0,1,1],[1,1,0,1,0,1,1],[1,1,1,1,1,1,1],[0,1,1,0,1,1,0]],
    "x":[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,1,0,0,0,1,1],[0,1,1,0,1,1,0],[0,0,1,1,1,0,0],[0,1,1,0,1,1,0],[1,1,0,0,0,1,1]],
    "y":[[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,1,1],[1,1,0,0,1,1],[1,1,0,0,1,1],[0,1,1,1,1,1],[0,0,0,0,1,1],[1,1,1,1,1,0]],
    "z":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[1,0,0,1,1,0],[0,0,1,1,0,0],[0,1,1,0,0,1],[1,1,1,1,1,1]],
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
    "?":[[0,0,0,0],[1,1,1,0],[1,0,1,1],[0,0,1,1],[0,1,1,0],[0,0,0,0],[0,1,1,0],[0,1,1,0]],
    ",":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[1,1,0,0]],
    ".":[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[1,1,0],[1,1,0]],
    ";":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0],[0,1,1,0],[0,1,1,0],[1,1,0,0]],
    "/":[[0,0,0,0,0,0],[0,0,0,0,1,1],[0,0,0,0,1,0],[0,0,0,1,1,0],[0,0,1,1,0,0],[0,0,1,0,0,0],[0,1,1,0,0,0],[1,1,0,0,0,0]],
    ":":[[0,0],[0,0],[1,1],[1,1],[0,0],[1,1],[1,1],[0,0]],
    "!":[[0,0],[1,1],[1,1],[1,1],[1,1],[0,0],[1,1],[1,1]],
    "&":[[0,1,1,1,0,0,0],[1,0,0,0,1,0,0],[1,0,0,0,1,0,0],[0,1,1,1,0,0,0],[1,1,0,1,1,0,0],[1,0,0,0,1,0,1],[1,1,0,0,0,1,0],[0,1,1,1,1,0,1]],
    "é":[[0,0,0,1,1,0],[0,1,1,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "~":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,1],[1,0,0,1,0]],
    '"':[[0,0,0,0],[0,1,0,1],[0,1,0,1],[1,0,1,0],[1,0,1,0]],
    "#":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,1,0,1,0],[1,1,1,1,1],[0,1,0,1,0],[1,1,1,1,1],[0,1,0,1,0]],
    "'":[[0,0,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,1,1,0,0],[0,1,1,0,0]],
    "{":[[0,0,0],[0,0,1],[0,1,0],[0,1,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1]],
    "(":[[0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,0,0],[1,0,0],[0,1,0],[0,0,1]],
    "[":[[0,0,0],[1,1,1],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,1,1]],
    "-":[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1],[1,1,1,1],[0,0,0,0],[0,0,0,0]],
    "|":[[1],[1],[1],[1],[1],[1],[1],[1]],
    "è":[[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,1,1,1,1],[1,1,0,0,0,0],[0,1,1,1,1,0]],
    "_":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1]],
    "ç":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,1,1,1,0],[1,1,0,0,1,1],[1,1,0,0,0,0],[1,1,0,0,1,1],[0,1,1,1,1,0],[0,0,0,1,0,0],[0,0,1,0,0,0]],
    "à":[[0,0,1,1,0,0,0],[0,0,0,0,1,1,0],[0,0,0,0,0,0,0],[0,1,1,1,1,0,0],[0,0,0,0,1,1,0],[0,1,1,1,1,1,0],[1,1,0,0,1,1,0],[0,1,1,1,0,1,1]],
    "@":[[0,0,0,0,0,0,0],[0,0,1,1,1,1,0],[0,1,0,0,0,0,1],[1,0,0,1,1,0,1],[1,0,1,0,0,1,1],[1,0,1,0,0,1,1],[1,0,0,1,1,0,0],[0,1,0,0,0,0,1],[0,0,1,1,1,1,0]],
    "°":[[1,1,1],[1,0,1],[1,1,1]],
    ")":[[0,0,0],[1,0,0],[0,1,0],[0,0,1],[0,0,1],[0,0,1],[0,1,0],[1,0,0]],
    "]":[[0,0,0],[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[1,1,1]],
    "+":[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0]],
    "=":[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,1,1,1,1],[0,0,0,0,0,0]],
    "}":[[0,0,0],[1,0,0],[0,1,0],[0,1,0],[0,0,1],[0,1,0],[0,1,0],[1,0,0]],
    "*":[[0,0,0],[1,0,1],[0,1,0],[1,0,1]],
    "%":[[0,1,0,0,0,0,0],[1,0,1,0,1,1,0],[0,1,0,0,1,0,0],[0,0,0,1,1,0,0],[0,0,1,1,0,0,0],[0,0,1,0,0,1,0],[0,1,1,0,1,0,1],[1,1,0,0,0,1,0]],
    "€":[[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,0,0,0,1],[0,1,1,1,0,0],[1,0,0,0,0,0],[0,1,1,1,0,0],[0,1,0,0,0,1],[0,0,1,1,1,0]],
    "$":[[0,0,1,0,0],[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,0],[0,1,1,1,0],[0,0,1,0,1],[1,0,1,0,1],[0,1,1,1,0],[0,0,1,0,0]]
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

NORMAL_COLOR_MODE = 0
ROTATING_COLOR_MODE = 1
RANDOM_COLOR_MODE = 2

ANCHOR_TOP_LEFT = 0
ANCHOR_TOP_RIGHT = 1
ANCHOR_BOTTOM_LEFT = 2
ANCHOR_BOTTOM_RIGHT = 3
ANCHOR_LEFT = 4
ANCHOR_RIGHT = 5
ANCHOR_TOP = 6
ANCHOR_BOTTOM = 7
ANCHOR_CENTER = 8


class PyxelManager:

    def __init__(self, window_size:tuple, scenes:list, default_scene_id:int, fps:int=60, fullscreen:bool=False, mouse:bool=False, quit_key:int=pyxel.KEY_ESCAPE, camera_x:int=0, camera_y:int=0)-> None:
        self.__fps = fps
        self.__scenes = scenes
        for scene in self.__scenes:
            if scene.id == default_scene_id:
                self.__current_scene = scene

        self.__camera_x = camera_x
        self.__camera_y = camera_y
        self.__camera_target_x = self.__camera_x
        self.__camera_target_y = self.__camera_y
        self.__shake_amount = 0
        self.__substracting_shake_amount = 0

        self.__debug_mode = False
        self.__debug_color = 7
        self.__start_time = time.time()
        self.__current_fps = self.__fps

        pyxel.init(window_size[0], window_size[1], fps=self.__fps, quit_key=quit_key)
        pyxel.fullscreen(fullscreen)
        pyxel.mouse(mouse)

        if self.__current_scene.pyxres_path:
            pyxel.load(self.__current_scene.pyxres_path)
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)
        pyxel.colors.from_list(self.__current_scene.palette)

    @property
    def camera_x(self)-> int:
        return self.__camera_x
    
    @property
    def camera_y(self)-> int:
        return self.__camera_y
    
    @property
    def mouse_x(self)-> int:
        return self.__camera_x + pyxel.mouse_x
    
    @property
    def mouse_y(self)-> int:
        return self.__camera_y + pyxel.mouse_y

    @property
    def fps(self)-> int:
        return self.__fps

    @property
    def current_fps(self)-> int:
        return self.__current_fps

    def set_camera(self, new_x:int, new_y:int)-> None:
        self.__camera_x = new_x
        self.__camera_y = new_y
        self.__camera_target_x = new_x
        self.__camera_target_y = new_y
        pyxel.camera(self.__camera_x, self.__camera_y)

    def move_camera_to(self, target_x:int, target_y:int)-> None:
        self.__camera_target_x = target_x
        self.__camera_target_y = target_y

    def shake_camera(self, amount:int, substracting_shake_amount:int)-> None:
        self.__substracting_shake_amount = abs(substracting_shake_amount)
        self.__shake_amount = abs(amount)

    def change_scene(self, new_scene_id:int, next_camera_x:int=0, next_camera_y:int=0, action=None)-> None:
        self.set_camera(next_camera_x, next_camera_y)
        for scene in self.__scenes:
            if scene.id == new_scene_id:
                self.__current_scene = scene
        if self.__current_scene.pyxres_path:
            pyxel.load(self.__current_scene.pyxres_path)
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)
        pyxel.colors.from_list(self.__current_scene.palette)
        if action: action()

    def change_scene_outer_circle(self, new_scene_id:int, speed:int, transition_color:int, next_camera_x:int=0, next_camera_y:int=0, action=None)-> None:
        start_end = int(((pyxel.width ** 2 + pyxel.height ** 2) ** 0.5) / 2) + 1
        end = start_end
        while end > 0:
            self.draw()
            for radius in range(start_end, end, -1):
                pyxel.ellib(self.__camera_x + pyxel.width / 2 - radius, self.__camera_y + pyxel.height / 2 - radius, radius * 2, radius * 2, transition_color)
                pyxel.ellib(self.__camera_x + pyxel.width / 2 - radius + 1, self.__camera_y + pyxel.height / 2 - radius, radius * 2, radius * 2, transition_color)
            end -= abs(speed)
            pyxel.flip()

        self.change_scene(new_scene_id, next_camera_x, next_camera_y, action)

        while end < start_end:
            self.draw()
            for radius in range(start_end, end, -1):
                pyxel.ellib(self.__camera_x + pyxel.width / 2 - radius, self.__camera_y + pyxel.height / 2 - radius, radius * 2, radius * 2, transition_color)
                pyxel.ellib(self.__camera_x + pyxel.width / 2 - radius + 1, self.__camera_y + pyxel.height / 2 - radius, radius * 2, radius * 2, transition_color)
            end += abs(speed)
            pyxel.flip()

    def change_scene_dither(self, new_scene_id:int, speed:int, transition_color:int, next_camera_x:int=0, next_camera_y:int=0, action=None)-> None:
        dither = 0
        while dither < 1:
            dither += abs(speed)
            self.draw()
            pyxel.dither(dither)
            pyxel.rect(self.__camera_x, self.__camera_y, pyxel.width, pyxel.height, transition_color)
            pyxel.dither(1)
            pyxel.flip()

        self.change_scene(new_scene_id, next_camera_x, next_camera_y, action)

        while dither > 0:
            dither -= abs(speed)
            self.draw()
            pyxel.dither(dither)
            pyxel.rect(self.__camera_x, self.__camera_y, pyxel.width, pyxel.height, transition_color)
            pyxel.dither(1)
            pyxel.flip()

    def change_palette(self, new_palette:list)-> None:
        pyxel.colors.from_list(new_palette)

    def apply_palette_effect(self, function_effect)-> None:
        pyxel.colors.from_list(function_effect(self.__current_scene.palette))

    def reset_palette(self)-> None:
        pyxel.colors.from_list(self.__current_scene.palette)

    def activate_debug(self, debug_color:int=7, camera_speed:int=2)-> None:
        self.__debug_mode = True
        self.__debug_color = debug_color
        self.__debug_camera_speed = camera_speed

    def deactivate_debug(self)-> None:
        self.__debug_mode = False

    def toogle_debug(self, debug_color:int=7, camera_speed:int=2)-> None:
        self.__debug_mode = not self.__debug_mode
        self.__debug_color = debug_color
        self.__debug_camera_speed = camera_speed

    def update(self)-> None:
        if self.__debug_mode:
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.set_camera(self.__camera_x + self.__debug_camera_speed, self.__camera_y)
            if pyxel.btn(pyxel.KEY_LEFT):
                self.set_camera(self.__camera_x - self.__debug_camera_speed, self.__camera_y)
            if pyxel.btn(pyxel.KEY_UP):
                self.set_camera(self.__camera_x, self.__camera_y - self.__debug_camera_speed)
            if pyxel.btn(pyxel.KEY_DOWN):
                self.set_camera(self.__camera_x, self.__camera_y + self.__debug_camera_speed)

        self.__camera_x += (self.__camera_target_x - self.__camera_x) * 0.1
        self.__camera_y += (self.__camera_target_y - self.__camera_y) * 0.1

        if self.__shake_amount > 0:
            amount = int(self.__shake_amount)
            pyxel.camera(self.__camera_x + random.randint(-amount, amount), self.__camera_y + random.randint(-amount, amount))
            self.__shake_amount -= self.__substracting_shake_amount
        else:
            pyxel.camera(self.__camera_x, self.__camera_y)

        self.__current_scene.update()

    def draw(self)-> None:
        self.__current_scene.draw()
        if self.__debug_mode:
            pyxel.text(self.camera_x + 5, self.camera_y + 5, f"({int(self.mouse_x)},{int(self.mouse_y)})", self.__debug_color)
            pyxel.text(self.camera_x + 5, self.camera_y + 15, f"fps:{self.__current_fps}", self.__debug_color)
        if pyxel.frame_count % self.__fps == 0:
            self.__current_fps = int(1 / (time.time() - self.__start_time))
        self.__start_time = time.time()
    
    def run(self)-> None:
        pyxel.run(self.update, self.draw)

class Scene:

    def __init__(self, id:int, title:str, update, draw, pyxres_path:str=None, palette:list=DEFAULT_PYXEL_COLORS, screen_mode:int=0)-> None:
        self.id = id
        self.title = title
        self.update = update
        self.draw = draw
        self.pyxres_path = pyxres_path
        self.palette = palette
        self.screen_mode = screen_mode

class Sprite:

    def __init__(self, img:int, u:int, v:int, width:int, height:int, colkey:int=None)-> None:
        self.img = img
        self.u = u
        self.v= v
        self.width = width    
        self.height = height
        self.colkey = 0 if colkey == 0 else colkey
        self.flip_horizontal = False
        self.flip_vertical = False

    def flip_h(self) -> None:
        """
        Flip H
        ===
        Enables horizontal flipping of the sprite.
        """
        self.flip_horizontal = True

    def unflip_h(self) -> None:
        """
        Unflip H
        ===
        Disables horizontal flipping of the sprite.
        """
        self.flip_horizontal = False

    def flip_v(self) -> None:
        """
        Flip V
        ===
        Enables vertical flipping of the sprite.
        """
        self.flip_vertical = True

    def unflip_v(self) -> None:
        """
        Unflip V
        ===
        Disables vertical flipping of the sprite.
        """
        self.flip_vertical = False

class Animation:

    def __init__(self, sprite:Sprite, frames:int=1, speed:int=20, loop:bool=True)-> None:
        self.__sprite = sprite
        self.__frames = frames
        self.__speed = speed
        self.__loop = loop
        self.__timer = 0
        self.__current_frame = 0
        self.__is_finished_once  = False

    @property
    def current_frame(self)-> int:
        return self.__current_frame

    def is_finished(self)-> bool:
        return self.__is_finished_once and not self.__loop
    
    def is_looped(self)-> bool:
        return self.__loop

    def reset(self)-> None:
        self.__timer = 0
        self.__current_frame = 0
        self.__is_finished_once = False

    def flip_h(self)-> None:
        self.__sprite.flip_h()

    def unflip_h(self)-> None:
        self.__sprite.unflip_h()

    def flip_v(self)-> None:
        self.__sprite.flip_v()

    def unflip_v(self)-> None:
        self.__sprite.unflip_v()

    def update(self)-> None:
        if self.is_finished():
            return

        self.__timer += 1
        if self.__timer >= self.__speed:
            self.__timer = 0
            self.__current_frame += 1
            if self.__current_frame >= self.__frames:
                if self.__loop:
                    self.__current_frame = 0
                else:
                    self.__is_finished_once = True
                    self.__current_frame = self.__frames - 1

    def draw(self, x:int, y:int, anchor:int=ANCHOR_TOP_LEFT)-> None:
        if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
            x -= self.__sprite.width
        if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
            y -= self.__sprite.height
        if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
            x -= self.__sprite.width // 2
        if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
            y -= self.__sprite.height // 2

        w = -self.__sprite.width if self.__sprite.flip_horizontal else self.__sprite.width
        h = -self.__sprite.height if self.__sprite.flip_vertical else self.__sprite.height
        pyxel.blt(x, y, self.__sprite.img, self.__sprite.u + self.__current_frame * abs(self.__sprite.width), self.__sprite.v, w, h, self.__sprite.colkey)

class Text:

    def __init__(self, text:str, x:int, y:int, text_colors:list|int, font_size:int=0, anchor:int=ANCHOR_TOP_LEFT, color_mode:int=NORMAL_COLOR_MODE, color_speed:int|float=5, relative:bool=False, wavy:bool=False, wave_speed:int|float=10, wave_height:int=3, shadow:bool=False, shadow_color:int=0, shadow_offset:int=1, glitch_intensity:int=0, underline:bool=False, underline_color:int=0, blinking:bool=False, blinking_frames:int=30)-> None:
        self.text = text
        self.x = x
        self.y = y
        self.__font_size = font_size
        self.__text_width, self.__text_height = text_size(text, font_size)
        self.__anchor = anchor
        self.__relative = relative
        self.__wavy = wavy
        self.__wave_speed = wave_speed
        self.__wave_height = wave_height
        self.__shadow = shadow
        self.__shadow_color = shadow_color
        self.__shadow_x = self.x + shadow_offset
        self.__shadow_y = self.y + shadow_offset
        self.__shadow_offset = shadow_offset
        self.__glitch_intensity = glitch_intensity
        self.__underline = underline
        self.__underline_color = underline_color
        self.__blinking = blinking
        self.__blinking_frames = blinking_frames

        self.__text_colors = [text_colors] if isinstance(text_colors, int) else text_colors
        self.__original_text_colors = [x for x in self.__text_colors]
        self.__color_mode = color_mode
        self.__color_speed = color_speed
        self.__last_change_color_time = pyxel.frame_count

        if "\n" not in self.text:
            if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
                self.x -= self.__text_width
            if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
                self.y -= self.__text_height
            if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
                self.x -= self.__text_width // 2
            if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
                self.y -= self.__text_height // 2

    def __draw_line(self, text:str, y:int, camera_x:int=0, camera_y:int=0)-> None:
        x = self.x
        text_width, text_height = text_size(text, self.__font_size)

        if self.__shadow:
            Text(text, x + self.__shadow_offset, y + self.__shadow_offset, self.__shadow_color, self.__font_size, self.__anchor, relative=self.__relative, underline=self.__underline, underline_color=self.__shadow_color).draw(camera_x, camera_y)

        if self.__anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
            x -= text_width
        if self.__anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
            y -= self.__text_height
        if self.__anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
            x -= text_width // 2
        if self.__anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
            y -= self.__text_height // 2

        if self.__relative:
            x += camera_x
            y += camera_y

        char_x = x

        if self.__font_size > 0:
            for char_index, char in enumerate(text):
                char_y = y + math.cos(pyxel.frame_count / self.__wave_speed + char_index * 0.3) * self.__wave_height if self.__wavy else y

                if char in characters_matrices:
                    char_matrix = characters_matrices[char]
                    char_width = len(char_matrix[0]) * self.__font_size

                    x += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                    char_y += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                    
                    for row_index, row in enumerate(char_matrix):
                        for col_index, pixel in enumerate(row):
                            if pixel:
                                pyxel.rect(x + col_index * self.__font_size, char_y + row_index * self.__font_size + (1 * self.__font_size if char in "gjpqy" else 0), self.__font_size, self.__font_size, self.__text_colors[char_index % len(self.__text_colors)])
                    
                    x += char_width + self.__font_size

            if self.__underline:
                pyxel.rect(char_x, y + text_height - self.__font_size, text_width, self.__font_size, self.__underline_color)
        else:
            for char_index, char in enumerate(text):
                char_y = y + math.cos(pyxel.frame_count / self.__wave_speed + char_index * 0.3) * self.__wave_height if self.__wavy else y
                x += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                char_y += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                pyxel.text(x, char_y, char, self.__text_colors[char_index % len(self.__text_colors)])
                x += 4

    def update(self)-> None:
        if self.__color_mode and pyxel.frame_count - self.__last_change_color_time >= self.__color_speed:
            if self.__color_mode == ROTATING_COLOR_MODE:
                self.__last_change_color_time = pyxel.frame_count
                self.__text_colors = [self.__text_colors[-1]] + self.__text_colors[:-1]
            elif self.__color_mode == RANDOM_COLOR_MODE:
                self.__last_change_color_time = pyxel.frame_count
                self.__text_colors = [random.choice(self.__original_text_colors) for _ in range(len(self.text))]

    def draw(self, camera_x:int=0, camera_y:int=0)-> None:
        if self.__blinking and pyxel.frame_count % (self.__blinking_frames) >= self.__blinking_frames // 2:
            return

        x = self.x
        y = self.y

        if "\n" in self.text:
            lines = self.text.split("\n")
            for i, line in enumerate(lines):
                if self.__font_size > 0:
                    self.__draw_line(line, y + i * (9 * self.__font_size), camera_x, camera_y)
                else:
                    self.__draw_line(line, y + i * 6, camera_x, camera_y)
            return
        
        if self.__relative:
            x += camera_x
            y += camera_y

        if self.__shadow:
            Text(self.text, self.__shadow_x, self.__shadow_y, self.__shadow_color, self.__font_size, self.__anchor, relative=self.__relative, underline=self.__underline, underline_color=self.__shadow_color).draw(camera_x, camera_y)

        if self.__font_size > 0:
            for char_index, char in enumerate(self.text):
                char_y = y + math.cos(pyxel.frame_count / self.__wave_speed + char_index * 0.3) * self.__wave_height if self.__wavy else y

                if char in characters_matrices:
                    char_matrix = characters_matrices[char]
                    char_width = len(char_matrix[0]) * self.__font_size

                    x += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                    char_y += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                    
                    for row_index, row in enumerate(char_matrix):
                        for col_index, pixel in enumerate(row):
                            if pixel:
                                pyxel.rect(x + col_index * self.__font_size, char_y + row_index * self.__font_size + (1 * self.__font_size if char in "gjpqy" else 0), self.__font_size, self.__font_size, self.__text_colors[char_index % len(self.__text_colors)])
                    
                    x += char_width + self.__font_size

            if self.__underline:
                pyxel.rect(self.x, y + self.__text_height - self.__font_size, self.__text_width, self.__font_size, self.__underline_color)
        else:
            for char_index, char in enumerate(self.text):
                char_y = y + math.cos(pyxel.frame_count / self.__wave_speed + char_index * 0.3) * self.__wave_height if self.__wavy else y
                x += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                char_y += random.uniform(-self.__glitch_intensity, self.__glitch_intensity)
                pyxel.text(x, char_y, char, self.__text_colors[char_index % len(self.__text_colors)])
                x += 4

class Button:

    def __init__(self, text:str, x:int, y:int, background_color:int, text_colors:list|int, hover_background_color:int, hover_text_colors:list|int, font_size:int=1, border:bool=False, border_color:int=0, color_mode:int=NORMAL_COLOR_MODE, color_speed:int=10, relative:bool=True, anchor:int=ANCHOR_TOP_LEFT, command=None)-> None:
        self.__x = x
        self.__y = y
        self.__width, self.__height = text_size(text, font_size)
        self.__width += 4 if border else 2
        self.__height += 4 if border else 2
        self.__background_color = background_color
        self.__hover_background_color = hover_background_color
        self.__border = border
        self.__border_color = border_color
        self.__relative = relative
        self.__command = command

        if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
            self.__x -= self.__width
        if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
            self.__y -= self.__height
        if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
            self.__x -= self.__width // 2
        if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
            self.__y -= self.__height // 2

        self.__text = Text(text, self.__x + 2 if border else self.__x + 1, self.__y + 2 if border else self.__y + 1, text_colors, font_size, color_mode=color_mode, color_speed=color_speed, relative=relative)
        self.__hover_text = Text(text, self.__x + 2 if border else self.__x + 1, self.__y + 2 if border else self.__y + 1, hover_text_colors, font_size, color_mode=color_mode, color_speed=color_speed, relative=relative)

    def is_hovered(self, camera_x:int=0, camera_y:int=0)-> bool:
        if self.__x <= pyxel.mouse_x < self.__x + self.__width and self.__y <= pyxel.mouse_y < self.__y + self.__height and self.__relative:
            return True
        if self.__x <= camera_x + pyxel.mouse_x < self.__x + self.__width and self.__y <= camera_y + pyxel.mouse_y < self.__y + self.__height and not self.__relative:
            return True
        
    def update(self, camera_x:int=0, camera_y:int=0)-> None:
        self.__text.update()
        self.__hover_text.update()
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and self.is_hovered(camera_x, camera_y) and self.__command:
            self.__command()

    def draw(self, camera_x:int=0, camera_y:int=0)-> None:
        x = camera_x + self.__x if self.__relative else self.__x
        y = camera_y + self.__y if self.__relative else self.__y
        if self.is_hovered(camera_x, camera_y):
            pyxel.rect(x, y, self.__width, self.__height, self.__hover_background_color)
            self.__hover_text.draw(camera_x, camera_y)
        else:
            pyxel.rect(x, y, self.__width, self.__height, self.__background_color)
            self.__text.draw(camera_x, camera_y)
        if self.__border:
            pyxel.rectb(x, y, self.__width, self.__height, self.__border_color)

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

    def __init__(self, relative_start_x:int, relative_start_y:int, relative_end_x:int, relative_end_y:int, width:int, height:int, char_speed:int=3, next_key:int=pyxel.KEY_SPACE)-> None:
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
        self.__next_key = next_key

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
                    if pyxel.btnp(self.__next_key):
                        self.__char_index = len(self.__dialog.lines[self.__current_line][1])
                        if self.__dialog.sound:
                            pyxel.play(self.__dialog.channel, self.__dialog.sound_number)
                    self.__frame_count += 1
                    if self.__frame_count % self.__char_speed == 0:
                        if self.__dialog.sound:
                            pyxel.play(self.__dialog.channel, self.__dialog.sound_number)
                        self.__char_index += 1
                else:
                    if pyxel.btnp(self.__next_key):
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
        if pyxel.frame_count % (30 * 2) < 50:
            pyxel.text(camera_x + self.__x + self.__width - len(keys_to_representation.get(self.__next_key, "") * 4) - 1, 
                    camera_y + self.__y + self.__height - 7, 
                    keys_to_representation.get(self.__next_key, ""), 
                    self.__text_colors if isinstance(self.__text_colors, int) else self.__text_colors[0])
        if self.__border:
            pyxel.rectb(camera_x + self.__x, camera_y + self.__y, self.__width, self.__height, self.__border_color)
        if self.__open:
            Text(self.__dialog.lines[self.__current_line][0], camera_x + self.__x + 2, camera_y + self.__y + 2, self.__names_colors, 1).draw()
        if self.__dialog:
            visible_text = self.__dialog.lines[self.__current_line][1][:self.__char_index]
            Text(visible_text, camera_x + self.__x + 2, camera_y + self.__y + 14, self.__text_colors, 1).draw()

class OvalParticle:

    def __init__(self, x:int, y:int, width:int, height:int, colors:list|int, lifespan:int, speed:int|float, target_x:int, target_y:int, growing_speed:int|float=0, acceleration_speed:int|float=0, dither_duration:int|float=0, hollow:bool=False)-> None:
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__colors = [colors] if isinstance(colors, int) else colors
        self.__colors_length = len(self.__colors)
        self.__current_color = 0
        self.__lifespan = round(lifespan / self.__colors_length) * self.__colors_length
        self.__starting_lifespan = self.__lifespan
        self.__growing_speed = growing_speed
        self.__acceleration_speed = acceleration_speed
        self.__hollow = hollow
        self.__dither = 1
        self.__dither_duration = max(dither_duration, 0)

        self.__direction_x = -1 if target_x - self.__x < 0 else 1
        self.__direction_y = -1 if target_y - self.__y < 0 else 1

        direction_x = target_x - self.__x
        direction_y = target_y - self.__y
        distance = math.sqrt(direction_x ** 2 + direction_y ** 2)
        if distance != 0:
            direction_x /= distance
            direction_y /= distance

        self.__speed_x = direction_x * speed
        self.__speed_y = direction_y * speed

    @property
    def lifespan(self)-> int:
        return self.__lifespan

    def update(self)-> None:
        self.__speed_x = abs(self.__speed_x) + self.__acceleration_speed
        self.__speed_y = abs(self.__speed_y) + self.__acceleration_speed

        self.__x += abs(self.__speed_x) * self.__direction_x
        self.__y += abs(self.__speed_y) * self.__direction_y

        self.__lifespan -= 1
        self.__width += self.__growing_speed
        self.__height += self.__growing_speed

        if self.__width <= 0 or self.__height <= 0:
            self.__lifespan = 0

        if self.__lifespan <= self.__dither_duration and self.__dither_duration:
            self.__dither -= 1 / self.__dither_duration

        if self.__lifespan % (self.__starting_lifespan / self.__colors_length) == 0 and self.__lifespan != 0:
            self.__current_color = (self.__current_color + 1) % self.__colors_length

    def draw(self)-> None:
        pyxel.dither(self.__dither)
        if self.__hollow:
            pyxel.ellib(self.__x - self.__width / 2, self.__y - self.__height / 2, self.__width, self.__height, self.__colors[self.__current_color])
        else:             
            pyxel.elli(self.__x - self.__width / 2, self.__y - self.__height / 2, self.__width, self.__height, self.__colors[self.__current_color])
        pyxel.dither(1)

class ParticleManager:

    def __init__(self)-> None:
        self.__particles :list[OvalParticle] = []

    def reset(self)-> None:
        self.__particles = []

    def add_particle(self, new_particle:OvalParticle)-> None:
        self.__particles.append(new_particle)

    def update(self)-> None:
        for particle in self.__particles:
            particle.update()

        self.__particles = [particle for particle in self.__particles if particle.lifespan > 0]

    def draw(self)-> None:
        for particle in self.__particles:
            particle.draw()


def text_size(text:str, font_size:int=1)-> tuple:
    lines = text.split("\n")
    if font_size == 0:
        return (max(len(line) * 4 for line in lines), 6 * len(lines))
    text_width = max(sum(len(characters_matrices[char][0]) * font_size + font_size for char in line) - font_size for line in lines)
    text_height = (9 * font_size + 1) * len(lines)

    return (text_width, text_height)

def wave_motion(value:int|float, wave_speed:int|float, wave_height:int|float, time:int)-> int|float:
    return value + (math.cos(time / wave_speed)) * wave_height

def lerp(start:int|float, end:int|float, speed:float=0.1)-> int|float:
    return start + (end - start) * speed

def clamp(value:int|float, min_value:int|float, max_value:int|float)-> int|float:
    return max(min_value, min(value, max_value))

def draw_moving_spiral(x:int, y:int, radius:int, color:int, time:int, turns:int=3, segments:int=50, speed:int|float=0.05)-> None:
    for i in range(segments):
        angle = (i / segments) * (turns * math.pi * 2) + time * speed
        r = (i / segments) * radius
        px = x + math.cos(angle) * r
        py = y + math.sin(angle) * r
        pyxel.pset(int(px), int(py), color)

def hex_to_rgb(hex_val:int)-> tuple:
    r = (hex_val >> 16) & 0xFF
    g = (hex_val >> 8) & 0xFF
    b = hex_val & 0xFF
    return r, g, b

def rgb_to_hex(r:int, g:int, b:int)-> int:
    return int(f"0x{r:02X}{g:02X}{b:02X}", 16)

def grayscaled_palette(original_palette:list)-> list:
    palette = []
    for color in original_palette:
        r, g, b = hex_to_rgb(color)
        gray = int((r + g + b) / 3)
        palette.append(rgb_to_hex(gray, gray, gray))

    return palette
