import pygame
import os
import random
import csv
import button
from pygame import mixer
from pygame.locals import *
from Particle import Particles
import sys

flags = HWSURFACE
pygame.display.init()
pygame.font.init()
pygame.init()
mixer.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
FPS = 25
fullscreen = False
shiftx = 0
shifty = 0

screen_info = pygame.display.Info()
FULL_SCREEN_WIDTH = screen_info.current_w
FULL_SCREEN_HEIGHT = screen_info.current_h
aux_width = 0
aux_height = 0

# define game variables
GRAVITY = 0.8
SCROLL_TRESH = 300
screen_scroll = 0
bg_scroll = 0
ROWS = 16
COLUMNS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 30

season = 1
level = 4
lvls_unlocked = []
load_wrld = 0
start_game = False
show_levels = False
start_intro = False
MAX_LEVELS = 8
settings_screen = False
particles_on = False
particles = []
hurt_timer = 0
b_count = 0
info_counter = 0
text = []
circle_width = 300
fb = False
shield_activate_timer = 0
shield = False
shield_timer = 0
s = pygame.sprite.Sprite()
ver = 0
d = 1
fire = False
final_anim = False
final_anim_timer = 300
on_ground = False
tunnel = False
button_activated = 0
healthBoost = False
health_counter = 0
pick_up_box = False
drop_box = False
player_appearance = False
end = False
end_count = 0
end_fade = False
with open('levelsUnlocked.txt') as file:
    reader = file.read()
lvls_unlocked = reader.split(' ')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, 16)

pygame.display.set_caption('PIXEL RUN')

# define player action variables
moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False

# load music and sounds
MAX_VOLUME = 0.5
MUSIC_VOLUME = 0.5
SFX_VOLUME = 0.5
music_width = 500
sfx_width = 500
pygame.mixer.music.load('audio/music2.mp3')
pygame.mixer.music.set_volume(MUSIC_VOLUME)
end_music = pygame.mixer.Sound('audio/Victory.mp3')
end_music.set_volume(MUSIC_VOLUME)
pygame.mixer.music.play(-1, 0.0, 5000)
explosion = pygame.mixer.Sound('audio/grenade.wav')
explosion.set_volume(1)
win_fx = pygame.mixer.Sound('audio/win.mp3')
win_fx.set_volume(SFX_VOLUME)
fb_sfx = pygame.mixer.Sound('audio/FB.mp3')
fb_sfx.set_volume(1)
heal_fx = pygame.mixer.Sound('audio/Heal.mp3')
heal_fx.set_volume(SFX_VOLUME )
revive_fx = pygame.mixer.Sound('audio/Revive.mp3')
revive_fx.set_volume(SFX_VOLUME )
coin_fx = pygame.mixer.Sound('audio/coin.wav')
coin_fx.set_volume(SFX_VOLUME )
jump_fx = pygame.mixer.Sound('audio/jump.wav')
jump_fx.set_volume(SFX_VOLUME)
shot_fx = pygame.mixer.Sound('audio/shot.wav')
shot_fx.set_volume(SFX_VOLUME)
grenade_fx = pygame.mixer.Sound('audio/grenade.wav')
grenade_fx.set_volume(SFX_VOLUME)
# load images
PINE1_IMG = pygame.image.load('img/background/pine1.png').convert_alpha()
PINE2_IMG = pygame.image.load('img/background/pine2.png').convert_alpha()
MOUNTAIN_IMG = pygame.image.load('img/background/mountain.png').convert_alpha()
SKY_IMG = pygame.image.load('img/background/sky_cloud.png').convert_alpha()
SETTINGS_IMG = pygame.image.load('img/New Piskel.png').convert_alpha()
# button images
A_BUTTON = pygame.image.load('img/ActivationButton.png').convert_alpha()
START_IMG = pygame.image.load('img/start_btn.png').convert_alpha()
EXIT_IMG = pygame.transform.scale(pygame.image.load('img/exit_btn.png').convert_alpha(),
                                  (START_IMG.get_width(), START_IMG.get_height()))
RESTART_IMG = pygame.image.load('img/restart_btn.png').convert_alpha()
BG_IMG = pygame.image.load('img/bg.png').convert_alpha()
HURT_IMG = pygame.transform.scale(pygame.image.load('img/hurt.png'),(TILE_SIZE,TILE_SIZE)).convert_alpha()
COIN_IMG = pygame.image.load('img/coin/coin1.png').convert_alpha()
info_img_list = []
i = pygame.image.load('img/info2.png').convert_alpha()
INFO_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.4), int(i.get_height() * 0.4)))
i = pygame.image.load('img/info.png').convert_alpha()
INFO2_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.4), int(i.get_height() * 0.4)))
i = pygame.image.load('img/infotext1.png').convert_alpha()
INFO3_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.8), int(i.get_height() * 0.8)))
i = pygame.image.load('img/infotext2.png').convert_alpha()
INFO4_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.9), int(i.get_height() * 0.9)))
i = pygame.image.load('img/infotext3.png').convert_alpha()
INFO5_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.9), int(i.get_height() * 0.9)))
i = pygame.image.load('img/infotext4.png').convert_alpha()
INFO6_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.9), int(i.get_height() * 0.9)))
i = pygame.image.load('img/infotext5.png').convert_alpha()
INFO7_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.9), int(i.get_height() * 0.9)))
i = pygame.image.load('img/infotext6.png').convert_alpha()
INFO8_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.9), int(i.get_height() * 0.9)))
i = pygame.image.load('img/infotext8.png').convert_alpha()
INFO9_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.9), int(i.get_height() * 0.9)))
i = pygame.image.load('img/infotext7.png').convert_alpha()
INF10_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.9), int(i.get_height() * 0.9)))
i = pygame.image.load('img/infotext9.png').convert_alpha()
INF11_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.9), int(i.get_height() * 0.9)))
i = pygame.image.load('img/infotext10.png').convert_alpha()
INF12_IMG = pygame.transform.scale(i, (int(i.get_width() * 0.9), int(i.get_height() * 0.9)))
temp = []
temp.append(INFO2_IMG)
temp.append(INFO_IMG)
temp.append(INFO3_IMG)
info_img_list.append(temp)
temp = []
temp.append(INFO4_IMG)
temp.append(INFO5_IMG)
temp.append(INFO6_IMG)
info_img_list.append(temp)
temp = []
temp.append(INFO7_IMG)
temp.append(INFO8_IMG)
info_img_list.append(temp)
temp = []
info_img_list.append(temp)
temp = []
temp.append(INFO9_IMG)
temp.append(INF10_IMG)
info_img_list.append(temp)
temp = []
temp.append(INF11_IMG)
temp.append(INF12_IMG)
info_img_list.append(temp)

shieldimg = pygame.image.load('img/shield.png').convert_alpha()
SHIELD_IMG = pygame.transform.scale(shieldimg, (shieldimg.get_width() // 4, shieldimg.get_height() // 4))
pine1_img = pygame.image.load('img/Background/pine1.png').convert_alpha()
pine2_img = pygame.image.load('img/Background/pine2.png').convert_alpha()
mountain_img = pygame.image.load('img/Background/mountain.png').convert_alpha()
sky_img = pygame.image.load('img/Background/sky_cloud.png').convert_alpha()
BG_ICE = pygame.transform.scale(pygame.image.load('img/BGICE.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
h = pygame.image.load('img/HealthShield.png').convert_alpha()
HEALTH_BOOST = pygame.transform.scale(h, (h.get_width() // 3, h.get_height() // 3))
BOX_IMG = pygame.transform.scale(pygame.image.load('img/tiles/0/12.png').convert_alpha(), (TILE_SIZE, TILE_SIZE))
lvl = pygame.image.load('img/LvlBox.png').convert_alpha()
LVL_BOX = pygame.transform.scale(pygame.image.load('img/LvlBox.png').convert_alpha(),
                                 (lvl.get_width() // 3, lvl.get_height() // 3))
ctrlimg = pygame.image.load('img/controls3.png').convert_alpha()
CONTROLS_IMG = pygame.transform.scale(ctrlimg, (int(ctrlimg.get_width() / 1.2), int(ctrlimg.get_height() / 1.2)))

appearance_imgs = []
for i in range(3,9):
    img = pygame.transform.scale2x(pygame.image.load(f'img/appearance/5.png').convert_alpha())
    img = pygame.transform.scale(img,(int(img.get_width()/(i*0.9)),int(img.get_height()/(i*0.9))))
    appearance_imgs.append(img)



lvl_images = []
for i in range(1, 9):
    img = pygame.image.load(f'img/lvl_imgs/{i}.png').convert_alpha()
    LVL = pygame.transform.scale(img, (int(SCREEN_WIDTH / 1.42), int(SCREEN_HEIGHT / 2.53)))
    lvl_images.append(LVL)

current_level_image = lvl_images[0]
current_level_selected = 0
# store tiles in a list
img_list = []
img_list0 = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/tiles/0/{x}.png').convert_alpha()
    # img.set_alpha(80)

    if x == 23:
        img = pygame.transform.scale(img, (TILE_SIZE - 7, TILE_SIZE - 7))
    else:
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list0.append(img)
img_list.append(img_list0)
img_list1 = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/tiles/1/{x}.png').convert_alpha()
    # img.set_alpha(80)

    if x == 23 or x == 24:
        img = pygame.transform.scale(img, (TILE_SIZE - 7, TILE_SIZE - 7))
    else:
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list1.append(img)
img_list.append(img_list1)
img_list2 = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/tiles/2/{x}.png').convert_alpha()
    # img.set_alpha(80)

    if x == 23:
        img = pygame.transform.scale(img, (TILE_SIZE - 7, TILE_SIZE - 7))
    else:
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list2.append(img)
img_list.append(img_list2)
BULLET_IMG = pygame.image.load('img/icons/bullet.png').convert_alpha()
GRENADE_IMG = pygame.image.load('img/icons/grenade.png').convert_alpha()
HEALTH_BOX_IMG = pygame.image.load('img/icons/health_box.png').convert_alpha()
AMMO_BOX_IMG = pygame.image.load('img/icons/ammo_box.png').convert_alpha()
GRENADE_BOX_IMG = pygame.image.load('img/icons/grenade_box.png').convert_alpha()
item_boxes = {
    'Health': HEALTH_BOX_IMG,
    'Ammo': AMMO_BOX_IMG,
    'Grenade': GRENADE_BOX_IMG
}
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
BLACK2 = (0, 0, 0, 100)
PINK = (235, 65, 54)
TRANSPARENT = (0, 0, 0, 0)
BLUE = (130, 181, 210)

font = pygame.font.Font('Futura Bold font.ttf', int(SCREEN_HEIGHT / 26.66) - 5)
font2 = pygame.font.Font('Futura Bold font.ttf', int(SCREEN_HEIGHT / 8) - 5)
font3 = pygame.font.Font('Futura Bold font.ttf', int(SCREEN_HEIGHT / 16) - 5)
PixelFont = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 26.66))
PixelFont6 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 25))
PixelFont2 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 5))
PixelFont3 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 4.93))
PixelFont4 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 11.42))
PixelFont5 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 11.11))
PixelFont7 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 20))


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


lvl_buttons = []
# level boxes menu load images
for i in range(1, 9):
    if i <= 4:
        b = button.Button(shiftx + 120 + (LVL_BOX.get_width() + 120) * (i - 1), shifty +
                          40 + LVL_BOX.get_height(), LVL_BOX, 1)
        lvl_buttons.append(b)

    else:
        b = button.Button(shiftx + 120 + (LVL_BOX.get_width() + 120) * (i - 5), shifty +
                          40 + LVL_BOX.get_height() + 500, LVL_BOX, 1)
        # screen.blit(LVL_BOX, (120 + (LVL_BOX.get_width() + 120) * (i - 5), 40 + LVL_BOX.get_height() + 500))
        lvl_buttons.append(b)


def init_program():
    global lvl_buttons, FULL_SCREEN_WIDTH, SCREEN_WIDTH, font, font2, font3, PixelFont, PixelFont5, PixelFont4, PixelFont3, PixelFont2, PixelFont6, shiftx, shifty, start_button, restart_button, exit_button, settings_button
    font = pygame.font.Font('Futura Bold font.ttf', int(SCREEN_HEIGHT / 26.66) - 5)
    font2 = pygame.font.Font('Futura Bold font.ttf', int(SCREEN_HEIGHT / 8) - 5)
    font3 = pygame.font.Font('Futura Bold font.ttf', int(SCREEN_HEIGHT / 16) - 5)
    PixelFont = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 26.66))
    PixelFont6 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 22))
    PixelFont2 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 5))
    PixelFont3 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 4.93))
    PixelFont4 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 11.42))
    PixelFont5 = pygame.font.Font('ARCADECLASSIC.TTF', int(SCREEN_HEIGHT / 11.11))

    # level boxes menu load images
    lvl_buttons.clear()
    # level boxes menu load images
    if fullscreen:
        for i in range(1, 9):
            if i <= 4:
                b = button.Button(200 + (FULL_SCREEN_WIDTH - 600) // 3 * (i - 1), shifty -
                                  55 + LVL_BOX.get_height(), LVL_BOX, 1)
                lvl_buttons.append(b)

            else:
                b = button.Button(200 + (FULL_SCREEN_WIDTH - 600) // 3 * (i - 5), shifty +
                                  60 + LVL_BOX.get_height() + 500, LVL_BOX, 1)
                # screen.blit(LVL_BOX, (120 + (LVL_BOX.get_width() + 120) * (i - 5), 40 + LVL_BOX.get_height() + 500))
                lvl_buttons.append(b)
    else:
        for i in range(1, 9):
            if i <= 4:
                b = button.Button(shiftx + 120 + (LVL_BOX.get_width() + 120) * (i - 1), shifty +
                                  40 + LVL_BOX.get_height(), LVL_BOX, 1)
                lvl_buttons.append(b)

            else:
                b = button.Button(shiftx + 120 + (LVL_BOX.get_width() + 120) * (i - 5), shifty +
                                  40 + LVL_BOX.get_height() + 500, LVL_BOX, 1)
                # screen.blit(LVL_BOX, (120 + (LVL_BOX.get_width() + 120) * (i - 5), 40 + LVL_BOX.get_height() + 500))
                lvl_buttons.append(b)

        # create buttons
    start_button = button.Button(shiftx + SCREEN_WIDTH // 2 - 130, shifty + SCREEN_HEIGHT // 2 - 100, START_IMG, 1)
    exit_button = button.Button(shiftx + SCREEN_WIDTH // 2 - 130, shifty + SCREEN_HEIGHT // 2 + 100, EXIT_IMG, 1)
    restart_button = button.Button(shiftx + SCREEN_WIDTH // 2 - 100, shifty + SCREEN_HEIGHT // 2 - 50, RESTART_IMG, 2)

    if fullscreen:
        settings_button = button.Button(FULL_SCREEN_WIDTH - 100, 0, SETTINGS_IMG, 3)
    else:
        settings_button = button.Button(shiftx + SCREEN_WIDTH - 100, 0, SETTINGS_IMG, 3)


def draw_bg():
    global settings_screen
    screen.fill(BG)
    # for x in range(5):
    #     screen.blit(SKY_IMG,(x * SKY_IMG.get_width()-bg_scroll * 0.5,0))
    #     screen.blit(MOUNTAIN_IMG,(x * SKY_IMG.get_width()-bg_scroll * 0.6,SCREEN_HEIGHT - MOUNTAIN_IMG.get_height() - 300))
    #     screen.blit(PINE1_IMG,(x * SKY_IMG.get_width()-bg_scroll * 0.7,SCREEN_HEIGHT - PINE1_IMG.get_height() - 150))
    #     screen.blit(PINE2_IMG,(x * SKY_IMG.get_width()-bg_scroll * 0.8,SCREEN_HEIGHT - PINE2_IMG.get_height()))
    for x in range(70):
        for y in range(10):
            screen.blit(BG_IMG, (x * BG_IMG.get_width() - bg_scroll, y * BG_IMG.get_height()))
    if not settings_screen:
        BRICK = pygame.transform.scale(pygame.image.load('img/tiles/0/4.png'), (TILE_SIZE, TILE_SIZE)).convert_alpha()
        nr = 10
        start = 800
        for x in range(180):
            if x >= 150:
                nr = 26
                start = 0
            for y in range(nr):
                screen.blit(BRICK, (x * BRICK.get_width() - bg_scroll, y * BRICK.get_height() + start))


def draw_bg2():
    screen.fill(BLUE)
    width = sky_img.get_width()
    for x in range(5):
        screen.blit(sky_img, ((x * width) - bg_scroll * 0.5, 0))
        if not start_game and fullscreen or (settings_screen and fullscreen) or (end and fullscreen):
            screen.blit(mountain_img,
                        ((x * width) - bg_scroll * 0.6, FULL_SCREEN_HEIGHT - mountain_img.get_height() - 300))
            screen.blit(pine1_img, ((x * width) - bg_scroll * 0.7, FULL_SCREEN_HEIGHT - pine1_img.get_height() - 150))
            screen.blit(pine2_img, ((x * width) - bg_scroll * 0.8, FULL_SCREEN_HEIGHT - pine2_img.get_height()))
        else:
            screen.blit(mountain_img, ((x * width) - bg_scroll * 0.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
            screen.blit(pine1_img, ((x * width) - bg_scroll * 0.7, SCREEN_HEIGHT - pine1_img.get_height() - 150))
            screen.blit(pine2_img, ((x * width) - bg_scroll * 0.8, SCREEN_HEIGHT - pine2_img.get_height()))
    if not settings_screen:
        BRICK = pygame.transform.scale(pygame.image.load('img/tiles/2/4.png'), (TILE_SIZE, TILE_SIZE)).convert_alpha()
        nr = 10
        start = 800
        if start_game and not settings_screen and not end:
            for x in range(180):
                if x >= 150:
                    nr = 26
                    start = 0
                for y in range(nr):
                    screen.blit(BRICK, (x * BRICK.get_width() - bg_scroll, y * BRICK.get_height() + start))


def draw_bg1():
    if fullscreen:
        BG_ICE = pygame.transform.scale(pygame.image.load('img/BGICE.png').convert_alpha(),
                                        (FULL_SCREEN_WIDTH, FULL_SCREEN_HEIGHT))
    else:
        BG_ICE = pygame.transform.scale(pygame.image.load('img/BGICE.png').convert_alpha(),
                                        (SCREEN_WIDTH, SCREEN_HEIGHT))
    width = BG_ICE.get_width()
    for x in range(8):
        screen.blit(BG_ICE, (x * width - bg_scroll * 0.5, 0))
    if not settings_screen:
        BRICK = pygame.transform.scale(pygame.image.load('img/tiles/1/4.png'), (TILE_SIZE, TILE_SIZE)).convert_alpha()
        nr = 10
        start = 800
        for x in range(180):
            if x >= 150:
                nr = 26
                start = 0
            for y in range(nr):
                screen.blit(BRICK, (x * BRICK.get_width() - bg_scroll, y * BRICK.get_height() + start))


# function to reset level
def reset_level():
    global ver, info_counter,player_appearance
    enemy_group.empty()
    bullet_group.empty()
    grenade_group.empty()
    explosion_group.empty()
    item_box_group.empty()
    decoration_group.empty()
    water_group.empty()
    exit_group.empty()
    coin_group.empty()
    light_group.empty()
    box_group.empty()
    act_buttons.empty()
    movingTilegroup.empty()
    infoBoxGroup.empty()

    info_counter = 0
    player_appearance = False
    # create empty tile list
    data = []
    for row in range(ROWS):
        r = [-1] * COLUMNS
        data.append(r)

    return data


class Appearance:
    def __init__(self, delta_time, appearance_imgs):
        self.imgs = appearance_imgs
        self.delta_time = delta_time
        self.index = 0
        self.time = self.delta_time
        self.rect = pygame.Rect(0,0,0,0)

    def draw(self):
        global player_appearance
        my_img = self.imgs[self.index]
        screen.blit(my_img, (player.rect.x - (my_img.get_width()//2) ,player.rect.bottom - (my_img.get_height()//2)))
        if self.time < 0:
            self.time = self.delta_time
            if self.index < 5:
                self.index += 1

            else:
                self.index = 0
                player_appearance = False
        self.time -= 1.7





class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades):
        pygame.sprite.Sprite.__init__(self)
        self.boxes = 0
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.coins = 0
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.grenades = grenades
        self.health = 100
        self.max_health = self.health
        self.direction = 1
        self.jump = False
        self.megajump = False
        self.in_air = True
        self.vel_y = 0
        self.update_time = pygame.time.get_ticks()
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        # create AI characters
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.idling = False
        self.idling_counter = 0
        self.mega_air = False
        self.died = False
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            temp_list = []
            # count number of files in a folder
            num_of_frames = len(os.listdir(f'img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.draw_time = 10

    def update(self):
        self.update_animation()
        # update_cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
        self.check_alive()

    def move(self, moving_left, moving_right):
        global on_ground
        screen_scroll = 0
        dx = 0
        dy = 0
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if self.jump and self.in_air == False:
            self.vel_y = -13
            self.jump = False
            self.in_air = True

        if self.megajump and self.in_air == False:
            if self.coins >= 10:
                jump_fx.play()
                self.vel_y = -22
                self.megajump = False
                self.in_air = True
                self.coins -= 10
                self.mega_air = True
            else:
                self.draw_time -= 1
                draw_text('You need 10 coins to activate the megajump!', font, WHITE, 300, 100)
                if self.draw_time <= 0:
                    self.draw_time = 10

                    self.megajump = False

        # apply Gravity
        self.vel_y += GRAVITY
        if self.vel_y >= 10:
            self.vel_y = 10

        dy += self.vel_y

        # check for collision
        for tile in world.obstacle_list:
            # check collision in the x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
                # if ai has hit the wall make it turn around
                if self.char_type == 'enemy':
                    self.direction *= -1
                    self.move_counter = 0
            # check collision in the y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if bellow the ground,ex jumping
                global on_ground
                on_ground = True
                if self.vel_y < 0:
                    self.vel_y = 0

                    dy = tile[1].bottom - self.rect.top
                # check if above the ground,ex falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    self.in_air = False
                    dy = tile[1].top - self.rect.bottom

        # check for collision with water
        if pygame.sprite.spritecollide(self, water_group, False) and not shield and player.vel_y > 0:
            self.health = 0
        # check for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_group, False):
            level_complete = True
        # check if falling off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0
        # CHECK IF GOING OFF THE EDGES OF THE SCREEN
        if self.char_type == 'player':
            if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
                dx = 0

        self.rect.x += dx

        if pygame.sprite.spritecollide(self, movingTilegroup, False):
            dy = 0

        # if jumping off boxes does not work,jump twice ,or more times,to get out of the boxes
        # if pygame.sprite.spritecollide(player, box_group, False) and self.in_air == True and self.vel_y>0:
        #     dy = 0
        # box = pygame.sprite.spritecollide(player, box_group, False)
        # if box:
        #     pygame.draw.rect(screen,RED,box[0].rect,3)
        #     pygame.draw.rect(screen,RED,player.rect,3)
        #     pygame.display.update()
        #     if box[0].rect.top <= player.rect.bottom and not on_ground:
        #         print(str(box[0].rect.top) + '--' + str(player.rect.bottom))
        #         dy = 0
        box = pygame.sprite.spritecollide(player, box_group, False)
        if box:
            # pygame.draw.rect(screen,RED,box[0].rect,3)
            # pygame.draw.rect(screen,RED,player.rect,3)
            # pygame.display.update()
            # print(str(box[0].rect.top) + '--' + str(player.rect.bottom))
            for b in box:
                dif = player.rect.bottom - b.rect.top
                if dif >= 4 and dif <= 11:
                    dy = 0

        self.rect.y += dy

        global fullscreen

        # update scroll based on player position
        if self.char_type == 'player':
            if fullscreen:
                if (
                        self.rect.right >= FULL_SCREEN_WIDTH - SCROLL_TRESH and bg_scroll < world.level_length * TILE_SIZE - FULL_SCREEN_WIDTH) or (
                        self.rect.left < SCROLL_TRESH and bg_scroll > abs(dx)):
                    self.rect.x -= dx
                    screen_scroll = -dx
            else:
                if (
                        self.rect.right >= SCREEN_WIDTH - SCROLL_TRESH and bg_scroll < world.level_length * TILE_SIZE - SCREEN_WIDTH) or (
                        self.rect.left < SCROLL_TRESH and bg_scroll > abs(dx)):
                    self.rect.x -= dx
                    screen_scroll = -dx

        return screen_scroll, level_complete

    def shoot(self):
        global shield
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 8
            if shield:
                bullet = Bullet(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction + 50 * self.direction),
                                self.rect.y + self.rect.height // 2, self.direction)
            else:
                bullet = Bullet(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction),
                                self.rect.y + self.rect.height // 2, self.direction)
            bullet_group.add(bullet)
            self.ammo -= 1
            shot_fx.play()

    def ai(self):
        if self.alive and player.alive:
            if random.randint(1, 200) == 5 and self.idling == False:
                self.update_action(0)
                self.idling = True
                self.idling_counter = 50
                # check if the ai is near the player
            if self.vision.colliderect(player.rect):
                # stop running and face player
                self.update_action(0)
                self.shoot()


            elif self.idling == False:

                if self.direction == 1:
                    ai_moving_right = True
                else:
                    ai_moving_right = False
                ai_moving_left = not ai_moving_right
                self.move(ai_moving_left, ai_moving_right)
                self.update_action(1)
                self.move_counter += 1
                # update ai vision as the enemies move
                self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)
                # pygame.draw.rect(screen,RED,self.vision,3)

                if self.move_counter > TILE_SIZE - 10:
                    self.direction *= -1
                    self.move_counter *= -1
            else:
                self.idling_counter -= 1
                self.move(False, False)
                if self.idling_counter <= 0:
                    self.idling = False
        elif self.alive == False and player.alive == True:
            self.move(False, False)
        self.rect.x += screen_scroll

    def update_animation(self):
        if self.action == 3 and self.char_type == 'enemy' and self.frame_index < 7:
            draw_text(' +5 ', font3, BLACK, self.rect.x + 20, self.rect.y - 30)
        if self.action == 2 and self.mega_air:
            if self.in_air:
                draw_text(' -10 ', font3, BLACK, self.rect.x, self.rect.y - 60)
            else:
                self.mega_air = False

        ANIMATION_COOLDOWN = 100
        # update image depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action different to the previous one
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            if self.char_type == 'enemy' and self.died == False:
                self.died = True
                player.coins += 5
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


class World():
    def __init__(self):
        self.obstacle_list = []
        self.level_length = 0
        self.temp_obstacles = []

    def process_data(self, data):

        global season
        # print(season)
        # iterate through each value in level data file
        global info_counter
        self.level_length = len(data[0])
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[season][tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE - bg_scroll
                    img_rect.y = y * TILE_SIZE

                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 9 and tile <= 10:
                        water = Water(img, x * TILE_SIZE - bg_scroll, y * TILE_SIZE)
                        water_group.add(water)
                    elif tile == 14 or tile == 13 or tile == 11:
                        decoration = []
                        if season == 1 or season == 2:
                            if (tile == 14):
                                decoration = Decoration(img, x * TILE_SIZE - bg_scroll - 10, y * TILE_SIZE + 17)
                            elif tile == 11:
                                decoration = Decoration(img, x * TILE_SIZE - bg_scroll - 10, y * TILE_SIZE)
                        else:
                            decoration = Decoration(img, x * TILE_SIZE - bg_scroll, y * TILE_SIZE)
                        decoration_group.add(decoration)
                    elif tile == 12:
                        box = Box(img, x * TILE_SIZE - bg_scroll, y * TILE_SIZE)
                        box_group.add(box)

                    elif tile == 15:
                        # for test purposes use the Soldier in comments because he has 3x speed of a normal Soldier
                        # player = Soldier('player', x * TILE_SIZE- bg_scroll, y * TILE_SIZE, 1.35, 15, 20, 5)
                        player = Soldier('player', x * TILE_SIZE - bg_scroll, y * TILE_SIZE, 1.35, 5, 20, 5)
                        health_bar = HealthBar(10, 10, player.health, player.health)
                    elif tile == 16:
                        enemy = Soldier('enemy', x * TILE_SIZE - bg_scroll, y * TILE_SIZE, 1.35, 2, 20, 0)
                        enemy_group.add(enemy)
                    elif tile == 17:
                        item_box2 = ItemBox('Ammo', x * TILE_SIZE - bg_scroll, y * TILE_SIZE)
                        item_box_group.add(item_box2)
                    elif tile == 18:
                        item_box2 = ItemBox('Grenade', x * TILE_SIZE - bg_scroll, y * TILE_SIZE)
                        item_box_group.add(item_box2)
                    elif tile == 19:
                        item_box = ItemBox('Health', x * TILE_SIZE - bg_scroll, y * TILE_SIZE)
                        item_box_group.add(item_box)
                    elif tile == 20:
                        exit = Exit(img, x * TILE_SIZE - bg_scroll, y * TILE_SIZE)
                        exit_group.add(exit)
                    elif tile == 21:

                        infoBox = InfoBox(img, x * TILE_SIZE - bg_scroll + 15, y * TILE_SIZE,
                                          info_img_list[level - 1][info_counter])
                        info_counter += 1

                        infoBoxGroup.add(infoBox)
                    elif tile == 22:
                        water = Water(img, x * TILE_SIZE - bg_scroll, y * TILE_SIZE)
                        water_group.add(water)
                    elif tile == 23:
                        coin = Coin(x * TILE_SIZE - bg_scroll, y * TILE_SIZE)
                        coin_group.add(coin)
                    elif tile == 24:
                        if level >= 1 and level <= 3:
                            Light = Lights(img, x * TILE_SIZE - bg_scroll, y * TILE_SIZE + 20)
                            light_group.add(Light)
                        elif level >= 4 and level <= 6:
                            deco = Decoration(img, x * TILE_SIZE - bg_scroll + 10, y * TILE_SIZE + 20)
                            decoration_group.add(deco)
                        else:
                            deco = Decoration(img, x * TILE_SIZE - bg_scroll - 7, y * TILE_SIZE + 10)
                            decoration_group.add(deco)

                    elif tile == 25:
                        act_but = Activation_Button(img, x * TILE_SIZE + 25 - bg_scroll, y * TILE_SIZE + 25)
                        act_buttons.add(act_but)
                    elif tile == 27 or tile == 28 or tile == 29:
                        global d
                        if tile == 27:
                            d *= -1
                        movingTile = Moving_Tile(img, x * TILE_SIZE - bg_scroll, y * TILE_SIZE)
                        movingTile.speed *= d
                        movingTilegroup.add(movingTile)

        return player, health_bar

    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += screen_scroll
            screen.blit(tile[0], tile[1])


class Moving_Tile(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3

    def update(self):

        if self.rect.y + self.speed >= SCREEN_HEIGHT - 200:
            self.speed *= -1
        elif self.rect.y + self.speed <= 100:
            self.speed *= -1
        self.rect.y += self.speed
        self.rect.x += screen_scroll
        if self.rect.colliderect(player.rect):
            player.rect.y = self.rect.y - player.height
            player.vel_y = 0
            player.in_air = False
        for e in enemy_group:
            if self.rect.colliderect(e.rect):
                e.rect.y = self.rect.y - e.rect.height
                e.vel_y = 0
                e.in_air = False


class FireBall(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = []
        for x in range(1, 8):
            image = pygame.transform.scale(pygame.image.load(f'img/FireBall/FB{x}.png'), (148 , 68)).convert_alpha()
            self.imgs.append(image)
        self.index = 0
        self.img = self.imgs[self.index]
        self.rect = self.img.get_rect()
        r = random.randrange(-100, 100)
        self.rect.center = (10, player.rect.centery + r)
        self.speed = 50
        self.timer = 20

    def update(self):
        global fb,particles_on
        self.timer -= 1
        if self.timer < 0:
            if self.index < 6:
                self.index += 1
            else:
                self.index = 0
        self.img = self.imgs[self.index]
        self.rect.x += self.speed + screen_scroll
        if self.rect.colliderect(player.rect):
            explosion.play()
            particles_on = True
            global hurt_timer
            hurt_timer = 30
            player.health -= 20
            fb = False
            self.kill()
        if fullscreen:
            if self.rect.right >= FULL_SCREEN_WIDTH + 100:
                fb = False
                self.kill()
        elif self.rect.right >= SCREEN_WIDTH + 100:
            fb = False
            self.kill()

    def draw(self):
        global surface
        # surface1.fill([0, 0, 0, 0])
        # pygame.draw.circle(surface1, (0, 0, 0, 200), (self.rect.x, self.rect.y), 100)
        # screen.blit(surface1, (0, 0))

        screen.blit(self.img, (self.rect.x, self.rect.y))


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.coin_imgs = []
        for i in range(1, 7):
            image = pygame.image.load(f'img/coin/coin{i}.png').convert_alpha()
            pygame.transform.scale(image, (TILE_SIZE - 10, TILE_SIZE - 10))
            self.coin_imgs.append(image)
        self.index = 0
        self.image = self.coin_imgs[self.index]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + 20, y + TILE_SIZE)
        self.timer = 3

    def update(self):
        self.rect.x += screen_scroll
        self.timer -= 1
        if self.timer < 0:
            if self.index < 5:
                self.index += 1
            else:
                self.index = 0
            self.timer = 3

        if self.rect.colliderect(player.rect):
            player.coins += 1
            # print(player.coins)
            coin_fx.play()
            self.kill()
        self.image = self.coin_imgs[self.index]


class InfoBox(pygame.sprite.Sprite):
    def __init__(self, img, x, y, info_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y)
        self.info_img = info_img

    'Press D to move forward'

    def update(self):
        global fire
        self.rect.x += screen_scroll

        if player.rect.colliderect(self.rect):
            if level == 2:
                fire = True
            rect_info = pygame.Rect(SCREEN_WIDTH // 2 - self.info_img.get_width() // 2 - 50, 60,
                                    self.info_img.get_width() + 100, self.info_img.get_height() + 80)
            surface1 = screen.convert_alpha()
            surface1.fill([0, 0, 0, 0])
            pygame.draw.rect(surface1, (0, 0, 0, 230), rect_info)
            screen.blit(surface1, (0, 0))
            pygame.draw.rect(screen, WHITE, rect_info, 3)
            screen.blit(self.info_img, (SCREEN_WIDTH // 2 - self.info_img.get_width() // 2, 100))


class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class Box(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        global world, on_box
        move = True
        dx = 0
        dy = 0
        move = True
        tile_data = (self.image, self.rect)
        if self.rect.colliderect(player.rect):
            if pick_up_box:
                player.boxes += 1
                box_group.remove(self)
                self.kill()
            on_box = True
            if player.jump and player.in_air == False:
                player.vel_y = -13
                player.jump = False
                player.in_air = True
                player.update_action(1)
                player.rect.y -= 13
            # print(str(self.rect.top)+" -- " + str(player.rect.bottom))
            if player.in_air and player.vel_y > 0:

                player.vel_y = 0
                player.in_air = False
                player.update_action(0)

            else:

                for tile_data in world.obstacle_list:
                    if tile_data[1].colliderect(self.rect):
                        move = False
                dif = player.rect.bottom - self.rect.top
                # print(dif)
                if move and player.action == 1 and dif >= 50 and dif <= 60:

                    direction = 1
                    if player.rect.x > self.rect.x:
                        direction = -1
                    self.rect.x += player.speed * direction
                    my_box = self
                    box_group.remove(self)
                    if pygame.sprite.spritecollide(self, box_group, False):
                        current_box = self
                        for b in box_group:
                            if b.rect.colliderect(current_box.rect):
                                current_box = b
                                b.rect.x += player.speed * direction

                    box_group.add(my_box)
        else:
            on_box = False

        self.rect.x += screen_scroll


class Lights(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        global season
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))
        self.imgs = []
        if season == 0:
            for x in range(1, 5):
                img = pygame.image.load(f'img/Lights/light0{x}.png').convert_alpha()
                self.imgs.append(img)
            self.index = 0
            self.timer = 5
        else:
            self.image = img

    def update(self):
        global season
        self.rect.x += screen_scroll
        if season == 0:
            self.timer -= 1
            if self.timer <= 0:
                self.timer = 5
                if self.index < 3:
                    self.index += 1
                else:
                    self.index = 0
            self.image = self.imgs[self.index]


class Water(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class Exit(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll


class ItemBox(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item_type = item_type

        self.image = item_boxes[self.item_type]

        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + (TILE_SIZE - self.image.get_height()))

    def update(self):

        self.rect.x += screen_scroll
        if pygame.sprite.collide_rect(self, player):
            if self.item_type == 'Health':
                player.health += 25
                if player.health > player.max_health:
                    player.health = player.max_health
            elif self.item_type == 'Ammo':
                player.ammo += 15
            elif self.item_type == 'Grenade':
                player.grenades += 3
            self.kill()


class HealthBar():
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health

    def draw(self, health):
        global circle_width
        self.health = health
        if fullscreen:
            circle_width = 1250 + (100 - self.health) * 7
        else:
            circle_width = 300 + (100 - self.health) * 7
        ratio = self.health / self.max_health
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 154, 24))
        pygame.draw.rect(screen, RED, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 150 * ratio, 20))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = BULLET_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        global circle_width, s
        # move bullet
        self.rect.x += (self.direction * self.speed) + screen_scroll
        # check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH + 120:
            self.kill()
        # check for collision with level
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()
        if shield:
            try:
                if pygame.sprite.spritecollide(s, bullet_group, False):
                    self.kill()
            except:
                pass
        # check colision with characters
        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive and not shield:
                player.health -= 5
                self.kill()

        for enemy in enemy_group:
            if pygame.sprite.spritecollide(enemy, bullet_group, False):
                if enemy.alive:
                    enemy.health -= 25
                    self.kill()


class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = GRENADE_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):

        self.vel_y += GRAVITY
        dx = self.direction * self.speed
        dy = self.vel_y

        if self.rect.left + dx < 0 or self.rect.right + dx > SCREEN_WIDTH:
            self.direction *= -1
            dx = self.direction * self.speed
        # check collision with level
        for tile in world.obstacle_list:
            # check for colilison with walls
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                self.direction *= -1
                dx = self.direction * self.speed
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                self.speed = 0
                # check for collision on y axis
                # check if bellow the ground,ex thrown up
                if self.vel_y < 0:
                    self.vely = 0
                    dy = tile[1].bottom - self.rect.top
                # check if above the ground,ex falling
                elif self.vel_y >= 0:
                    self.vel_y = 0
                    dy = tile[1].top - self.rect.bottom

        self.rect.x += dx + screen_scroll
        self.rect.y += dy

        # countdown timer
        self.timer -= 1
        if self.timer <= 0:
            grenade_fx.play()
            self.kill()
            explosion = Explosion(self.rect.x, self.rect.y, 0.5)
            explosion_group.add(explosion)
            # do damage to anyone nearby
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE * 2 and abs(
                    self.rect.centery - player.rect.centery) < TILE_SIZE * 2:
                player.health -= 50
            for enemy in enemy_group:
                if abs(self.rect.centerx - enemy.rect.centerx) < TILE_SIZE * 2 and abs(
                        self.rect.centery - enemy.rect.centery) < TILE_SIZE * 2:
                    enemy.health -= 50


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 6):
            img = pygame.image.load(f'img/explosion/exp{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):

        self.rect.x += screen_scroll
        EXPLOSION_SPEED = 4
        # update explosion animation
        self.counter += 1
        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            if self.frame_index < len(self.images) - 1:
                self.frame_index += 1
            else:
                self.kill()

            self.image = self.images[self.frame_index]


class Shield(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = SHIELD_IMG.get_rect()
        self.rect.center = player.rect.center

    def draw(self):
        screen.blit(SHIELD_IMG, self.rect)

    def update(self):
        global shield_timer, fireball, fb, shield,particles_on
        shield_timer += 1
        self.rect.x += screen_scroll
        if shield_timer >= 70:
            player.coins -= 10
            shield_timer = 0

        draw_text(f'{7 - shield_timer // 10}:00', font, WHITE, self.rect.x + 45, self.rect.y - 25)
        if fb:
            if self.rect.colliderect(fireball.rect):
                particles_on = True

                fireball.kill()
                fb = False
                explosion.play()
        if pygame.sprite.spritecollide(self, water_group, False):
            # bubble_pop = False
            player.vel_y = -15
            player.in_air = True
            self.kill()
            # shield = False


class Activation_Button(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.t_act = 0

    def update(self):
        global tunnel, button_activated
        global ver, world_data, player, health_bar, screen_scroll
        self.rect.x += screen_scroll
        if pygame.sprite.spritecollide(self, box_group, False) and self.t_act == 0:
            button_activated = self
            tunnel = True
            self.t_act = 1


class ScreenFade():
    def __init__(self, direction, colour, speed):
        self.direction = direction
        self.colour = colour
        self.speed = speed
        self.fade_counter = 0
        if fullscreen:
            self.border = FULL_SCREEN_WIDTH
            self.speed = self.speed
        else:
            self.border = SCREEN_WIDTH
            self.speed += 50

    def fade(self):

        fade_complete = False
        self.fade_counter += self.speed
        if self.direction == 1:  # whole screen fade
            if fullscreen:
                pygame.draw.rect(screen, self.colour, (0, 0, FULL_SCREEN_WIDTH, FULL_SCREEN_HEIGHT),
                                 self.border - self.fade_counter)
            else:
                pygame.draw.rect(screen, self.colour, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT),
                                 self.border - self.fade_counter)
        if self.direction == 2:  # vertical screen fade down
            if fullscreen:
                pygame.draw.rect(screen, self.colour, (0, 0, FULL_SCREEN_WIDTH, 0 + self.fade_counter))
            else:
                pygame.draw.rect(screen, self.colour, (0, 0, SCREEN_WIDTH, 0 + self.fade_counter))
        if fullscreen:
            if self.fade_counter >= FULL_SCREEN_HEIGHT:
                fade_complete = True
        else:
            if self.fade_counter >= SCREEN_WIDTH:
                fade_complete = True

        return fade_complete


def draw_levels_menu():
    global lvl_buttons, current_level_image, current_level_selected, level, ver, season, start_game, start_intro, lvls_unlocked, player, health_bar, world, world_data, shiftx, shifty, show_levels
    with open('levelsUnlocked.txt') as file:
        reader = file.read()
    lvls_unlocked = reader.split(' ')

    # surface1 = screen.convert_alpha()
    # surface1.fill([0, 0, 0, 0])
    # pygame.draw.rect(surface1, (0, 0, 0, 230), rect_info)
    # screen.blit(surface1, (0, 0))
    screen.fill(BG)

    draw_text('Levels', PixelFont4, WHITE, shiftx + int(SCREEN_WIDTH / 3.59) + 100, int(SCREEN_HEIGHT / 26.66))
    draw_text('Levels', PixelFont5, BLACK, shiftx + int(SCREEN_WIDTH / 3.59) + 104, int(SCREEN_HEIGHT / 26.66) + 4)
    h_dif = 0
    if fullscreen:
        h_dif = -30

    r1 = pygame.Rect(shiftx + SCREEN_WIDTH // 2 - int(SCREEN_WIDTH / 2.85),
                     shifty + SCREEN_HEIGHT // 2 - int(SCREEN_HEIGHT / 5.92) + h_dif, int(SCREEN_WIDTH / 1.42),
                     int(SCREEN_HEIGHT / 2.53))
    r2 = pygame.Rect(shiftx + SCREEN_WIDTH // 2 - int(SCREEN_WIDTH / 2.72),
                     shifty + SCREEN_HEIGHT // 2 - int(SCREEN_HEIGHT / 5.51) + h_dif, int(SCREEN_WIDTH / 1.35),
                     int(SCREEN_HEIGHT / 2.38))
    pygame.draw.rect(screen, WHITE, r2)
    pygame.draw.rect(screen, BLACK, r1)
    if lvls_unlocked[current_level_selected] == '0':
        screen.blit(current_level_image, (shiftx + SCREEN_WIDTH // 2 - int(SCREEN_WIDTH / 2.85),
                                          shifty + SCREEN_HEIGHT // 2 - int(SCREEN_HEIGHT / 5.92) + h_dif))
        r = pygame.Rect(shiftx + SCREEN_WIDTH // 2 - int(SCREEN_WIDTH / 2.85),
                        shifty + SCREEN_HEIGHT // 2 - int(SCREEN_HEIGHT / 5.92) + h_dif,
                        current_level_image.get_width(), current_level_image.get_height())
        surface1 = screen.convert_alpha()
        surface1.fill([0, 0, 0, 0])
        pygame.draw.rect(surface1, (0, 0, 0, 200), r)
        screen.blit(surface1, (0, 0))
    else:
        screen.blit(current_level_image, (shiftx + SCREEN_WIDTH // 2 - int(SCREEN_WIDTH / 2.85),
                                          shifty + SCREEN_HEIGHT // 2 - int(SCREEN_HEIGHT / 5.92) + h_dif))
    for i, b in enumerate(lvl_buttons):
        if i + 1 <= 4:

            clicked, detect = b.draw(screen, True)
            if clicked:
                if lvls_unlocked[i] == '1':
                    show_levels = False
                    start_game = True
                    start_intro = True
                    level = i + 1
                    ver = 0
                    if level >= 1 and level <= 3:
                        season = 0
                    elif level >= 4 and level <= 6:
                        season = 1
                    else:
                        season = 2

                    world_data = []
                    for r in range(ROWS):
                        r = [-1] * COLUMNS
                        world_data.append(r)
                    global screen_scroll, bg_scroll
                    screen_scroll = 0
                    bg_scroll = 0
                    world_data = reset_level()
                    with open(f'level{level}_data{ver}.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar = world.process_data(world_data)

            if detect:
                current_level_image = lvl_images[i]
                current_level_selected = i
            if fullscreen:
                draw_text(str(i + 1), PixelFont6, WHITE,
                          190 + (FULL_SCREEN_WIDTH - 600) // 3 * i + LVL_BOX.get_width() // 2,
                          shifty + int(SCREEN_HEIGHT / 20) + LVL_BOX.get_height() + int(SCREEN_HEIGHT / 40) - 80)
            else:
                draw_text(str(i + 1), PixelFont6, WHITE,
                          shiftx + int(SCREEN_WIDTH / 8.33) + (LVL_BOX.get_width() + int(
                              SCREEN_WIDTH / 8.33)) * i + LVL_BOX.get_width() // 2 - int(SCREEN_WIDTH / 83.33),
                          shifty + int(SCREEN_HEIGHT / 20) + LVL_BOX.get_height() + int(SCREEN_HEIGHT / 40))
            if lvls_unlocked[i] == '0':
                r = b.rect
                surface1 = screen.convert_alpha()
                surface1.fill([0, 0, 0, 0])
                pygame.draw.rect(surface1, (0, 0, 0, 200), r)
                screen.blit(surface1, (0, 0))
        else:

            clicked, detect = b.draw(screen, True)
            if clicked:
                if lvls_unlocked[i] == '1':
                    start_game = True
                    start_intro = True
                    level = i + 1
                    ver = 0
                    if level >= 1 and level <= 3:
                        season = 0
                    elif level >= 4 and level <= 6:
                        season = 1
                    else:
                        season = 2
                    world_data = []
                    for r in range(ROWS):
                        r = [-1] * COLUMNS
                        world_data.append(r)

                    screen_scroll = 0
                    bg_scroll = 0
                    world_data = reset_level()
                    with open(f'level{level}_data{ver}.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar = world.process_data(world_data)
            if detect:
                current_level_image = lvl_images[i]
                current_level_selected = i
            if fullscreen:
                draw_text(str(i + 1), PixelFont6, WHITE,
                          200 + (FULL_SCREEN_WIDTH - 600) // 3 * (i - 4) + LVL_BOX.get_width() // 2,
                          shifty + int(SCREEN_HEIGHT / 20) + LVL_BOX.get_height() + int(SCREEN_HEIGHT / 40) + 520)
            else:
                draw_text(str(i + 1), PixelFont6, WHITE,
                          shiftx + int(SCREEN_WIDTH / 8.33) + (
                                  LVL_BOX.get_width() + int(SCREEN_WIDTH / 8.33)) * (
                                  i - 4) + LVL_BOX.get_width() // 2 - int(
                              SCREEN_WIDTH / 83.33),
                          shifty + int(SCREEN_HEIGHT / 20) + LVL_BOX.get_height() + int(SCREEN_HEIGHT / 40) + 500)
            if lvls_unlocked[i] == '0':
                r = b.rect
                surface1 = screen.convert_alpha()
                surface1.fill([0, 0, 0, 0])
                pygame.draw.rect(surface1, (0, 0, 0, 200), r)
                screen.blit(surface1, (0, 0))

    pygame.display.update()


def draw_viewpoint(radius, color, x, y, width):

    surface1 = screen.convert_alpha()
    surface1.fill([0, 0, 0, 0])
    pygame.draw.circle(surface1, (0, 0, 0, 230), (x, y), radius, width)
    screen.blit(surface1, (0, 0))
    # surface = screen.convert_alpha()
    # pygame.draw.circle(surface,color,(x,y),radius,width)

def draw_end():
    global IntroFade,MUSIC_VOLUME,end_count


    draw_bg2()
    if fullscreen:
        draw_text("The End", PixelFont3, WHITE, FULL_SCREEN_WIDTH // 2 - 250, 100)
        draw_text("The End", PixelFont3, BLACK, FULL_SCREEN_WIDTH // 2 - 246, 101)
        draw_text("You have succesfully conquered Pixel Run!", PixelFont5, WHITE, FULL_SCREEN_WIDTH // 2 - 700, 400)
        draw_text("You have succesfully conquered Pixel Run!", PixelFont5, BLACK, FULL_SCREEN_WIDTH // 2 - 696, 402)
        draw_text("Congratulations!!!", PixelFont5, WHITE, FULL_SCREEN_WIDTH // 2 - 280, 700)
        draw_text("Congratulations!!!", PixelFont5, BLACK, FULL_SCREEN_WIDTH // 2 - 276, 702)






    else:

        draw_text("The End", PixelFont3, WHITE, SCREEN_WIDTH // 2 - 270, 100)
        draw_text("The End", PixelFont3, BLACK, SCREEN_WIDTH // 2 - 266, 101)
        draw_text("You have succesfully conquered Pixel Run!", PixelFont7, WHITE, SCREEN_WIDTH // 2 - 390, 350)
        draw_text("You have succesfully conquered Pixel Run!", PixelFont7, BLACK, SCREEN_WIDTH // 2 - 386, 352)
        draw_text("Congratulations!!!", PixelFont7, WHITE, SCREEN_WIDTH // 2 - 200, 500)
        draw_text("Congratulations!!!", PixelFont7, BLACK, SCREEN_WIDTH // 2 - 196, 502)

    if fullscreen:
        draw_text("MENU - M", font, WHITE, FULL_SCREEN_WIDTH - 100, FULL_SCREEN_HEIGHT - 30)
    else:
        draw_text("MENU - M", font, WHITE, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 30)

def settings_show():
    global music_width, sfx_width, fullscreen, SCREEN_WIDTH, SCREEN_HEIGHT, FULL_SCREEN_WIDTH, FULL_SCREEN_HEIGHT, b_count, settings_screen
    # if fullscreen:
    #     t1 = SCREEN_WIDTH
    #     t2 = SCREEN_HEIGHT
    #     SCREEN_WIDTH = FULL_SCREEN_WIDTH - 200
    #     SCREEN_HEIGHT = FULL_SCREEN_HEIGHT - 200

    if season == 2 or not start_game:
        draw_bg2()
    elif season == 1:
        draw_bg1()
    else:
        draw_bg()

    start_x = SCREEN_WIDTH // 2 - 60
    start_y = 30
    if fullscreen:
        start_x = FULL_SCREEN_WIDTH // 2 - 60
        start_y = 100

    if fullscreen:
        rect_info = pygame.Rect(start_x - 320, 0,
                                770, FULL_SCREEN_HEIGHT)
    else:
        rect_info = pygame.Rect(start_x - 320, 0,
                                770, SCREEN_HEIGHT)
    surface1 = screen.convert_alpha()
    surface1.fill([0, 0, 0, 0])
    pygame.draw.rect(surface1, (0, 0, 0, 110), rect_info)
    screen.blit(surface1, (0, 0))
    draw_text('Music', PixelFont6, WHITE, start_x + 10, start_y - 20)

    pygame.draw.rect(screen, BLACK, (start_x - 190, start_y + 30, 500, 30))
    pygame.draw.rect(screen, WHITE, (start_x - 190, start_y + 30, music_width, 30))
    pygame.draw.rect(screen, BLACK, (start_x - 190, start_y + 30, 500, 30), 5)
    draw_text('Sound effects', PixelFont6, WHITE, start_x - 45, start_y + 110)

    pygame.draw.rect(screen, BLACK, (start_x - 190, start_y + 170, 500, 30))
    pygame.draw.rect(screen, WHITE, (start_x - 190, start_y + 170, sfx_width, 30))
    pygame.draw.rect(screen, BLACK, (start_x - 190, start_y + 170, 500, 30), 5)
    draw_text('Controls', PixelFont6, WHITE, start_x - 24, start_y + 230)

    # rect_info = pygame.Rect(start_x - 320, start_y + 300,
    #                             770, SCREEN_HEIGHT)
    # surface1 = screen.convert_alpha()
    # surface1.fill([0, 0, 0, 0])
    # pygame.draw.rect(surface1, (0, 0, 0, 220), rect_info)
    # screen.blit(surface1, (0, 0))
    if fullscreen:
        screen.blit(CONTROLS_IMG, (start_x - 240, start_y + 360))
    else:
        screen.blit(CONTROLS_IMG, (start_x - 240, start_y + 290))
    pos = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0] == True and pos[0] >= start_x - 190 and pos[
        0] <= start_x + 310 and pos[1] >= start_y + 30 and pos[1] <= start_y + 60:
        percent = (pos[0] - (start_x - 190)) / 5
        MUSIC_VOLUME = (percent * MAX_VOLUME) / 100

        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        music_width = pos[0] - (start_x - 190)

    if pygame.mouse.get_pressed()[0] == True and pos[0] >= start_x - 190 and pos[
        0] <= start_x + 310 and pos[1] >= start_y + 170 and pos[1] <= start_y + 200:
        percent = (pos[0] - (start_x - 190)) / 5
        SFX_VOLUME = (percent * MAX_VOLUME) / 100
        jump_fx.set_volume(SFX_VOLUME)
        shot_fx.set_volume(SFX_VOLUME)
        grenade_fx.set_volume(SFX_VOLUME)

        sfx_width = pos[0] - (start_x - 190)
    # if fullscreen:
    #
    #     SCREEN_WIDTH = t1
    #     SCREEN_HEIGHT = t2
    # if fullscreen:
    #     t1 = SCREEN_WIDTH
    #     t2 = SCREEN_HEIGHT
    #     SCREEN_WIDTH = FULL_SCREEN_WIDTH - 200
    #     SCREEN_HEIGHT = FULL_SCREEN_HEIGHT - 200
    #
    # pygame.draw.rect(screen, BLACK2, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 120, 600, 400))
    # pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 120, 600, 400), 10)
    # draw_text('Music', PixelFont, WHITE, SCREEN_WIDTH // 2 - 60, SCREEN_HEIGHT // 2 - 80)
    # pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 , 500, 50))
    # pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 , music_width, 50))
    # pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 , 500, 50), 5)
    # draw_text('Sound effects', PixelFont, WHITE, SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 120)
    # pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 180, 500, 50))
    # pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 180, sfx_width, 50))
    # pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 180, 500, 50), 5)
    # pos = pygame.mouse.get_pos()
    # if pygame.mouse.get_pressed()[0] == True and pos[0] >= SCREEN_WIDTH // 2 - 250 and pos[
    #     0] <= SCREEN_WIDTH // 2 + 250 and pos[1] >= SCREEN_HEIGHT // 2 and pos[1] <= SCREEN_HEIGHT // 2 +50:
    #     percent = (pos[0] - (SCREEN_WIDTH // 2 - 250)) / 5
    #     MUSIC_VOLUME = (percent * MAX_VOLUME) / 100
    #
    #     pygame.mixer.music.set_volume(MUSIC_VOLUME)
    #     music_width = pos[0] - (SCREEN_WIDTH // 2 - 250)
    #
    # if pygame.mouse.get_pressed()[0] == True and pos[0] >= SCREEN_WIDTH // 2 - 250 and pos[
    #     0] <= SCREEN_WIDTH // 2 + 250 and pos[1] >= SCREEN_HEIGHT // 2 + 180 and pos[1] <= SCREEN_HEIGHT // 2 + 230:
    #     percent = (pos[0] - (SCREEN_WIDTH // 2 - 250)) / 5
    #     SFX_VOLUME = (percent * MAX_VOLUME) / 100
    #     jump_fx.set_volume(SFX_VOLUME)
    #     shot_fx.set_volume(SFX_VOLUME)
    #     grenade_fx.set_volume(SFX_VOLUME)
    #
    #     sfx_width = pos[0] - (SCREEN_WIDTH // 2 - 250)
    # if fullscreen:
    #
    #     SCREEN_WIDTH = t1
    #     SCREEN_HEIGHT = t2
    # create screen Fade
    # rect_info = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 120,
    #                         600, 400)
    # surface1 = screen.convert_alpha()
    # surface1.fill([0, 0, 0, 0])
    # pygame.draw.rect(surface1, (0, 0, 0, 230), rect_info)
    # screen.blit(surface1, (0, 0))
    s_click, s_det = settings_button.draw(screen, False)

    if s_click:
        settings_screen = False
        b_count = 0


DeathFade = ScreenFade(2, PINK, 8)
IntroFade = ScreenFade(1, BLACK, 15)

# create buttons
start_button = button.Button(shiftx + SCREEN_WIDTH // 2 - 130, shifty + SCREEN_HEIGHT // 2 - 100, START_IMG, 1)
exit_button = button.Button(shiftx + SCREEN_WIDTH // 2 - 130, shifty + SCREEN_HEIGHT // 2 + 100, EXIT_IMG, 1)
restart_button = button.Button(shiftx + SCREEN_WIDTH // 2 - 100, shifty + SCREEN_HEIGHT // 2 - 50, RESTART_IMG, 2)

# create sprite groups
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
item_box_group = pygame.sprite.Group()
decoration_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
infoBoxGroup = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
light_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()
act_buttons = pygame.sprite.Group()
movingTilegroup = pygame.sprite.Group()

appear = Appearance(1, appearance_imgs)

# load in levels





clock = pygame.time.Clock()
settings_button = button.Button(SCREEN_WIDTH - 100, 0, SETTINGS_IMG, 3)
run = True
while run:

    if not start_game:
        if not settings_screen:
            # if season == 0:
            #     draw_bg()
            # elif season == 1:
            #     draw_bg1()
            # else:
            if not show_levels:
                draw_bg2()

                draw_text('Pixel Run', PixelFont2, WHITE, shiftx + 120, shifty + 80)
                draw_text('Pixel Run', PixelFont3, BLACK, shiftx + 124, shifty + 82)
                clicked, detect = start_button.draw(screen, True)
                clicked_exit, detect_exit = exit_button.draw(screen, True)
                settings_clicked, settings_exit = settings_button.draw(screen, False)
                if clicked:
                    show_levels = True
                if clicked_exit:
                    run = False
                    quit()
                    sys.exit()


                if settings_clicked:
                    settings_screen = True

            else:
                draw_levels_menu()

        else:
            settings_clicked, settings_exit = settings_button.draw(screen, False)
            if settings_clicked:
                settings_screen = False

            settings_show()






    else:

        clock.tick(FPS)

        # update background
        if season == 0:
            draw_bg()
        elif season == 1:
            draw_bg1()
        else:
            draw_bg2()
        # draw world map
        world.draw()
        player.update()
        if player_appearance:

            appear.draw()

        elif not start_intro:
            player.draw()

        for enemy in enemy_group:
            enemy.draw()
            enemy.update()
            enemy.ai()

        # update and draw groups
        bullet_group.update()
        bullet_group.draw(screen)
        grenade_group.update()
        grenade_group.draw(screen)
        explosion_group.update()
        explosion_group.draw(screen)
        item_box_group.update()
        item_box_group.draw(screen)
        decoration_group.update()
        water_group.update()
        exit_group.update()
        decoration_group.draw(screen)
        water_group.draw(screen)
        exit_group.draw(screen)

        infoBoxGroup.draw(screen)

        coin_group.draw(screen)
        coin_group.update()
        light_group.draw(screen)
        light_group.update()
        box_group.draw(screen)
        box_group.update()
        act_buttons.draw(screen)
        act_buttons.update()
        movingTilegroup.draw(screen)
        movingTilegroup.update()


        # settings button

        if healthBoost:
            health_counter = 30
            healthBoost = False
            heal_fx.play()
        if health_counter > 1:
            health_counter -= 1

            h_rect = HEALTH_BOOST.get_rect()
            h_rect.center = player.rect.center
            screen.blit(HEALTH_BOOST, h_rect)
            draw_text('health + 10', font, BLACK, h_rect.x, h_rect.y - 30)
        elif health_counter == 1:
            player.health += 10
            player.coins -= 20
            health_counter = 0

        if drop_box:
            drop_box = False
            if player.boxes > 0:
                box = Box(BOX_IMG, player.rect.x, player.rect.y + BOX_IMG.get_height())
                box_group.add(box)
                player.boxes -= 1
        if fullscreen:

            draw_viewpoint(2000, BLACK, player.rect.x + player.rect.width // 2, player.rect.y + player.rect.height // 2,
                           circle_width)
        else:
            draw_viewpoint(1050, BLACK, player.rect.x + player.rect.width // 2, player.rect.y + player.rect.height // 2,
                           circle_width)
        if fullscreen:
            draw_text("MENU - M", font, WHITE, FULL_SCREEN_WIDTH - 100, FULL_SCREEN_HEIGHT - 30)
        else:
            draw_text("MENU - M", font, WHITE, SCREEN_WIDTH - 100, SCREEN_HEIGHT - 30)

        settings_clicked, settings_exit = settings_button.draw(screen, False)
        if settings_clicked:
            if b_count == 0:
                settings_screen = True
                b_count = 1
                current_health = player.health
            else:
                settings_screen = False
                b_count = 0
                player.health = current_health

        if settings_screen:
            settings_show()
            player.health = current_health

        health_bar.draw(player.health)
        # show ammo
        draw_text(f'AMMO: ', font, WHITE, 10, 35)
        for x in range(player.ammo):
            screen.blit(BULLET_IMG, (90 + (x * 10), 40))
        draw_text(f'GRENADES: ', font, WHITE, 10, 60)
        for x in range(player.grenades):
            screen.blit(GRENADE_IMG, (135 + (x * 15), 60))
        if player.coins >= 50:
            player.coins = 50
        draw_text(f'COINS: {player.coins}', font, WHITE, 10, 85)
        screen.blit(COIN_IMG, (120, 86))
        draw_text(f'BOXES: {player.boxes}', font, WHITE, 10, 110)
        # SHOW INTRO
        if start_intro:
            draw_text(f'Level {level}', font2, WHITE, SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 200)

            if IntroFade.fade():
                start_intro = False

                revive_fx.play()


                player_appearance = True

                IntroFade.fade_counter = 0

        elif IntroFade.fade_counter < SCREEN_WIDTH + 50 and IntroFade.fade_counter >= SCREEN_WIDTH:



            draw_text(f'Level {level}', font2, WHITE, SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 - 200)
            IntroFade.fade_counter += 1
        elif IntroFade.fade_counter >= SCREEN_WIDTH + 50:

            IntroFade.fade_counter = 0


        # update player action
        if player.alive:
            if shield_activate_timer>0:
                shield_activate_timer -= 1
                draw_text(f'Shield cooldown: {shield_activate_timer//10}', font, RED, 10, 135)
            if shield_activate_timer<0:
                shield_activate_timer = 0
            if particles_on:
                for i in range(240):
                    particle = Particles(player.rect.x - 30,player.rect.y,RED,0)
                    particles.append(particle)

                particles_on = False

            for particle in particles:
                particle.draw(screen)
                if not particle.update():
                    particles.remove(particle)
            if hurt_timer > 0:
                hurt_timer -= 1
                if fullscreen:
                    r = pygame.Rect(0,0,FULL_SCREEN_WIDTH,FULL_SCREEN_HEIGHT)
                else:
                    r = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
                surface1 = screen.convert_alpha()
                surface1.fill([0, 0, 0, 0])
                pygame.draw.rect(surface1, (255, 0, 0, 120), r)
                screen.blit(surface1, (0, 0))





            if shield:
                if player.coins >= 10:
                    s = Shield()
                    s.draw()
                    s.update()
                else:
                    draw_text('You need 10 coins to activate force field!', font, WHITE, 300, 100)

            if IntroFade.fade_counter == 0:

                # fireball shooter
                if fire or level >= 3:
                    r = random.randint(1, 700)
                    if r == 13:
                        fb_sfx.play()
                        fireball = FireBall()
                        fb = True
                    if fb:
                        fireball.draw()
                        fireball.update()
                # shoot bullets
            if shoot:
                player.shoot()

            # throw grenades
            elif grenade and grenade_thrown == False and player.grenades > 0:
                g = Grenade(player.rect.centerx + player.rect.size[0] * 0.5 * player.direction, player.rect.top,
                            player.direction)
                grenade_group.add(g)
                grenade_thrown = True
                player.grenades -= 1

            if player.in_air:
                player.update_action(2)  # 2: jump
            elif moving_left or moving_right:
                player.update_action(1)  # 1 : run
            else:
                player.update_action(0)  # 0: idle
            screen_scroll, level_complete = player.move(moving_left, moving_right)
            bg_scroll -= screen_scroll
            # check if level is completed

            if level_complete:
                win_fx.play()
                lvls_unlocked[level] = '1'
                update_lvls = ""
                for i in range(0, 8):
                    update_lvls += str(lvls_unlocked[i])
                    update_lvls += " "
                with open('levelsUnlocked.txt', 'w') as file:
                    file.write(update_lvls)

                h = player.health
                if fullscreen:
                    circle_width = 1250
                health_bar.draw(30)
                if fullscreen:
                    draw_viewpoint(2000, BLACK, player.rect.x + player.rect.width // 2,
                                   player.rect.y + player.rect.height // 2,
                                   circle_width)
                else:
                    draw_viewpoint(1050, BLACK, player.rect.x + player.rect.width // 2,
                                   player.rect.y + player.rect.height // 2,
                                   circle_width)
                pygame.display.update()
                pygame.time.delay(400)
                if fullscreen:
                    circle_width = 1250
                health_bar.draw(20)
                if fullscreen:

                    draw_viewpoint(2000, BLACK, player.rect.x + player.rect.width // 2,
                                   player.rect.y + player.rect.height // 2,
                                   circle_width)
                else:
                    draw_viewpoint(1050, BLACK, player.rect.x + player.rect.width // 2,
                                   player.rect.y + player.rect.height // 2,
                                   circle_width)
                pygame.display.update()
                pygame.time.delay(400)
                if fullscreen:
                    circle_width = 1250
                health_bar.draw(10)
                if fullscreen:

                    draw_viewpoint(2000, BLACK, player.rect.x + player.rect.width // 2,
                                   player.rect.y + player.rect.height // 2,
                                   circle_width)
                else:
                    draw_viewpoint(1050, BLACK, player.rect.x + player.rect.width // 2,
                                   player.rect.y + player.rect.height // 2,
                                   circle_width)
                pygame.display.update()
                pygame.time.delay(400)

                start_intro = True
                level += 1
                bg_scroll = 0
                world_data = reset_level()
                ver = 0
                if level >= 1 and level <= 3:
                    season = 0
                elif level >= 4 and level <= 6:
                    season = 1
                else:
                    season = 2

                if level <= MAX_LEVELS:

                    with open(f'level{level}_data0.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar = world.process_data(world_data)
                    player.health = player.max_health
                else:
                    end = True
            if end:
                ok = True
                draw_end()
                if end_count == 0:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('audio/Victory.mp3')
                    pygame.mixer.music.set_volume(0.8)
                    pygame.mixer.music.play(-1, 0.0)
                if not end_fade:
                    if IntroFade.fade():
                        IntroFade.fade_counter = -1
                        end_fade = True
                if end_count == 1:
                    if fullscreen:
                        mx = random.randint(100,FULL_SCREEN_WIDTH)
                        my = random.randint(100,FULL_SCREEN_HEIGHT)
                    else:
                        mx = random.randint(100, SCREEN_WIDTH)
                        my = random.randint(100, SCREEN_HEIGHT)

                    for x in range(240):
                        particle = Particles(mx,my, RED, 0)
                        particles.append(particle)
                    if fullscreen:
                        mx = random.randint(100, FULL_SCREEN_WIDTH)
                        my = random.randint(100, FULL_SCREEN_HEIGHT)
                    else:
                        mx = random.randint(100, SCREEN_WIDTH)
                        my = random.randint(100, SCREEN_HEIGHT)
                    for x in range(240):
                        particle = Particles(mx, my, PINK, 0)
                        particles.append(particle)

                end_count += 1
                if end_count>=10:
                    end_count = 1

                for particle in particles:
                    particle.draw(screen)
                    if not particle.update():
                        particles.remove(particle)



        else:
            if fullscreen:

                draw_viewpoint(2000, BLACK, player.rect.x + player.rect.width // 2,
                               player.rect.y + player.rect.height // 2,
                               800)
            else:
                draw_viewpoint(1050, BLACK, player.rect.x + player.rect.width // 2,
                               player.rect.y + player.rect.height // 2,
                               300)
            if DeathFade.fade():


                screen_scroll = 0
                player.speed = 0
                restart_clicked, restart_detected = restart_button.draw(screen, True)
                if restart_clicked and settings_screen == False:
                    DeathFade.fade_counter = 0
                    start_intro = True
                    bg_scroll = 0
                    world_data = reset_level()
                    ver = 0
                    with open(f'level{level}_data0.csv', newline='') as csvfile:
                        reader = csv.reader(csvfile, delimiter=',')
                        for x, row in enumerate(reader):
                            for y, tile in enumerate(row):
                                world_data[x][y] = int(tile)
                    world = World()
                    player, health_bar = world.process_data(world_data)
                settings_clicked, settings_exit = settings_button.draw(screen, False)
                if settings_clicked:
                    if b_count == 0:
                        settings_screen = True
                        b_count = 1
                        current_health = player.health
                    else:
                        settings_screen = False
                        b_count = 0
                        player.health = current_health
                if settings_screen:
                    settings_show()
                    player.health = current_health
        # print(tunnel)

        if tunnel:
            # if button_activated.t_act == 1:
            #     print(button_activated.t_act)
            if 2 == 2:
                # button_activated.t_act +=1

                tunnel = False
                scroll = screen_scroll
                sc = bg_scroll
                posx = player.rect.x
                posy = player.rect.y
                h = player.health
                h = player.health
                a = player.ammo
                g = player.grenades
                c = player.coins
                world_data = reset_level()
                if ver == 0:
                    ver = 1
                elif ver == 1:
                    ver = 0
                with open(f'level{level}_data{ver}.csv', newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    for x, row in enumerate(reader):
                        for y, tile in enumerate(row):
                            world_data[x][y] = int(tile)
                world = World()
                info_counter = 0
                player, health_bar = world.process_data(world_data)
                player.health = h
                player.ammo = a
                player.grenades = g
                player.coins = c

                player.rect.x = posx
                player.rect.y = posy
                screen_scroll = scroll
                bg_scroll = sc + screen_scroll
                player.health = h
    # demonstrate the player and boxes rects
    # pygame.draw.rect(screen,RED,player.rect,4)
    # for box in box_group:
    #     pygame.draw.rect(screen,RED,box.rect,4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_w and player.alive:
                player.jump = True
                jump_fx.play()
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_q:
                grenade = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_e and player.alive:
                player.megajump = True
            if event.key == pygame.K_s:
                if shield_activate_timer == 0:
                    shield = True
            if event.key == pygame.K_RCTRL:
                healthBoost = True
            if event.key == pygame.K_UP:
                pick_up_box = True
            if event.key == pygame.K_DOWN:
                drop_box = True
            if event.key == pygame.K_m:
                start_game = False
                show_levels = True
                if end:
                    end = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('audio/music2.mp3')
                    pygame.mixer.music.set_volume(MUSIC_VOLUME)
                    pygame.mixer.music.play(-1,0.0,5000)
            if event.key == pygame.K_f:
                pygame.display.quit()
                pygame.display.init()
                fullscreen = True
                circle_width = 1250

                shiftx = (FULL_SCREEN_WIDTH - SCREEN_WIDTH) // 2
                shifty = (FULL_SCREEN_HEIGHT - SCREEN_HEIGHT) // 2

                init_program()
                SCROLL_TRESH = FULL_SCREEN_WIDTH // 2 + 200
                if start_game:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

            if event.key == pygame.K_g:
                fullscreen = False
                shiftx = 0
                shifty = 0
                pygame.display.quit()
                pygame.display.init()
                init_program()
                SCROLL_TRESH = 200
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, 16)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_q:
                grenade = False
                grenade_thrown = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_s:
                if shield_activate_timer == 0:
                    shield_activate_timer = 100
                shield = False
            if event.key == pygame.K_UP:
                pick_up_box = False

    infoBoxGroup.update()
    pygame.display.update()

