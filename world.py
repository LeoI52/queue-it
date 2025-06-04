"""
@author : Léo IMBERT & Eddy MONGIN
@created : 14/05/2025
@updated : 17/05/2025
"""

from copy import deepcopy
from utils import *
import pyxel

COLLISION_TILES = [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),
                   (0,2),(1,2),(2,2),(3,2),
                   (0,3),(1,3),(2,3),(3,3),
                   (0,4),(1,4),(2,4),(3,4)]

KILL_TILES = [(0,7),(1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7)]

DOOR_TILES = [(0,8),(1,8),(0,9),(1,9)]

BREAKING_TILES = [(4,1),(5,1)]

JUMP_GEM = 0
PHASE_GEM = 1
DASH_GEM = 2
GRAVITY_GEM = 3
BREAKING_GEM = 4

GEM_COLORS_DICT = {
    JUMP_GEM : [9, 10, 11],
    PHASE_GEM : [1, 15],
    DASH_GEM : [12, 13],
    GRAVITY_GEM : [6, 14],
    BREAKING_GEM : [3, 4]
}

GEMS_DICT = {
    JUMP_GEM : (1, 80, 6, 8),
    PHASE_GEM : (17, 80, 6, 8),
    DASH_GEM : (24, 81, 7, 7),
    GRAVITY_GEM : (32, 80, 8, 8),
    BREAKING_GEM : (40, 80, 8, 8)
}

SPECIAL_TILES_DICT = {
    (0, 10) : [(0, 0), JUMP_GEM],
    (2, 10) : [(0, 0), PHASE_GEM],
    (3, 10) : [(0, 0), DASH_GEM],
    (4, 10) : [(0, 0), GRAVITY_GEM],
    (5, 10) : [(0, 0), BREAKING_GEM]
}

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

                    if object_type in [JUMP_GEM, PHASE_GEM, DASH_GEM, GRAVITY_GEM, BREAKING_GEM]:
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
        elif gem == PHASE_GEM:
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
        elif gem == BREAKING_GEM:
            pyxel.play(1, 4)
            self.gems.pop(0)
            self.tilemap.replace_tiles(self.x, self.y, self.width, self.height, 4, BREAKING_TILES, (0, 0))
            self.is_breaking = True
        
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

        if self.gravity_direction == 1 and (self.tilemap.collision_rect_tiles(self.x, self.y - 3, self.width, self.height, KILL_TILES) and self.velocity_y >= 0 and not self.dead) or (self.tilemap.collision_rect_tiles(self.x, self.y + 3, self.width, self.height, KILL_TILES) and self.velocity_y < -1 and not self.dead):
            pyxel.play(1, 7)
            self.dead = True
        elif self.gravity_direction == -1 and (self.tilemap.collision_rect_tiles(self.x, self.y + 3, self.width, self.height, KILL_TILES) and self.velocity_y > 0 and not self.dead) or (self.tilemap.collision_rect_tiles(self.x, self.y - 3, self.width, self.height, KILL_TILES) and self.velocity_y <= -1 and not self.dead):
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

        if pyxel.btn(pyxel.KEY_LEFT):
            self.velocity_x = max(self.velocity_x - self.speed, -self.max_velocity_x)
            self.facing_right = False
        if pyxel.btn(pyxel.KEY_RIGHT):
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
        if self.facing_right:
            self.player_idle.unflip_h()
            self.player_walk.unflip_h()
            self.player_death.unflip_h()
            self.player_win.unflip_h()
        else:
            self.player_idle.flip_h()
            self.player_walk.flip_h()
            self.player_death.flip_h()
            self.player_win.flip_h()

        if self.gravity_direction == 1:
            self.player_idle.unflip_v()
            self.player_walk.unflip_v()
            self.player_death.unflip_v()
            self.player_win.unflip_v()
        else:
            self.player_idle.flip_v()
            self.player_walk.flip_v()
            self.player_death.flip_v()
            self.player_win.flip_v()

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
