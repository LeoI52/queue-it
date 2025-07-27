"""
@author : Léo IMBERT & Eddy MONGIN
@created : 14/05/2025
@updated : 27/07/2025

* Gems Types :
- Green : Jump Gem
- Yellow : Build Gem
- Pink : Phase Gem
- Blue : Dash Gem
- Red : Gravity Gem
- Grey : Breaking Gem

* Pyxres Files :
1.pyxres : Main menu, Credits, Level Selection, Level 1, Level 2, Level 3, Level 4, level 5

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
from world import *
from utils import *
import pyxel
import time

#? Constants
FPS = 60
PALETTE = [0x000000, 0xE6E1CC, 0x2E1B37, 0xB49A8D, 0xFFDBAC, 0xA45A41, 0xCF4F4F, 0xD87E46, 0xEDD15A, 0x7DA446, 0x3A7E4C, 0x28524E, 0x7394BA, 0x4E53A2, 0x8C315D, 0xF6788D, 0x4E9FE5]

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

        scenes = [main_menu_scene, credits_scene, level_selection_scene, level_1_scene, level_2_scene, level_3_scene, level_4_scene, level_5_scene]

        #? Pyxel Manager
        self.pyxel_manager = PyxelManager(228, 128, scenes, 0, FPS, True, False, pyxel.KEY_A)

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
        self.level_selection_button_6 = Button("6 ", 154, 46, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_7 = Button("7 ", 174, 46, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_8 = Button("8 ", 54, 66, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
        self.level_selection_button_9 = Button("9 ", 74, 66, 6, 8, 7, 8, 1, True, 8, anchor=ANCHOR_TOP)
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
        self.dialog_7 = Dialog([
            ("Sign", "Well done ! You've mastered the\ngem queue."),
            ("Sign", "Remember : gems are used in the\norder they appear."),
            ("Sign", "Think ahead, plan your queue,\nand adapt on the fly."),
            ("Sign", "Good luck - the real challenge\nbegins now !")], 0, 1, 1, True, 1, True, 0, 10)

        #? Levels Variables
        self.tilemap = None
        self.player: Player = None
        self.gem_manager = None
        self.dialog_manager = DialogManager(5, -50, 5, 5, 118, 50, 3, pyxel.KEY_E)

        # self.setup_music()

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

    def menu_buttons_action(self, scene_id:int):
        pyxel.play(0, 0)
        self.pyxel_manager.change_scene_dither(scene_id, 0.05, 2, action=lambda:time.sleep(0.1))

    def level_buttons_action(self, level:int):
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

            self.gem_manager = GemManager(self.tilemap.load_tiles())
            self.pyxel_manager.set_camera(self.player.x - 114, self.player.y - 64)
            time.sleep(0.1)

        self.pyxel_manager.change_scene_dither(level + 2, 0.05, 2, action=action)


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
            self.pyxel_manager.change_scene_dither(0, 0.05, 2, action=lambda:time.sleep(0.1))
            return

        if self.player.dead and not self.player.player_death.is_finished():
            self.pyxel_manager.apply_palette_effect(grayscaled_palette)

        if pyxel.btnp(pyxel.KEY_R) or self.player.player_death.is_finished():
            self.level_buttons_action(level)
            return
        
        if self.player.player_win.is_finished():
            pyxel.play(0, 0)
            self.pyxel_manager.change_scene_outer_circle(2, 4, 2, action=lambda:time.sleep(0.1))
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

#? Main
if __name__ == "__main__":
    Game()