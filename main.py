"""
@author : Léo IMBERT & Eddy MONGIN
@created : 14/05/2025
@updated : 07/08/2025

* Gems Types :
- Green : Jump Gem
- Yellow : Build Gem
- Pink : Phase Gem
- Blue : Dash Gem
- Red : Gravity Gem
- Grey : Breaking Gem

* Pyxres Files :
1.pyxres : Main menu, Credits, Level Selection, Level 1, Level 2, Level 3, Level 4, level 5
2.pyxres : Level 6, Level 7, Level 8, Level 9

* Pyxres Images :
0. Cursor / Player / Ennemy
1. Tiles /
2.

* Pyxres Sounds :
0. Button Click
1. Collect Gem
2. Jump
3. Dash
4. Break
5. Gravity
6. Phase
7. Death
8. Win
9. No Gem
10. Dialog
11. Music Lead Melody
12. Music Bass Line
13. Build Gem

* Pyxel Channels :
0. Buttons / Collect Gem / Dialog
1. Use Gems / Death / Win / No Gem
2. Music Lead Melody
3. Music Bass Line
"""

#? Importations
from copy import deepcopy
import random
import pyxel
import time
import math
import sys
import os

#? Utils
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

    def __init__(self, width:int, height:int, scenes:list, default_scene_id:int=0, fps:int=60, fullscreen:bool=False, mouse:bool=False, quit_key:int=pyxel.KEY_ESCAPE, camera_x:int=0, camera_y:int=0):
        
        self.__fps = fps
        self.__scenes_dict = {scene.id:scene for scene in scenes}
        self.__current_scene = self.__scenes_dict.get(default_scene_id, 0)
        self.__transition = {}

        self.__cam_x = self.__cam_tx = camera_x
        self.__cam_y = self.__cam_ty = camera_y
        self.__shake_amount = 0
        self.__sub_shake_amount = 0

        pyxel.init(width, height, fps=self.__fps, quit_key=quit_key)
        pyxel.fullscreen(fullscreen)
        pyxel.mouse(mouse)

        if self.__current_scene.pyxres_path:
            pyxel.load(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), self.__current_scene.pyxres_path))
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)
        pyxel.colors.from_list(self.__current_scene.palette)

    @property
    def camera_x(self)-> int:
        return self.__cam_x
    
    @property
    def camera_y(self)-> int:
        return self.__cam_y

    @property
    def mouse_x(self)-> int:
        return self.__cam_x + pyxel.mouse_x
    
    @property
    def mouse_y(self)-> int:
        return self.__cam_y + pyxel.mouse_y
    
    @property
    def fps(self)-> int:
        return self.__fps
    
    def set_camera(self, new_camera_x:int, new_camera_y:int):
        self.__cam_x = self.__cam_tx = new_camera_x
        self.__cam_y = self.__cam_ty = new_camera_y

    def move_camera(self, new_camera_x:int, new_camera_y:int):
        self.__cam_tx = new_camera_x
        self.__cam_ty = new_camera_y

    def shake_camera(self, amount:int, sub_amount:float):
        self.__shake_amount = amount
        self.__sub_shake_amount = sub_amount

    def change_scene(self, new_scene_id:int, new_camera_x:int=0, new_camera_y:int=0):
        self.set_camera(new_camera_x, new_camera_y)

        self.__current_scene = self.__scenes_dict.get(new_scene_id, 0)

        if self.__current_scene.pyxres_path:
            pyxel.load(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), self.__current_scene.pyxres_path))
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)
        pyxel.colors.from_list(self.__current_scene.palette)

    def change_scene_dither(self, new_scene_id:int, speed:float, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.__transition = {
            "type":"dither",
            "direction":1,
            "new_scene_id":new_scene_id,
            "speed":speed,
            "transition_color":transition_color,
            "new_camera_x":new_camera_x,
            "new_camera_y":new_camera_y,
            "dither":0,
            "action":action
        }

    def change_scene_outer_circle(self, new_scene_id:int, speed:int, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.__transition = {
            "type":"outer_circle",
            "direction":1,
            "new_scene_id":new_scene_id,
            "speed":speed,
            "transition_color":transition_color,
            "new_camera_x":new_camera_x,
            "new_camera_y":new_camera_y,
            "start_end":int(((pyxel.width ** 2 + pyxel.height ** 2) ** 0.5) / 2) + 1,
            "end":int(((pyxel.width ** 2 + pyxel.height ** 2) ** 0.5) / 2) + 1,
            "action":action
        }

    def apply_palette_effect(self, effect_function):
        pyxel.colors.from_list(effect_function(self.__current_scene.palette))

    def reset_palette(self):
        pyxel.colors.from_list(self.__current_scene.palette)

    def handle_transitions(self):

        if self.__transition.get("type") == "dither":
            self.__transition["dither"] += self.__transition["speed"] * self.__transition["direction"]

            if self.__transition["dither"] > 1 and self.__transition["direction"] == 1:
                self.__transition["direction"] = -1
                self.change_scene(self.__transition["new_scene_id"], self.__transition["new_camera_x"], self.__transition["new_camera_y"])
                if self.__transition["action"]:
                    self.__transition["action"]()
            if self.__transition["dither"] < 0 and self.__transition["direction"] == -1:
                self.__transition = {}
                return
            pyxel.dither(self.__transition["dither"])
            pyxel.rect(self.__cam_x, self.__cam_y, pyxel.width, pyxel.height, self.__transition["transition_color"])
            pyxel.dither(1)

        elif self.__transition.get("type") == "outer_circle":
            self.__transition["end"] -= self.__transition["speed"] * self.__transition["direction"]

            if self.__transition["end"] < 0 and self.__transition["direction"] == 1:
                self.__transition["direction"] = -1
                self.change_scene(self.__transition["new_scene_id"], self.__transition["new_camera_x"], self.__transition["new_camera_y"])
                if self.__transition["action"]:
                    self.__transition["action"]()
            if self.__transition["end"] > self.__transition["start_end"] and self.__transition["direction"] == -1:
                self.__transition = {}
                return
            
            for radius in range(self.__transition["start_end"], self.__transition["end"], -1):
                pyxel.ellib(self.__cam_x + pyxel.width / 2 - radius, self.__cam_y + pyxel.height / 2 - radius, radius * 2, radius * 2, self.__transition["transition_color"])
                pyxel.ellib(self.__cam_x + pyxel.width / 2 - radius + 1, self.__cam_y + pyxel.height / 2 - radius, radius * 2, radius * 2, self.__transition["transition_color"])

    def update(self):
        self.__cam_x += (self.__cam_tx - self.__cam_x) * 0.1
        self.__cam_y += (self.__cam_ty - self.__cam_y) * 0.1

        if self.__shake_amount > 0:
            amount = int(self.__shake_amount)
            pyxel.camera(self.__cam_x + random.randint(-amount, amount), self.__cam_y + random.randint(-amount, amount))
            self.__shake_amount -= self.__sub_shake_amount
        else:
            pyxel.camera(self.__cam_x, self.__cam_y)

        if not self.__transition.get("type"):
            self.__current_scene.update()

    def draw(self):
        self.__current_scene.draw()
        if self.__transition:
            self.handle_transitions()

    def run(self):
        pyxel.run(self.update, self.draw)

class Scene:

    def __init__(self, id:int, title:str, update, draw, pyxres_path:str, palette:list, screen_mode:int=0):
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
        self.flip_horizontal = True

    def unflip_h(self) -> None:
        self.flip_horizontal = False

    def flip_v(self) -> None:
        self.flip_vertical = True

    def unflip_v(self) -> None:
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
        self.background_color = background_color
        self.hover_background_color = hover_background_color
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
            pyxel.rect(x, y, self.__width, self.__height, self.hover_background_color)
            self.__hover_text.draw(camera_x, camera_y)
        else:
            pyxel.rect(x, y, self.__width, self.__height, self.background_color)
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

#? Constants
FPS = 60
PALETTE = [0x000000, 0xE6E1CC, 0x2E1B37, 0xB49A8D, 0xFFDBAC, 0xA45A41, 0xCF4F4F, 0xD87E46, 0xEDD15A, 0x7DA446, 0x3A7E4C, 0x28524E, 0x7394BA, 0x4E53A2, 0x8C315D, 0xF6788D, 0x4E9FE5]

COLLISION_TILES = [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),
                   (0,2),(1,2),(2,2),(3,2),
                   (0,3),(1,3),(2,3),(3,3),
                   (0,4),(1,4),(2,4),(3,4)]

KILL_TILES = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)]

DOOR_TILES = [(0,8),(1,8),(0,9),(1,9)]

BREAK_TILES = [(4,1),(5,1)]

JUMP_GEM = 0
BUILD_GEM = 1
PHASE_GEM = 2
DASH_GEM = 3
GRAVITY_GEM = 4
BREAK_GEM = 5

GEM_COLORS_DICT = {
    JUMP_GEM : [9, 10, 11],
    BUILD_GEM : [7, 8],
    PHASE_GEM : [1, 15],
    DASH_GEM : [12, 13],
    GRAVITY_GEM : [6, 14],
    BREAK_GEM : [3, 4]
}

GEMS_DICT = {
    JUMP_GEM : (1, 80, 6, 8),
    BUILD_GEM : (8, 80, 8, 8),
    PHASE_GEM : (17, 80, 6, 8),
    DASH_GEM : (24, 81, 7, 7),
    GRAVITY_GEM : (32, 80, 8, 8),
    BREAK_GEM : (40, 80, 8, 8)
}

SPECIAL_TILES_DICT = {
    (0, 10) : [(0, 0), JUMP_GEM],
    (1, 10) : [(0, 0), BUILD_GEM],
    (2, 10) : [(0, 0), PHASE_GEM],
    (3, 10) : [(0, 0), DASH_GEM],
    (4, 10) : [(0, 0), GRAVITY_GEM],
    (5, 10) : [(0, 0), BREAK_GEM]
}

#? Game Classes
class Tilemap:

    def __init__(self, id:int, x:int, y:int, w:int, h:int, colkey:int):
        self.id = id
        self.x = x
        self.y = y
        self.w, self.h = w, h
        self.colkey = colkey

    def collision_rect_tiles(self, x:int, y:int, w:int, h:int, tiles:list)-> bool:
        start_tile_x = (x - self.x) // 8
        start_tile_y = (y - self.y) // 8
        end_tile_x = (x + w - self.x - 1) // 8
        end_tile_y = (y + h - self.y - 1) // 8

        start_tile_x = clamp(start_tile_x, 0, self.w // 8 - 1)
        start_tile_y = clamp(start_tile_y, 0, self.h // 8 - 1)
        end_tile_x = clamp(end_tile_x, 0, self.w // 8 - 1)
        end_tile_y = clamp(end_tile_y, 0, self.h // 8 - 1)

        for tile_y in range(int(start_tile_y), int(end_tile_y) + 1):
            for tile_x in range(start_tile_x, end_tile_x + 1):
                tile_id = pyxel.tilemaps[self.id].pget(tile_x, tile_y)

                if tile_id in tiles:
                    return True
        
        return False
    
    def collision_tile_coord(self, x:int, y:int, w:int, h:int, tile_x1:int, tile_y1)-> bool:
        start_tile_x = (x - self.x) // 8
        start_tile_y = (y - self.y) // 8
        end_tile_x = (x + w - self.x - 1) // 8
        end_tile_y = (y + h - self.y - 1) // 8

        start_tile_x = clamp(start_tile_x, 0, self.w // 8 - 1)
        start_tile_y = clamp(start_tile_y, 0, self.h // 8 - 1)
        end_tile_x = clamp(end_tile_x, 0, self.w // 8 - 1)
        end_tile_y = clamp(end_tile_y, 0, self.h // 8 - 1)

        for tile_y in range(int(start_tile_y), int(end_tile_y) + 1):
            for tile_x in range(start_tile_x, end_tile_x + 1):
                if tile_x == tile_x1 and tile_y == tile_y1:
                    return True
        
        return False
    
    def replace_tiles(self, x:int, y:int, width:int, height:int, radius:int, tiles:list, replace_tile:tuple):
        start_tile_x = (x - radius - self.x) // 8
        start_tile_y = (y - radius - self.y) // 8
        end_tile_x = (x + width + radius - self.x - 1) // 8
        end_tile_y = (y + height + radius - self.y - 1) // 8

        start_tile_x = clamp(start_tile_x, 0, self.w // 8 - 1)
        start_tile_y = clamp(start_tile_y, 0, self.h // 8 - 1)
        end_tile_x = clamp(end_tile_x, 0, self.w // 8 - 1)
        end_tile_y = clamp(end_tile_y, 0, self.h // 8 - 1)

        for tile_y in range(int(start_tile_y), int(end_tile_y) + 1):
            for tile_x in range(start_tile_x, end_tile_x + 1):
                tile_id = pyxel.tilemaps[self.id].pget(tile_x, tile_y)

                if tile_id in tiles:
                    pyxel.tilemaps[self.id].pset(tile_x, tile_y, replace_tile)

    def load_tiles(self, gems=None)-> list:
        new_gems = deepcopy(gems) if gems else []
        tiles_x = self.w // 8
        tiles_y = self.h // 8

        for ty in range(tiles_y):
            for tx in range(tiles_x):
                tile_x = tx
                tile_y = ty
                tile_id = pyxel.tilemaps[self.id].pget(tile_x, tile_y)

                if tile_id in SPECIAL_TILES_DICT:
                    replacement_tile, object_type = SPECIAL_TILES_DICT[tile_id]
                    pyxel.tilemaps[self.id].pset(tile_x, tile_y, replacement_tile)

                    world_x = self.x + tx * 8
                    world_y = self.y + ty * 8

                    if object_type in [JUMP_GEM, BUILD_GEM, PHASE_GEM, DASH_GEM, GRAVITY_GEM, BREAK_GEM]:
                        new_gems.append(Gem(object_type, world_x, world_y))

        return new_gems

    def draw(self):
        pyxel.bltm(self.x, self.y, self.id, 0, 0, self.w, self.h, self.colkey)

class Player:

    def __init__(self, x:int, y:int, tilemap:Tilemap, gems:list=None):
        self.x = x
        self.y = y
        self.width = 6
        self.height = 7
        self.tilemap = tilemap
        self.gems = deepcopy(gems) if gems else []

        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 0.5
        self.jump_power = 4
        self.max_velocity_x = 1.5
        self.max_velocity_y = 2
        self.gravity = 0.4
        self.friction = 0.85
        self.dashing_timer = 0
        self.dashing_time = 5
        self.gravity_direction = 1

        self.particle_manager = ParticleManager()

        self.player_idle = Animation(Sprite(0, 0, 9, 6, 7, 0), 2, 20, True)
        self.player_walk = Animation(Sprite(0, 0, 17, 6, 7, 0), 5, 10, True)
        self.player_death = Animation(Sprite(0, 0, 25, 6, 7, 0), 5, 15, False)
        self.player_win = Animation(Sprite(0, 0, 33, 6, 7, 0), 5, 15, False)

        self.facing_right = True
        self.is_dashing = False
        self.jumping = False
        self.on_ground = False
        self.dead = False
        self.win = False
        self.is_breaking = False

    def use_gem(self, gem:int):
        if gem == JUMP_GEM and self.on_ground and not self.jumping:
            pyxel.play(1, 2)
            self.gems.pop(0)
            self.velocity_y = -self.jump_power * self.gravity_direction
            self.jumping = True
            self.on_ground = False
        elif gem == BUILD_GEM:
            self.gems.pop(0)
            pyxel.play(1, 13)
            if pyxel.tilemaps[self.tilemap.id].pget(self.x // 8, self.y // 8 + 2 * self.gravity_direction) == (0, 0):
                pyxel.tilemaps[self.tilemap.id].pset(self.x // 8, self.y // 8 + 2 * self.gravity_direction, (random.randint(4, 5), 1))
            if pyxel.tilemaps[self.tilemap.id].pget(self.x // 8 - 1, self.y // 8 + 2 * self.gravity_direction) == (0, 0):
                pyxel.tilemaps[self.tilemap.id].pset(self.x // 8 - 1, self.y // 8 + 2 * self.gravity_direction, (random.randint(4, 5), 1))
            if pyxel.tilemaps[self.tilemap.id].pget(self.x // 8 + 1, self.y // 8 + 2 * self.gravity_direction) == (0, 0):
                pyxel.tilemaps[self.tilemap.id].pset(self.x // 8 + 1, self.y // 8 + 2 * self.gravity_direction, (random.randint(4, 5), 1))
        elif gem == PHASE_GEM and not self.tilemap.collision_rect_tiles(self.x, self.y - 32 * self.gravity_direction, self.width, self.height, COLLISION_TILES):
            pyxel.play(1, 6)
            self.gems.pop(0)
            self.y -= 32 * self.gravity_direction
        elif gem == DASH_GEM:
            pyxel.play(1, 3)
            self.gems.pop(0)
            self.is_dashing = True
            self.velocity_x = 4 if self.facing_right else -4
        elif gem == GRAVITY_GEM:
            pyxel.play(1, 5)
            self.gems.pop(0)
            self.gravity_direction = -self.gravity_direction
        elif gem == BREAK_GEM:
            pyxel.play(1, 4)
            self.gems.pop(0)
            self.tilemap.replace_tiles(self.x, self.y, self.width, self.height, 4, BREAK_TILES, (0, 0))
            self.is_breaking = True
        
        if (gem == JUMP_GEM and (not self.on_ground or self.jumping)) or (gem == PHASE_GEM and self.tilemap.collision_rect_tiles(self.x, self.y - 32 * self.gravity_direction, self.width, self.height, COLLISION_TILES)):
            return

        for _ in range(10):
            c = [random.choice(GEM_COLORS_DICT[gem]) for _ in range(3)]
            size = random.randint(1, 2)
            x = random.randint(self.x - 2, self.x + 8)
            y = self.y + self.height if self.gravity_direction == 1 else self.y
            self.particle_manager.add_particle(OvalParticle(x, y, size, size, c, 100, random.uniform(0.08, 0.25), x, y - self.gravity_direction))

    def update_velocity_x(self):
        if self.velocity_x != 0:
            step_x = 1 if self.velocity_x > 0 else -1
            for _ in range(int(abs(self.velocity_x))):
                if not self.tilemap.collision_rect_tiles(self.x + step_x, self.y, self.width, self.height, COLLISION_TILES):
                    self.x += step_x
                else:
                    self.velocity_x = 0
                    break

    def update_velocity_y(self):
        if self.velocity_y != 0:
            step_y = 1 if self.velocity_y > 0 else -1
            for _ in range(int(abs(self.velocity_y))):
                if not self.tilemap.collision_rect_tiles(self.x, self.y + step_y, self.width, self.height, COLLISION_TILES):
                    self.y += step_y
                else:
                    self.velocity_y = 0
                    break

    def update(self):
        self.is_breaking = False
        self.particle_manager.update()

        if self.dashing_timer > self.dashing_time:
            self.dashing_timer = 0
            self.is_dashing = False

        if self.dead:
            self.player_death.update()
            return
        
        if self.win:
            self.player_win.update()
            return
        
        if self.is_dashing:
            self.dashing_timer += 1
            if pyxel.btnp(pyxel.KEY_SPACE) and len(self.gems) > 0:
                self.use_gem(self.gems[0].type)
            elif pyxel.btnp(pyxel.KEY_SPACE):
                pyxel.play(1, 9)
            self.update_velocity_x()
            return

        self.player_idle.update()
        self.player_walk.update()

        if self.gravity_direction == 1 and (self.tilemap.collision_rect_tiles(self.x, self.y, self.width, self.height, KILL_TILES) and self.velocity_y >= 0 and not self.dead) or (self.tilemap.collision_rect_tiles(self.x, self.y, self.width, self.height, KILL_TILES) and self.velocity_y < -1 and not self.dead):
            pyxel.play(1, 7)
            self.dead = True
        elif self.gravity_direction == -1 and (self.tilemap.collision_rect_tiles(self.x, self.y, self.width, self.height, KILL_TILES) and self.velocity_y > 0 and not self.dead) or (self.tilemap.collision_rect_tiles(self.x, self.y, self.width, self.height, KILL_TILES) and self.velocity_y <= -1 and not self.dead):
            pyxel.play(1, 7)
            self.dead = True

        self.velocity_y += self.gravity * self.gravity_direction
        if self.velocity_y > self.max_velocity_y and self.gravity_direction == 1:
            self.velocity_y = self.max_velocity_y
        if self.velocity_y < -self.max_velocity_y and self.gravity_direction == -1:
            self.velocity_y = -self.max_velocity_y

        self.velocity_x *= self.friction
        self.on_ground = self.tilemap.collision_rect_tiles(self.x, self.y + self.gravity_direction, self.width, self.height, COLLISION_TILES)

        if self.on_ground:
            self.jumping = False

        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_A):
            self.velocity_x = max(self.velocity_x - self.speed, -self.max_velocity_x)
            self.facing_right = False
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self.velocity_x = min(self.velocity_x + self.speed, self.max_velocity_x)
            self.facing_right = True
        if pyxel.btnp(pyxel.KEY_E) and self.tilemap.collision_rect_tiles(self.x, self.y, self.width, self.height, DOOR_TILES):
            pyxel.play(1, 8)
            self.win = True
        if pyxel.btnp(pyxel.KEY_SPACE) and len(self.gems) > 0:
            self.use_gem(self.gems[0].type)
        elif pyxel.btnp(pyxel.KEY_SPACE):
            pyxel.play(1, 9)

        self.update_velocity_x()
        self.update_velocity_y()

    def draw(self, camera_x:int=0, camera_y:int=0):
        for anim in [self.player_idle, self.player_walk, self.player_death, self.player_win]:
            if self.facing_right:
                anim.unflip_h()
            else:
                anim.flip_h()

            if self.gravity_direction == 1:
                anim.unflip_v()
            else:
                anim.flip_v()

        self.particle_manager.draw()

        if self.dead:
            self.player_death.draw(self.x, self.y)
        elif self.win:
            self.player_win.draw(self.x, self.y)
        elif -1 < self.velocity_x < 1 and self.on_ground:
            self.player_idle.draw(self.x, self.y)
        elif self.on_ground:
            self.player_walk.draw(self.x, self.y)
        else:
            pyxel.blt(self.x, self.y, 0, 0, 9, self.width * (1 if self.facing_right else -1), self.height * self.gravity_direction, 0)

        if self.tilemap.collision_rect_tiles(self.x, self.y, self.width, self.height, DOOR_TILES + [(3,5)]):
            Text("E", self.x, self.y - 1, 1, 1, ANCHOR_BOTTOM_LEFT).draw()

        for index, gem in enumerate(self.gems):
            pyxel.blt(camera_x + 2 + 8 * index, camera_y + 2, 1, gem.u, gem.v, gem.w, gem.h, 0)

class Gem:

    def __init__(self, type:int, x:int=0, y:int=0):
        self.x = x
        self.y = y
        self.type = type
        self.u, self.v, self.w, self.h = GEMS_DICT[type]
        self.wave_speed = random.randint(10, 15)
        self.collected = False

class GemManager:

    def __init__(self, gems:list=None):
        self.gems:list[Gem] = deepcopy(gems) if gems else []

    def update(self, player:Player):
        for gem in self.gems:
            if gem.x < player.x + player.width and gem.x + gem.w > player.x and gem.y < player.y + player.height and gem.y + gem.h > player.y and not gem.collected:
                player.gems.append(gem)
                pyxel.play(0, 1)
                gem.collected = True

        self.gems = [gem for gem in self.gems if not gem.collected]

    def draw(self):
        for gem in self.gems:
            pyxel.blt(gem.x, wave_motion(gem.y, gem.wave_speed, 1, pyxel.frame_count), 1, gem.u, gem.v, gem.w, gem.h, 0)

#? Game Class
class Game:

    def __init__(self):
        #? Scenes
        main_menu_scene = Scene(0, "Queue It ! - Main Menu", self.update_main_menu, self.draw_main_menu, "assets/1.pyxres", PALETTE)
        credits_scene = Scene(1, "Queue It ! - Credits", self.update_credits, self.draw_credits, "assets/1.pyxres", PALETTE)
        level_selection_scene = Scene(2, "Queue It ! - Level Selection", self.update_level_selection, self.draw_level_selection, "assets/1.pyxres", PALETTE)
        level_1_scene = Scene(3, "Queue It ! - Level 1", lambda:self.update_level(1), lambda:self.draw_level(1), "assets/1.pyxres", PALETTE)
        level_2_scene = Scene(4, "Queue It ! - Level 2", lambda:self.update_level(2), lambda:self.draw_level(2), "assets/1.pyxres", PALETTE)
        level_3_scene = Scene(5, "Queue It ! - Level 3", lambda:self.update_level(3), lambda:self.draw_level(3), "assets/1.pyxres", PALETTE)
        level_4_scene = Scene(6, "Queue It ! - Level 4", lambda:self.update_level(4), lambda:self.draw_level(4), "assets/1.pyxres", PALETTE)
        level_5_scene = Scene(7, "Queue It ! - Level 5", lambda:self.update_level(5), lambda:self.draw_level(5), "assets/1.pyxres", PALETTE)
        level_6_scene = Scene(8, "Queue It ! - Level 6", lambda:self.update_level(6), lambda:self.draw_level(6), "assets/2.pyxres", PALETTE)
        level_7_scene = Scene(9, "Queue It ! - Level 7", lambda:self.update_level(7), lambda:self.draw_level(7), "assets/2.pyxres", PALETTE)
        level_8_scene = Scene(10, "Queue It ! - Level 8", lambda:self.update_level(8), lambda:self.draw_level(8), "assets/2.pyxres", PALETTE)
        level_9_scene = Scene(11, "Queue It ! - Level 9", lambda:self.update_level(9), lambda:self.draw_level(9), "assets/2.pyxres", PALETTE)

        scenes = [main_menu_scene, credits_scene, level_selection_scene, level_1_scene, level_2_scene, level_3_scene, level_4_scene, level_5_scene, 
                  level_6_scene, level_7_scene, level_8_scene, level_9_scene]

        #? Pyxel Manager
        self.pyxel_manager = PyxelManager(228, 128, scenes, 0, FPS, True, False, pyxel.KEY_A)

        #? Game Variables
        self.max_level = 20

        #? Main Menu Variables
        self.main_menu_title = Text("Queue It !", 114, 10, [6,6,7,7,8,8], 2, ANCHOR_TOP, ROTATING_COLOR_MODE, 20, shadow=True, shadow_color=2, shadow_offset=2)
        self.main_menu_play_button = Button("Play", 114, 60, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.menu_buttons_action(2))
        self.main_menu_credits_button = Button("Credits", 114, 80, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.menu_buttons_action(1))
        self.main_menu_quit_button = Button("Quit", 114, 100, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:pyxel.quit())

        #? Credits Variables
        self.credits_text = Text("This game was made by\nLéo Imbert & Eddy Mongin.\n\n\n\n\n\n\n\nIt was originally created for\n'La Nuit Du Code', but\nwe continued working on it\nand made this finished version.", 114, 10, 8, 1, ANCHOR_TOP, shadow=True, shadow_color=2)
        self.credits_back_button = Button("Back", 2, 2, 6, 8, 7, 8, 1, True, 8, command=lambda:self.menu_buttons_action(0))

        #? Level Selection Variables
        self.level_selection_title = Text("Level Selection", 114, 5, [6,6,7,7,8,8], 2, ANCHOR_TOP, ROTATING_COLOR_MODE, 20, shadow=True, shadow_color=2, shadow_offset=2)
        self.level_selection_button_1 = Button("1 ", 54, 46, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.level_buttons_action(1))
        self.level_selection_button_2 = Button("2 ", 74, 46, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.level_buttons_action(2))
        self.level_selection_button_3 = Button("3 ", 94, 46, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.level_buttons_action(3))
        self.level_selection_button_4 = Button("4 ", 114, 46, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.level_buttons_action(4))
        self.level_selection_button_5 = Button("5 ", 134, 46, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.level_buttons_action(5))
        self.level_selection_button_6 = Button("6 ", 154, 46, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.level_buttons_action(6))
        self.level_selection_button_7 = Button("7 ", 174, 46, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.level_buttons_action(7))
        self.level_selection_button_8 = Button("8 ", 54, 66, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.level_buttons_action(8))
        self.level_selection_button_9 = Button("9 ", 74, 66, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP, command=lambda:self.level_buttons_action(9))
        self.level_selection_button_10 = Button("10", 94, 66, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_11 = Button("11", 114, 66, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_12 = Button("12", 134, 66, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_13 = Button("13", 154, 66, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_14 = Button("14", 174, 66, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_15 = Button("15", 54, 86, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_16 = Button("16", 74, 86, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_17 = Button("17", 94, 86, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_18 = Button("18", 114, 86, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_19 = Button("19", 134, 86, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_20 = Button("20", 154, 86, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_21 = Button("21", 174, 86, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_back_button = Button("Back", 2, 126, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_BOTTOM_LEFT, command=lambda:self.menu_buttons_action(0))

        #? Main Menus
        self.player_animation_menus = Animation(Sprite(0, 0, 9, 6, 7, 0), 2, 20, True)

        #? Dialogs
        self.dialog_1 = Dialog([("Sign", "Welcome to Queue It !\nUse the right gem to overcome\neach challenge."),
                                ("Sign", "Each gem gives you a different\nability. Press SPACE to use the\nfirst gem in your queue."),
                                ("Sign", "If you get stuck, press R to\nrestart the level at any time."),
                                ("Sign", "You can also press ESC to\nreturn to the main menu."),
                                ("Sign", "See that green gem up ahead ?\nIt gives you the power to JUMP."),
                                ("Sign", "Go on, give it a try !")], 0, 9, 9, True, 9, True, 0, 10)
        self.dialog_2 = Dialog([("Sign", "This gem grants a quick DASH\nforward."),
                                ("Sign", "While dashing, you're invincible,\nperfect for dodging hazards !")], 0, 12, 12, True, 12, True, 0, 10)
        self.dialog_3 = Dialog([("Sign", "The gem on your left lets you\nPHASE upward through terrain."),
                                ("Sign", "It moves you up to 4 tiles,\ngreat for tight spaces or\nreaching ledges!")], 0, 15, 15, True, 15, True, 0, 10)
        self.dialog_4 = Dialog([("Sign", "This gem flips your GRAVITY."),
                                ("Sign", "You'll fall upward but you can\nstill jump and phase\n(just downward instead).")], 0, 6, 6, True, 6, True, 0, 10)
        self.dialog_5 = Dialog([("Sign", "This gem gives you the power to\nBREAK weaker blocks."),
                                ("Sign", "It destroys all nearby\nbreakable tiles in a small\nradius.")], 0, 4, 4, True, 4, True, 0, 10)
        self.dialog_6 = Dialog([("Sign", "Stuck with nowhere to land ?\nNot anymore."),
                                ("Sign", "The BUILD gem creates a\nplatform under you."),
                                ("Sign", "Use it to save yourself from\nfalling."),
                                ("Sign", "Try building under your feet\nnow !")], 0, 8, 8, True, 8, True, 0, 10)
        self.dialog_7 = Dialog([("Sign", "Well done ! You've mastered the\ngem queue."),
                                ("Sign", "Remember : gems are used in the\norder they appear."),
                                ("Sign", "Think ahead, plan your queue,\nand adapt on the fly."),
                                ("Sign", "Good luck - the real challenge\nbegins now !")], 0, 1, 1, True, 1, True, 0, 10)

        #? Levels Variables
        self.tilemap = None
        self.player: Player = None
        self.gem_manager = None
        self.dialog_manager = DialogManager(5, -50, 5, 5, 118, 50, 3, pyxel.KEY_E)

        self.setup_music()
        self.color_level_selection_buttons()

        #? Run
        self.pyxel_manager.run()

    def setup_music(self):
        pyxel.sounds[11].set(
            "b-2b-2b-2b-2a-2a-2a-2a-2 g2g2e-2e-2c2c2f2f2 f2f2g2g2f2f2e2e2 e2e2c2c2c2c2rr"
            "rrb-1b-1c2c2e-2e-2 f2f2f2f2e-2e-2f2f2 g2g2b-2b-2c3c3f2f2 f2f2e-2e-2e-2e-2f2f2",
            "0",
            "2",
            "vvvfnnnf nfnfnfvv vfnfnfvv vfvvvfvv vfnfnfvf vfnfnfnf nfnfnfvv vfnnnfnf",
            16,
            )
        pyxel.sounds[12].set("a-0rra-0 b-0rrb-0 g0rrg0 c1rrc1", "2", "2", "f", 32)
        pyxel.musics[0].set([], [], [11], [12])
        pyxel.playm(0, loop=True)

    def color_level_selection_buttons(self):
        for level_num in range(1, self.max_level + 2):
            exec(f"self.level_selection_button_{level_num}.background_color = 6")
            exec(f"self.level_selection_button_{level_num}.hover_background_color = 7")

        for level_num in range(self.max_level + 2, 22):
            exec(f"self.level_selection_button_{level_num}.background_color = 13")
            exec(f"self.level_selection_button_{level_num}.hover_background_color = 12")

    def menu_buttons_action(self, scene_id:int):
        pyxel.play(0, 0)
        self.pyxel_manager.change_scene_dither(scene_id, 0.05, 2, action=lambda:time.sleep(0.1))

    def level_buttons_action(self, level:int):
        if level > self.max_level + 1:
            pyxel.play(1, 9)
            return

        pyxel.play(0, 0)
        self.dialog_manager = DialogManager(5, -50, 5, 5, 218, 50, 3, pyxel.KEY_E)

        def action():

            if level == 1:
                self.tilemap = Tilemap(3, 0, 0, 96*8, 56*8, 0)
                self.player = Player(18*8, 29*8, self.tilemap)
            elif level == 2:
                self.tilemap = Tilemap(4, 0, 0, 72*8, 40*8, 0)
                self.player = Player(20*8, 29*8, self.tilemap)
            elif level == 3:
                self.tilemap = Tilemap(5, 0, 0, 96*8, 48*8, 0)
                self.player = Player(19*8, 29*8, self.tilemap)
            elif level == 4:
                self.tilemap = Tilemap(6, 0, 0, 80*8, 32*8, 0)
                self.player = Player(22*8, 13*8, self.tilemap)
            elif level == 5:
                self.tilemap = Tilemap(7, 0, 0, 72*8, 24*8, 0)
                self.player = Player(16*8, 8*8, self.tilemap, [Gem(JUMP_GEM), Gem(BREAK_GEM)])
            elif level == 6:
                self.tilemap = Tilemap(0, 0, 0, 48*8, 40*8, 0)
                self.player = Player(26*8, 23*8, self.tilemap, [Gem(JUMP_GEM), Gem(JUMP_GEM), Gem(JUMP_GEM), Gem(DASH_GEM)])
            elif level == 7:
                self.tilemap = Tilemap(1, 0, 0, 48*8, 48*8, 0)
                self.player = Player(23*8, 31*8, self.tilemap, [Gem(PHASE_GEM) for _ in range(4)])
            elif level == 8:
                self.tilemap = Tilemap(2, 0, 0, 56*8, 56*8, 0)
                self.player = Player(21*8, 23*8, self.tilemap, [Gem(GRAVITY_GEM) for _ in range(4)])
            elif level == 9:
                self.tilemap = Tilemap(3, 0, 0, 64*8, 48*8, 0)
                self.player = Player(23*8, 22*8, self.tilemap)

            self.gem_manager = GemManager(self.tilemap.load_tiles())
            self.pyxel_manager.set_camera(self.player.x - 114, self.player.y - 64)
            time.sleep(0.1)

        self.pyxel_manager.change_scene_outer_circle(level + 2, 4, 2, action=action)

    def update_main_menu(self):
        self.player_animation_menus.update()
        self.main_menu_title.update()
        self.main_menu_play_button.update()
        self.main_menu_credits_button.update()
        self.main_menu_quit_button.update()

    def draw_main_menu(self):
        pyxel.cls(16)

        pyxel.bltm(0, 0, 0, 0, 0, 288, 128, 0)
        pyxel.blt(88, wave_motion(70, 10, 2, pyxel.frame_count), 1, 0, 80, 8, 8, 0)
        pyxel.blt(184, wave_motion(70, 13, 2, pyxel.frame_count), 1, 0, 80, 8, 8, 0)
        self.player_animation_menus.draw(2*8, 7*8+1)

        self.main_menu_title.draw()
        self.main_menu_play_button.draw()
        self.main_menu_credits_button.draw()
        self.main_menu_quit_button.draw()

        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 0, 8, 8, 0)

    def update_credits(self):
        self.player_animation_menus.update()
        self.credits_text.update()
        self.credits_back_button.update()

    def draw_credits(self):
        pyxel.cls(16)

        pyxel.bltm(0, 0, 1, 0, 0, 228, 128, 0)
        pyxel.blt(7*8, wave_motion(10*8, 14, 1, pyxel.frame_count), 1, 32, 80, 8, 8, 0)
        pyxel.blt(3*8, wave_motion(4*8, 12, 1, pyxel.frame_count), 1, 32, 80, 8, 8, 0)
        pyxel.blt(21*8, wave_motion(7*8, 15, 1, pyxel.frame_count), 1, 40, 80, 8, 8, 0)
        pyxel.blt(16*8, wave_motion(7*8, 14, 1, pyxel.frame_count), 1, 24, 81, 7, 7, 0)
        pyxel.blt(14*8, wave_motion(7*8, 14, 1, pyxel.frame_count), 1, 17, 80, 6, 8, 0)
        self.player_animation_menus.draw(4*8, 10*8+1)

        self.credits_text.draw()
        self.credits_back_button.draw()

        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 0, 8, 8, 0)

    def update_level_selection(self):
        self.player_animation_menus.update()
        self.level_selection_title.update()
        self.level_selection_back_button.update()
        for i in range(1, 22):
            eval(f"self.level_selection_button_{i}.update()")

    def draw_level_selection(self):
        pyxel.cls(16)

        pyxel.bltm(0, 0, 2, 0, 0, 228, 128, 0)
        pyxel.blt(20*8, wave_motion(14*8, 14, 1, pyxel.frame_count), 1, 17, 80, 6, 8, 0)
        pyxel.blt(24.5*8, wave_motion(10*8, 12, 1, pyxel.frame_count), 1, 17, 80, 6, 8, 0)
        pyxel.blt(24.5*8, wave_motion(6*8, 13, 1, pyxel.frame_count), 1, 1, 80, 6, 8, 0)
        pyxel.blt(20*8, wave_motion(4*8, 15, 1, pyxel.frame_count), 1, 1, 80, 6, 8, 0)
        pyxel.blt(17*8, wave_motion(4*8, 12, 1, pyxel.frame_count), 1, 24, 81, 7, 7, 0)
        self.player_animation_menus.draw(8*8, 14*8+1)

        self.level_selection_title.draw()
        self.level_selection_back_button.draw()
        for i in range(1, 22):
            eval(f"self.level_selection_button_{i}.draw()")

        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 0, 0, 0, 8, 8, 0)


    def update_level(self, level:int):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.play(0, 0)
            self.color_level_selection_buttons()
            self.pyxel_manager.change_scene_dither(2, 0.05, 2, action=lambda:time.sleep(0.1))
            return

        if self.player.dead and not self.player.player_death.is_finished():
            self.pyxel_manager.apply_palette_effect(grayscaled_palette)

        if pyxel.btnp(pyxel.KEY_R) or self.player.player_death.is_finished():
            self.level_buttons_action(level)
            return
        
        if self.player.player_win.is_finished():
            pyxel.play(0, 0)
            self.max_level = max(self.max_level, level)
            self.level_buttons_action(level + 1)
            return

        self.player.update()
        if self.player.is_breaking:
            self.pyxel_manager.shake_camera(10, 0.5)
        self.gem_manager.update(self.player)
        self.pyxel_manager.move_camera(self.player.x - 114, self.player.y - 64)

        if level == 1:
            if pyxel.btnp(pyxel.KEY_E) and self.player.tilemap.collision_tile_coord(self.player.x, self.player.y, self.player.width, self.player.height, 21, 30) and not self.dialog_manager.is_dialog():
                self.dialog_manager.start_dialog(self.dialog_1)
            elif pyxel.btnp(pyxel.KEY_E) and self.player.tilemap.collision_tile_coord(self.player.x, self.player.y, self.player.width, self.player.height, 50, 38) and not self.dialog_manager.is_dialog():
                self.dialog_manager.start_dialog(self.dialog_2)
        elif level == 2:
            if pyxel.btnp(pyxel.KEY_E) and self.player.tilemap.collision_tile_coord(self.player.x, self.player.y, self.player.width, self.player.height, 21, 30) and not self.dialog_manager.is_dialog():
                self.dialog_manager.start_dialog(self.dialog_3)
            elif pyxel.btnp(pyxel.KEY_E) and self.player.tilemap.collision_tile_coord(self.player.x, self.player.y, self.player.width, self.player.height, 43, 22) and not self.dialog_manager.is_dialog():
                self.dialog_manager.start_dialog(self.dialog_4)
        elif level == 3:
            if pyxel.btnp(pyxel.KEY_E) and self.player.tilemap.collision_tile_coord(self.player.x, self.player.y, self.player.width, self.player.height, 20, 30) and not self.dialog_manager.is_dialog():
                self.dialog_manager.start_dialog(self.dialog_5)
            elif pyxel.btnp(pyxel.KEY_E) and self.player.tilemap.collision_tile_coord(self.player.x, self.player.y, self.player.width, self.player.height, 37, 30) and not self.dialog_manager.is_dialog():
                self.dialog_manager.start_dialog(self.dialog_6)
        elif level == 4:
            if pyxel.btnp(pyxel.KEY_E) and self.player.tilemap.collision_tile_coord(self.player.x, self.player.y, self.player.width, self.player.height, 26, 15) and not self.dialog_manager.is_dialog():
                self.dialog_manager.start_dialog(self.dialog_7)

        self.dialog_manager.update()

    def draw_level(self, level:int):
        pyxel.cls(16)

        self.tilemap.draw()
        self.gem_manager.draw()
        if self.player.win and not self.player.player_win.is_finished():
            draw_moving_spiral(self.player.x + 3, self.player.y + 3, 10, 14, pyxel.frame_count, 3, 200, 0.15)
        self.player.draw(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y)
        self.dialog_manager.draw(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y)

        pyxel.text(self.pyxel_manager.camera_x + 226 - len(f"Level {level}") * 4, self.pyxel_manager.camera_y + 2, f"Level {level}", 1)

#? Main
if __name__ == "__main__":
    Game()