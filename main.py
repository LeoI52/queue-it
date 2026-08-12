"""
@author : Léo Imbert
@created : 14/05/2025
@updated : 12/08/2026
"""

#? ---------- IMPORTATIONS ---------- ?#

from copy import deepcopy
from utils import *

#? ---------- CONSTANTS ---------- ?#

PALETTE = [0x3b78ad, 0x2E1B37, 0x353658, 0x83769C, 0xB49A8D, 0xc5cddb, 0xE6E1CC, 0x5ee9e9, 
           0x7394BA, 0x4E53A2, 0x053239, 0x005f41, 0x08b23b, 0x47f641, 0xe8ff75, 0xfbbe82, 
           0xde9751, 0xb66831, 0x8a4926, 0x461c14, 0x1e090d, 0x720d0d, 0x813704, 0xda2424, 
           0xef6e10, 0xecab11, 0xece910, 0xf78d8d, 0xf94e6d, 0xc12458, 0x841252, 0x3d083b, 0x000000]

COLLISION_TILES = zone(0,1,31,1) + [(0,8),(1,8)]

KILL_TILES = zone(0,4,3,4)

DOOR_TILES = [(0,7),(1,6)]

BREAK_TILES = [(0,8),(1,8)]

JUMP_GEM = 0
DASH_GEM = 1
PHASE_GEM = 2
GRAVITY_GEM = 3
BUILD_GEM = 4
BREAK_GEM = 5

GEM_COLORS_DICT = {
    JUMP_GEM:[11,12,13],
    DASH_GEM:[8,9],
    PHASE_GEM:[27,28],
    GRAVITY_GEM:[21,23],
    BUILD_GEM:[24,25,26],
    BREAK_GEM:[2,3,5],
}

SPECIAL_TILES_DICT = {
    #? id replace type
    (0,5):[(0,0),JUMP_GEM],
    (1,5):[(0,0),DASH_GEM],
    (2,5):[(0,0),PHASE_GEM],
    (3,5):[(0,0),GRAVITY_GEM],
    (4,5):[(0,0),BUILD_GEM],
    (5,5):[(0,0),BREAK_GEM],
}

DOORS_DICT = {
    #? pos id pos text

    #? 0
    (13,13):[2,(78,20),"Level Selection"],(19,13):[1,(53,21),"Credits"],
    #? 1
    (54,21):[0,(20,13),"Main Menu"],
    #? 2
    (77,20):[0,(14,13),"Main Menu"],(82,20):[3,(114,17),"Level 1"],(86,20):[4,(150,5),"Level 2"],(90,20):[5,(187,10),"Level 3"],
    (94,20):[6,(224,13),"Level 4"],(98,20):[7,(258,14),"Level 5"],(98,15):[8,(5,36),"Level 6"],(94,15):[9,(53,36),"Level 7"],(90,15):[10,(93,34),"Level 8"],
    (86,15):[11,(113,30),"Level 9"],(82,15):[12,(163,43),"Level 10"],(82,10):[13,(192,28),"Level 11"],(86,10):[14,(224,43),"Level 12"],(90,10):[15,(260,35),"Level 13"],
    (94,10):[16,(13,53),"Level 14"],(98,10):[17,(41,67),"Level 15"],(98,5):[18,(90,64),"Level 16"],(94,5):[19,(115,53),"Level 17"],(90,5):[20,(151,63),"Level 18"],
    (86,5):[21,(193,51),"Level 19"],(82,5):[22,(228,60),"Level 20"],
    #? 3
    (113,17):[2,(83,20),"Level Selection"],(140,14):[4,(150,5),"Level 2"],
    #? 4
    (149,5):[2,(87,20),"Level Selection"],(152,15):[5,(187,10),"Level 3"],
    #? 5
    (186,10):[2,(91,20),"Level Selection"],(184,18):[6,(224,13),"Level 4"],
    #? 6
    (225,13):[2,(95,20),"Level Selection"],(235,17):[7,(258,14),"Level 5"],
    #? 7
    (257,14):[2,(99,20),"Level Selection"],(284,14):[8,(5,36),"Level 6"],
    #? 8
    (4,36):[2,(97,15),"Level Selection"],(31,34):[9,(53,36),"Level 7"],
    #? 9
    (54,36):[2,(93,15),"Level Selection"],(54,39):[10,(93,34),"Level 8"],
    #? 10
    (94,34):[2,(89,15),"Level Selection"],(98,34):[11,(113,30),"Level 9"],
    #? 11
    (112,30):[2,(85,15),"Level Selection"],(140,36):[12,(163,43),"Level 10"],
    #? 12
    (162,43):[2,(81,15),"Level Selection"],(162,31):[13,(192,28),"Level 11"],
    #? 13
    (191,28):[2,(83,10),"Level Selection"],(203,42):[14,(224,43),"Level 12"],
    #? 14
    (223,43):[2,(87,10),"Level Selection"],(242,33):[15,(260,35),"Level 13"],
    #? 15
    (259,35):[2,(91,10),"Level Selection"],(281,33):[16,(13,53),"Level 14"],
    #? 16
    (12,53):[2,(95,10),"Level Selection"],(30,51):[17,(41,67),"Level 15"],
    #? 17
    (40,67):[2,(99,10),"Level Selection"],(60,55):[18,(90,64),"Level 16"],
    #? 18
    (89,64):[2,(97,5),"Level Selection"],(79,52):[19,(115,53),"Level 17"],
    #? 19
    (114,53):[2,(93,5),"Level Selection"],(124,57):[20,(151,63),"Level 18"],
    #? 20
    (150,63):[2,(89,5),"Level Selection"],(175,57):[21,(193,51),"Level 19"],
    #? 21
    (192,51):[2,(85,5),"Level Selection"],(192,54):[22,(228,60),"Level 20"],
    #? 22
    (226,60):[2,(81,5),"Level Selection"],(241,52):[23,(270,47),"The End"],
    #? 23
    (270,64):[0,(16,12),"Main Menu"],
}

DIALOG_1 = Dialog([("Sign","Welcome to Queue It!"),("Sign","You can move with Q/D or use the left\ngamepad joystick."),("Sign","If you are blocked restart the level\nwith R or the top gamepad button."),("Sign","You can interact with objects by\npressing E or the left gamepad button."),("Sign", "In this game gems go into a queue.\nPress Space or the bottom gamepad\nbutton to use the oldest one first."),("Sign","Each gem gives you a different power,\ngo ahead try the green one.")], 32, 12, 12, True, 12)
DIALOG_2 = Dialog([("Sign","The blue gem allows you to dash."),("Sign","During that dash, you are invincible.\nGreat for going through spikes."),("Sign","But you can't change direction while\ndashing, so be careful.")], 32, 9, 9, True, 9)
DIALOG_3 = Dialog([("Sign","The pink gem gives you the power to\nphase upward."),("Sign","The phasing is always exactly 4 tiles.\nIf you can't phase there, you can't\nuse the gem.")], 32, 28, 28, True, 28)
DIALOG_4 = Dialog([("Sign","The red gem reverse your gravity."),("Sign","While reversed you jump and phase in\nthe opposite vertical direction.")], 32, 23, 23, True, 23)
DIALOG_5 = Dialog([("Sign","Here you can see breakable blocks.\nThe gray gem can destroy them !"),("Sign","Be careful because the radius isn't\ninfinite.")], 32, 3, 3, True, 3)
DIALOG_6 = Dialog([("Sign","Finally, the yellow gem helps you build\nunderneath your feet."),("Sign","Giving you a nice platform made of\nbreakable tiles.")], 32, 25, 25, True, 25)

DIALOGS_DICT = {
    (116,17):DIALOG_1,
    (152,5):DIALOG_2,
    (223,13):DIALOG_3,
    (56,36):DIALOG_4,
    (92,34):DIALOG_5,
    (114,30):DIALOG_6,
}

#? ---------- CLASSES ---------- ?#

class Player:

    def __init__(self, pyxel_manager:PyxelManager, particle_manager:ParticleManager):
        self.x, self.y = 16 * 8, 12 * 8
        self.w, self.h = 6, 8

        #? Others
        self.gems = []
        self.pyxel_manager = pyxel_manager
        self.particle_manager = particle_manager

        #? Checkpoint
        self.checkpoint_x, self.checkpoint_y = self.x, self.y

        #? Animations
        self.player_idle = Animation(Sprite(0, 0, 8, 6, 8, 0), 2, 20, True)
        self.player_walk = Animation(Sprite(0, 0, 16, 6, 8, 0), 5, 10, True)
        self.player_death = Animation(Sprite(0, 0, 24, 6, 8, 0), 5, 15, False)

        #? Velocity
        self.vx = 0
        self.vxr = 0
        self.vy = 0
        self.vyr = 0
        self.max_vy = 5
        self.gravity = 0.37
        self.crouch_gravity = 0.6

        #? Movement
        self.acc = 0.4
        self.deacc = 0.5
        self.speed = 1.2
        self.cobweb_speed = 0.2

        #? Jump
        self.coyote_timer = 0
        self.coyote_time = 6
        self.jump_power = 5

        #? Dash
        self.dash_timer = 0
        self.dash_time = 6
        self.dash_power = 4.5

        #? Phase
        self.phase_timer = 0
        self.phase_time = 6

        #? Gravity
        self.gravity_dir = 1

        #? Flares
        self.facing_right = True
        self.on_ground = False
        self.jumping = False
        self.death = False
        self.free = False

    def reset(self):
        self.gravity_dir = 1
        self.dash_timer = 0
        self.phase_timer = 0
        self.vx, self.vy = 0, 0
        self.vxr, self.vyr = 0, 0

    def load(self, x:int, y:int, gems:list):
        self.x, self.y = x, y
        self.checkpoint_x, self.checkpoint_y = x, y
        self.death = False
        self.reset()
        self.player_death.reset()
        self.gems = deepcopy(gems)

    def use_gem(self, gem:int):
        particle = False

        if gem == JUMP_GEM:
            can_jump = (self.on_ground or self.coyote_timer > 0) and not self.jumping
        
            if can_jump:
                self.gems.pop(0)
                particle = True
                self.vy = -self.jump_power * self.gravity_dir
                self.vyr = 0
                self.jumping = True
                self.coyote_timer = 0

        elif gem == DASH_GEM:
            self.gems.pop(0)
            particle = True
            self.dash_timer = self.dash_time

        elif gem == PHASE_GEM:
            if not collision_rect_tiles(self.x, self.y - 32 * self.gravity_dir, self.w, self.h, COLLISION_TILES):
                self.gems.pop(0)
                particle = True
                self.y -= 32 * self.gravity_dir
                self.phase_timer = self.phase_time
            else:
                particle = False

        elif gem == GRAVITY_GEM:
            self.gems.pop(0)
            particle = True
            self.gravity_dir *= -1

        elif gem == BUILD_GEM:
            if pyxel.tilemaps[0].pget(self.x // 8, self.y // 8 + 2 * self.gravity_dir) not in COLLISION_TILES:
                pyxel.tilemaps[0].pset(self.x // 8, self.y // 8 + 2 * self.gravity_dir, random.choice(BREAK_TILES))
                self.gems.pop(0)
                particle = True
            if pyxel.tilemaps[0].pget(self.x // 8 - 1, self.y // 8 + 2 * self.gravity_dir) not in COLLISION_TILES:
                pyxel.tilemaps[0].pset(self.x // 8 - 1, self.y // 8 + 2 * self.gravity_dir, random.choice(BREAK_TILES))
                if not particle:
                    particle = True
                    self.gems.pop(0)
            if pyxel.tilemaps[0].pget(self.x // 8 + 1, self.y // 8 + 2 * self.gravity_dir) not in COLLISION_TILES:
                pyxel.tilemaps[0].pset(self.x // 8 + 1, self.y // 8 + 2 * self.gravity_dir, random.choice(BREAK_TILES))
                if not particle:
                    particle = True
                    self.gems.pop(0)

        elif gem == BREAK_GEM:
            particle = True
            self.gems.pop(0)
            tiles = replace_tiles(self.x, self.y, self.w, self.h, 16, BREAK_TILES, (0,0))
            for tile_x, tile_y in tiles:
                for _ in range(10):
                    x, y = tile_x * 8 + 4, tile_y * 8 + 4
                    tx, ty = x + random.randint(-3,3), y + random.randint(-3,3)
                    c = [random.choice([17,18]) for _ in range(3)]
                    self.particle_manager.add_particle(LineParticle(x, y, random.randint(2,4), c, 60, random.uniform(0.4, 0.8), (tx, ty), acceleration=(0, 0.02), dither_duration=10))
            self.pyxel_manager.shake_camera(2, 0.1)

        if not particle:
            return

        for _ in range(10):
            c = [random.choice(GEM_COLORS_DICT[gem]) for _ in range(3)]
            size = random.randint(1, 2)
            x = random.randint(self.x - 2, self.x + 8)
            y = self.y + self.h if self.gravity_dir == 1 else self.y
            self.particle_manager.add_particle(OvalParticle(x, y, size, size, c, 100, random.uniform(0.08, 0.25), (x, y - self.gravity_dir), dither_duration=10))

    def die(self):
        if self.free:
            return
        self.death = True

        self.pyxel_manager.shake_camera(3, 0.2)

    def _handle_free_movement(self):
        if left():
            self.x -= 2
        if right():
            self.x += 2
        if up():
            self.y -= 2
        if down():
            self.y += 2

    def _handle_death(self):
        if collision_rect_tiles(self.x + 1, self.y + 2, 6, 5, KILL_TILES):
            self.die()

    def _handle_on_ground(self):
        self.on_ground = collision_rect_tiles(self.x, self.y + 1 * self.gravity_dir, self.w, self.h, COLLISION_TILES)

        if self.on_ground:
            if not self.jumping:
                self.vy = 0
            self.jumping = False
            self.coyote_timer = self.coyote_time

    def _handle_movement(self):
        speed = self.speed
        if self.gravity_dir == 1:
            self.vy = min(self.vy + self.gravity, self.max_vy)
        else:
            self.vy = max(self.vy - self.gravity, -self.max_vy)

        if left() and self.vx > -speed:
            self.vx = max(self.vx - self.acc, -speed)
            self.facing_right = False
        elif right() and self.vx < speed:
            self.vx = min(self.vx + self.acc, speed)
            self.facing_right = True
        else:
            if self.vx > 0:
                self.vx = max(0, self.vx - self.deacc)
            elif self.vx < 0:
                self.vx = min(0, self.vx + self.deacc)

    def _handle_gems(self):
        if use() and len(self.gems) > 0:
            self.use_gem(self.gems[0].type)

    def _update_velocity_x(self):
        if self.vx == 0:
            return

        self.vx += self.vxr
        self.vxr = self.vx - int(self.vx)
        self.vx -= self.vxr
        step_x = 1 if self.vx > 0 else -1
        for _ in range(int(abs(self.vx))):
            if not collision_rect_tiles(self.x + step_x, self.y, self.w, self.h, COLLISION_TILES):
                self.x += step_x
            else:
                self.vx = 0
                break

    def _update_velocity_y(self):
        max_vy = self.max_vy
        self.vy = pyxel.clamp(self.vy, -max_vy, max_vy)
        if self.vy == 0:
            return
        
        self.vy += self.vyr
        self.vyr = self.vy - int(self.vy)
        self.vy -= self.vyr
        step_y = 1 if self.vy > 0 else -1
        for _ in range(int(abs(self.vy))):
            if not collision_rect_tiles(self.x, self.y + step_y, self.w, self.h, COLLISION_TILES):
                self.y += step_y
            else:
                self.vy = 0
                break

    def update(self):
        if pyxel.btnp(pyxel.KEY_F) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_B):
            self.free = not self.free

        if self.free:
            self._handle_free_movement()
            return
        
        if self.death:
            self.player_death.update()
            return
        
        if self.dash_timer > 0 or self.phase_timer > 0:
            if self.dash_timer > 0:
                self.vx = self.dash_power if self.facing_right else -self.dash_power
                self._update_velocity_x()

            self.vy = 0
            self.dash_timer = max(0, self.dash_timer - 1)
            self.phase_timer = max(0, self.phase_timer - 1)
            self._handle_gems()
            return

        self._handle_death()
        self._handle_on_ground()
        self._handle_movement()
        self._handle_gems()

        self.player_idle.update()
        self.player_walk.update()

        self._update_velocity_x()
        self._update_velocity_y()
    
    def draw(self):
        for anim in [self.player_idle, self.player_walk, self.player_death]:
            anim.sprite.flip_horizontal = not self.facing_right
            anim.sprite.flip_vertical = False if self.gravity_dir == 1 else True

        if self.death:
            self.player_death.draw(self.x, self.y)
        elif -1 < self.vx < 1 and self.on_ground:
            self.player_idle.draw(self.x, self.y)
        elif self.on_ground:
            self.player_walk.draw(self.x, self.y)
        else:
            pyxel.blt(self.x, self.y, 0, 0, 8, self.w * (1 if self.facing_right else -1), self.h * self.gravity_dir, 0)

        for index, gem in enumerate(self.gems):
            pyxel.blt(self.pyxel_manager.camera_x + 2 + 9 * index, self.pyxel_manager.camera_y + 2, 1, gem.u, gem.v, gem.w, gem.h, 0)

class Gem:

    def __init__(self, type:int, x:int=0, y:int=0):
        self.x = x
        self.y = y
        self.type = type
        self.u, self.v, self.w, self.h = type * 8, 40, 8, 8
        self.wave_speed = random.uniform(0.5, 2)
        self.collected = False

class GemManager:

    def __init__(self, gems:list):
        self.gems = deepcopy(gems)

    def update(self, player:Player):
        for gem in self.gems:
            if collision_rect_rect(player.x + 1, player.y + 1, player.w - 2, player.h - 2, gem.x, gem.y, gem.w, gem.h) and not gem.collected:
                player.gems.append(gem)
                gem.collected = True

        self.gems = [gem for gem in self.gems if not gem.collected]

    def draw(self):
        for gem in self.gems:
            pyxel.blt(gem.x, wave_motion(gem.y, 1, gem.wave_speed, pyxel.frame_count), 1, gem.u, gem.v, gem.w, gem.h, 0)

class CloudManager:

    COULDS_DICT = {
        #? u v w h
        0:[0,40,19,7],
        1:[0,48,18,8],
        2:[24,40,14,6],
        3:[24,48,20,9],
    }

    def __init__(self):
        #? x y type speed size
        self.reset()

    def reset(self):
        self.clouds = []
        for _ in range(5):
            type = random.randint(0,3)
            _, _, w, h = self.COULDS_DICT[type]
            s = random.uniform(0.8, 1.5)

            self.clouds.append([random.randint(0, pyxel.width - round(w * s)), random.randint(0, 64), type, random.uniform(0.2, 0.5), s])

    def update(self):
        if random.random() < 0.005 and len(self.clouds) < 10:
            type = random.randint(0,3)
            _, _, w, h = self.COULDS_DICT[type]
            s = random.uniform(0.8, 1.5)

            self.clouds.append([0 - w * s, random.randint(0, 64), type, random.uniform(0.2, 0.5), s])

        for i in range(len(self.clouds)):
            self.clouds[i][0] += self.clouds[i][3]

        self.clouds = [cloud for cloud in self.clouds if cloud[0] < pyxel.width]

    def draw(self, camera_x:int, camera_y:int):
        for x, y, type, _, s in self.clouds:
            u, v, w, h = self.COULDS_DICT[type]
            pyxel.blt(camera_x + x, camera_y + y, 0, u, v, w, h, 0, scale=s)

#? ---------- FUNCTIONS ---------- ?#

def collision_rect_tiles(x:int, y:int, w:int, h:int, tiles:list, tilemaps:int|list=0)-> bool:
    tilemaps = [tilemaps] if isinstance(tilemaps, int) else tilemaps
    tilemap_w, tilemap_h = pyxel.tilemaps[tilemaps[0]].width, pyxel.tilemaps[tilemaps[0]].height

    start_tile_x = int(pyxel.clamp(x // 8, 0, tilemap_w - 1))
    start_tile_y = int(pyxel.clamp(y // 8, 0, tilemap_h - 1))
    end_tile_x = int(pyxel.clamp((x + w - 1) // 8, 0, tilemap_w - 1))
    end_tile_y = int(pyxel.clamp((y + h - 1) // 8, 0, tilemap_h - 1))

    for tile_y in range(start_tile_y, end_tile_y + 1):
        for tile_x in range(start_tile_x, end_tile_x + 1):
            for tilemap_id in tilemaps:
                tile_id = pyxel.tilemaps[tilemap_id].pget(tile_x, tile_y)

                if tile_id in tiles:
                    return True
    
    return False

def tiles_in_rect(x:int, y:int, w:int, h:int, tiles:list, tilemaps:int|list=0)-> list:
    result = []
    tilemaps = [tilemaps] if isinstance(tilemaps, int) else tilemaps
    tilemap_w, tilemap_h = pyxel.tilemaps[tilemaps[0]].width, pyxel.tilemaps[tilemaps[0]].height

    start_tile_x = int(pyxel.clamp(x // 8, 0, tilemap_w - 1))
    start_tile_y = int(pyxel.clamp(y // 8, 0, tilemap_h - 1))
    end_tile_x = int(pyxel.clamp((x + w - 1) // 8, 0, tilemap_w - 1))
    end_tile_y = int(pyxel.clamp((y + h - 1) // 8, 0, tilemap_h - 1))

    for tile_y in range(start_tile_y, end_tile_y + 1):
        for tile_x in range(start_tile_x, end_tile_x + 1):
            for tilemap_id in tilemaps:
                tile_id = pyxel.tilemaps[tilemap_id].pget(tile_x, tile_y)

                if tile_id in tiles:
                    result.append((tile_x, tile_y))

    return result

def replace_tiles(x:int, y:int, w:int, h:int, radius:int, tiles:list, replace_tile:tuple)-> list:
    start_tile_x = int(pyxel.clamp((x - radius) // 8, 0, pyxel.tilemaps[0].width - 1))
    start_tile_y = int(pyxel.clamp((y - radius) // 8, 0, pyxel.tilemaps[0].height - 1))
    end_tile_x = int(pyxel.clamp((x + w + radius - 1) // 8, 0, pyxel.tilemaps[0].width - 1))
    end_tile_y = int(pyxel.clamp((y + h + radius - 1) // 8, 0, pyxel.tilemaps[0].height - 1))

    l = []
    for tile_y in range(start_tile_y, end_tile_y + 1):
        for tile_x in range(start_tile_x, end_tile_x + 1):
            tile_id = pyxel.tilemaps[0].pget(tile_x, tile_y)

            if tile_id in tiles:
                l.append((tile_x, tile_y))
                pyxel.tilemaps[0].pset(tile_x, tile_y, replace_tile)
    return l

def left()-> bool:
    return pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT) or pyxel.btnv(pyxel.GAMEPAD1_AXIS_LEFTX) < -8000

def right()-> bool:
    return pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btnv(pyxel.GAMEPAD1_AXIS_LEFTX) > 8000

def up()-> bool:
    return pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_W) or pyxel.btn(pyxel.KEY_UP) or pyxel.btnv(pyxel.GAMEPAD1_AXIS_LEFTY) < -20000

def down()-> bool:
    return pyxel.btn(pyxel.KEY_S) or pyxel.btnv(pyxel.GAMEPAD1_AXIS_LEFTY) > 8000

def use()-> bool:
    return pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A)

def interact()-> bool:
    return pyxel.btnp(pyxel.KEY_E) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X)

def restart()-> bool:
    return pyxel.btnp(pyxel.KEY_R) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_Y)

def get_room_uv(id:int)-> tuple:
    u = (id % 8) * 36 + 1
    v = (id // 8) * 23 + 1
    return u * 8, v * 8

def load_gems(u:int, v:int)-> list:
    l = []
    for tx in range(pyxel.width // 8):
        for ty in range(pyxel.height // 8):
            tile = pyxel.tilemaps[1].pget(u + tx, v + ty)
            if tile in SPECIAL_TILES_DICT.keys():
                replace, type = SPECIAL_TILES_DICT[tile]
                pyxel.tilemaps[1].pset(u + tx, v + ty, replace)
                l.append(Gem(type, (u + tx) * 8, (v + ty) * 8))
    return l
 
#? ---------- CONSTANTS ---------- ?#

LEVEL_GEMS_DICT = {
    7:[Gem(JUMP_GEM)],
    8:[Gem(PHASE_GEM)],
    9:[Gem(JUMP_GEM), Gem(DASH_GEM)],
    10:[Gem(JUMP_GEM), Gem(JUMP_GEM), Gem(DASH_GEM)],
    12:[Gem(PHASE_GEM) for _ in range(2)],
    13:[Gem(BUILD_GEM)],
    14:[Gem(PHASE_GEM) for _ in range(4)],
    15:[Gem(GRAVITY_GEM) for _ in range(5)],
    17:[Gem(JUMP_GEM)],
    18:[Gem(JUMP_GEM) for _ in range(3)],
    19:[Gem(JUMP_GEM), Gem(BREAK_GEM)],
    20:[Gem(GRAVITY_GEM) for _ in range(2)],
    21:[Gem(BUILD_GEM)],
    22:[Gem(DASH_GEM)],
}

#? ---------- GAME ---------- ?#

class Game:

    def __init__(self):
        #? Scenes
        scenes = [
            Scene(0, "Queue It ! - Game", self.update_game, self.draw_game),
        ]

        #? Pyxel Manager
        self.pyxel_manager = PyxelManager((280, 176), scenes, 0, 60, True, False, "assets2.pyxres", PALETTE, camera_x=8, camera_y=8)

        #? Game Variables
        self.id = 0
        self.cloud_manager = CloudManager()
        self.particle_manager = ParticleManager()
        self.dialog_manager = DialogManager(10, 186, 10, 176 - 64 - 10, 260, 64)
        self.dialog = 0
        self.player = Player(self.pyxel_manager, self.particle_manager)
        self.interact_signs = []
        self.gem_manager = GemManager([])
        self.door_texts = []
        self.unlocked_levels = {0,1,2,3}

        #? Text
        self.title = Text("Queue It !", 140, 20, [24,24,25,25,26,26], FONT_DEFAULT, 3, TOP, (VERTICAL, ROTATING_COLOR_MODE, 20), outline_color=1, relative=True)
        self.credits = Text("Credits", 140, 20, [24,24,25,25,26,26], FONT_DEFAULT, 3, TOP, (VERTICAL, ROTATING_COLOR_MODE, 20), outline_color=1, relative=True)
        self.credits_text = Text(wrap_text_width("This game was made by Léo Imbert.", 200, 1, FONT_DEFAULT), 140, 64, 26, FONT_DEFAULT, 1, TOP, outline_color=1, relative=True)
        self.end = Text("The End !", 140, 20, [24,24,25,25,26,26], FONT_DEFAULT, 3, TOP, (VERTICAL, ROTATING_COLOR_MODE, 20), outline_color=1, relative=True)

        #? Music
        pyxel.sounds[0].pcm("sounds/music.wav")
        pyxel.channels[0].gain = 0.5
        pyxel.play(0, 0, loop=True)

        #? Run
        self.pyxel_manager.run()

    def load_level(self, id, player_pos):
        def act():
            self.id = id
            self.unlocked_levels.add(id)
            self.pyxel_manager.set_camera(*get_room_uv(id))
            u, v = get_room_uv(id)
            pyxel.load("assets2.pyxres", exclude_sounds=True, exclude_musics=True)
            self.gem_manager = GemManager(load_gems(u // 8, v // 8))
            self.particle_manager.reset()
            self.cloud_manager.reset()
            self.player.load(*player_pos, LEVEL_GEMS_DICT.get(id, []))
        self.pyxel_manager.change_scene_transition(TransitionDiagonal(0, 1, 32, action=act))

    def update_game(self):
        if self.id == 0:    self.title.update()
        if self.id == 1:    self.credits.update();self.credits_text.update()
        if self.id == 23:   self.end.update()

        if self.dialog == -1:
            self.dialog = 0

        self.cloud_manager.update()
        self.particle_manager.update()
        self.dialog_manager.update()
        if not self.dialog_manager.is_dialog():
            if self.dialog == 1:
                self.dialog = -1
            self.player.update()

        self.gem_manager.update(self.player)

        if (restart() and self.id not in [0,1,2]) or self.player.player_death.is_finished():
            self.load_level(self.id, (self.player.checkpoint_x, self.player.checkpoint_y))

        tiles = tiles_in_rect(self.player.x, self.player.y, self.player.w, self.player.h, DOOR_TILES)
        self.door_texts = []
        if tiles:
            id, pos, text = DOORS_DICT[tiles[0]]
            self.door_texts.append((text, tiles[0][0], tiles[0][1]))

            if up() or interact():
                if not self.id == 2 or id <= max(self.unlocked_levels):
                    pos = (pos[0]*8, pos[1]*8)
                    self.load_level(id, pos)

        self.interact_signs = tiles_in_rect(self.player.x - 8, self.player.y - 8, self.player.w + 16, self.player.h + 16, [(6,6)])
        if self.interact_signs and interact() and self.dialog == 0:
            self.dialog = 1
            self.dialog_manager.start_dialog(DIALOGS_DICT[self.interact_signs[0]])

        if self.id in [0, 1, 2] and not self.player.gems:
            self.player.gems = [Gem(JUMP_GEM, 0, 0)]

    def draw_game(self):
        #? Background
        pyxel.cls(0)
        self.cloud_manager.draw(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y)

        #? Interactables
        for tile_x, tile_y in self.interact_signs:
            x, y = tile_x * 8, tile_y * 8
            u, v = pyxel.tilemaps[0].pget(tile_x, tile_y)
            for i in range(33):
                pyxel.pal(i, 6)
            for ox, oy in [(-1,0), (1,0), (0,-1), (0,1)]:
                pyxel.blt(x + ox, y + oy, 1, u * 8, v * 8, 8, 8, 0)
            pyxel.pal()
            pyxel.blt(x, y, 1, u * 8, v * 8, 8, 8, 0)

        #? Tilemap
        u, v = get_room_uv(self.id)
        pyxel.bltm(u, v, 0, u, v, 280, 176, 0)

        #? Player
        self.gem_manager.draw()
        self.player.draw()
        self.particle_manager.draw()

        #? Tilemap
        u, v = get_room_uv(self.id)
        pyxel.bltm(u, v, 1, u, v, 280, 176, 0)

        #? Door Text
        for text, tx, ty in self.door_texts:
            x, y = tx * 8 + 4, ty * 8 - 4
            c = 6
            if self.id == 2 and text[-1].isdigit():
                level = int(text.split()[-1])
                c = 6 if level + 2 in self.unlocked_levels else 23
            Text(text, x, y, c, FONT_PYXEL, anchor=BOTTOM, shadow=(1,1,1)).draw()

        #? Dialog Manager
        self.dialog_manager.draw(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y)

        #? Text
        if self.id not in [0,1,2,23]:
            Text(f"Level {self.id - 2}", 278, 2, 6, FONT_PYXEL, anchor=TOP_RIGHT, shadow=(1,1,1), relative=True).draw(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y)
        if self.id == 0:    self.title.draw(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y)
        if self.id == 1:    self.credits.draw(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y);self.credits_text.draw(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y)
        if self.id == 23:   self.end.draw(self.pyxel_manager.camera_x, self.pyxel_manager.camera_y)

#? ---------- MAIN ---------- ?#

if __name__ == "__main__":
    Game()