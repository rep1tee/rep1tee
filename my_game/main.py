import pygame
import sys
import os
from menu import main_menu, settings_menu
from levels.one_level import one
from levels.level2 import two
from levels.level3 import fre
from levels.maze_level import MazeLevel

settings = {
    'language': 'en',
    'fullscreen': False,
    'controls': {
        'left': pygame.K_a,
        'right': pygame.K_d,
        'up': pygame.K_w,
        'down': pygame.K_s
    }
}

# Инициализация Pygame
pygame.init()

# Настройки окна игры
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Развивающаяся игра на Python")

# Загрузка фона для мини-игры и основной игры
mini_game_background_image = pygame.image.load("assets/images/mini_game_background.png")
game_background_image = pygame.image.load("assets/images/game_background.png")

# Загрузка звуков
move_sound = pygame.mixer.Sound("assets/sounds/move.wav")
select_sound = pygame.mixer.Sound("assets/sounds/select.wav")
bonus_sound = pygame.mixer.Sound("assets/sounds/bonus.wav")
upgrade_sound = pygame.mixer.Sound("assets/sounds/upgrade.wav")
item_sound = pygame.mixer.Sound("assets/sounds/item.wav")

for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
            settings['fullscreen'] = not settings['fullscreen']
            if settings['fullscreen']:
                screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)




if __name__ == "__main__":
    if os.path.exists("assets/sounds/background_music.mp3"):
        pygame.mixer.music.load("assets/sounds/background_music.mp3")
        pygame.mixer.music.set_volume(0.5)  # Устанавливаем громкость музыки на 50%
        pygame.mixer.music.play(-1)

    settings = {
        'music_volume': 0.5,
        'effects_volume': 0.5,
        'move_up': pygame.K_w,
        'move_down': pygame.K_s,
        'move_left': pygame.K_a,
        'move_right': pygame.K_d,
        'fullscreen': False,
        'language': 'en'
    }

    while True:
        main_menu(screen, None, settings_menu, select_sound, settings)