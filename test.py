import random
import pyxel

TILES = {
    (14,1):{"chance":0.3, "tiles":[(2,6),(2,7),(3,6),(3,7),(4,6),(5,6)], "weights":[0.25, 0.25, 0.25, 0.25, 0.1, 0.1], "off":(0,-1), "tilemaps":[0,1]},
    (10,1):{"chance":0.2, "tiles":[(2,6),(2,7),(3,6),(3,7),(4,6),(5,6)], "weights":[0.25, 0.25, 0.25, 0.25, 0.1, 0.1], "off":(0,-1), "tilemaps":[0,1]},

    (12,1):{"chance":0.25, "tiles":[(2,6),(2,7),(3,7)], "weights":[0.33, 0.33, 0.33], "off":(0,-1), "tilemaps":[0,1]},
    (8,1):{"chance":0.1, "tiles":[(2,6),(2,7),(3,7)], "weights":[0.33, 0.33, 0.33], "off":(0,-1), "tilemaps":[0,1]},

    (6,1):{"chance":0.25, "tiles":[(2,6),(3,7)], "weights":[0.5, 0.5], "off":(0,-1), "tilemaps":[0,1]},
    (2,1):{"chance":0.1, "tiles":[(2,6),(3,7)], "weights":[0.5, 0.5], "off":(0,-1), "tilemaps":[0,1]},

    (4,1):{"chance":0.1, "tiles":[(2,6),(3,7)], "weights":[0.5, 0.5], "off":(0,-1), "tilemaps":[0,1]},
    (0,1):{"chance":0.1, "tiles":[(2,6),(3,7)], "weights":[0.5, 0.5], "off":(0,-1), "tilemaps":[0,1]},
}

pyxel.init(64, 64)

pyxel.load("assets.pyxres")

for tx in range(pyxel.tilemaps[0].width):
    for ty in range(pyxel.tilemaps[0].height):
        tile = pyxel.tilemaps[0].pget(tx, ty)
        if tile in TILES.keys():
            if random.random() < TILES[tile]["chance"]:
                new_tile = random.choices(TILES[tile]["tiles"], TILES[tile]["weights"])[0]
                new_tilemap = random.choice(TILES[tile]["tilemaps"])
                ox, oy = TILES[tile]["off"]
                if pyxel.tilemaps[0].pget(tx + ox, ty + oy) == (0,0) and pyxel.tilemaps[1].pget(tx + ox, ty + oy) == (0,0):
                    pyxel.tilemaps[new_tilemap].pset(tx + ox, ty + oy, new_tile)

pyxel.save("assets2.pyxres")