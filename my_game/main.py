import pygame
import sys
import os
import random
from menu import main_menu, settings_menu
from levels.level1 import level as level1
from levels.level2 import level as level2
from levels.level3 import level as level3
from levels.maze_level import MazeLevel
from objects import Player, Enemy, Bonus, Obstacle, MovingObstacle  # Импортируем классы объектов

# Инициализация Pygame
pygame.init()

# Настройки окна игры
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)  # Добавляем поддержку изменения размера окна
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


# Функция для проверки столкновений со стенами
def check_collision(rect, level):
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if tile == '1':
                wall_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if rect.colliderect(wall_rect):
                    return True
    return False


# Функция для нахождения свободного места для спавна игрока
def find_spawn_position(level):
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if tile == '0':
                return [x * TILE_SIZE, y * TILE_SIZE]
    return [WIDTH // 2, HEIGHT // 2]  # Если нет свободного места, спавним в центре


# Функция для отображения текста на экране
def draw_text(screen, text, font, color, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_obj, text_rect)


# Функция для мини-игры "Сбор предметов"
def item_collecting_mini_game(screen, font, player, settings):
    items = [Bonus("assets/images/item.png", random.randint(0, WIDTH // TILE_SIZE - 1) * TILE_SIZE,
                   random.randint(0, HEIGHT // TILE_SIZE - 1) * TILE_SIZE) for _ in range(10)]
    obstacles = [Obstacle("assets/images/obstacle.png", random.randint(0, WIDTH // TILE_SIZE - 1) * TILE_SIZE,
                          random.randint(0, HEIGHT // TILE_SIZE - 1) * TILE_SIZE) for _ in range(10)]
    moving_obstacles = [
        MovingObstacle("assets/images/moving_obstacle.png", random.randint(0, WIDTH // TILE_SIZE - 1) * TILE_SIZE,
                       random.randint(0, HEIGHT // TILE_SIZE - 1) * TILE_SIZE, 2) for _ in range(5)]

    player.rect.topleft = [WIDTH // 2, HEIGHT // 2]
    collected_items = 0
    mini_game_running = True

    while mini_game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[settings['move_left']]:
            player.rect.x -= player.speed
        if keys[settings['move_right']]:
            player.rect.x += player.speed
        if keys[settings['move_up']]:
            player.rect.y -= player.speed
        if keys[settings['move_down']]:
            player.rect.y += player.speed

        # Отрисовка фона
        screen.blit(pygame.transform.scale(mini_game_background_image, (screen.get_width(), screen.get_height())),
                    (0, 0))

        # Отрисовка препятствий
        for obstacle in obstacles:
            obstacle.draw(screen)
            if player.rect.colliderect(obstacle.rect):
                if keys[settings['move_left']]:
                    player.rect.x += player.speed
                if keys[settings['move_right']]:
                    player.rect.x -= player.speed
                if keys[settings['move_up']]:
                    player.rect.y += player.speed
                if keys[settings['move_down']]:
                    player.rect.y -= player.speed

        # Отрисовка движущихся препятствий
        for moving_obstacle in moving_obstacles:
            moving_obstacle.move()
            moving_obstacle.draw(screen)
            if player.rect.colliderect(moving_obstacle.rect):
                if keys[settings['move_left']]:
                    player.rect.x += player.speed
                if keys[settings['move_right']]:
                    player.rect.x -= player.speed
                if keys[settings['move_up']]:
                    player.rect.y += player.speed
                if keys[settings['move_down']]:
                    player.rect.y -= player.speed

        # Отрисовка предметов
        for item in items:
            item.draw(screen)
            if player.rect.colliderect(item.rect):
                items.remove(item)
                collected_items += 1
                item_sound.play()

        player.draw(screen)

        draw_text(screen, f"Collected items: {collected_items}", font, (255, 255, 255), 10, 10)

        pygame.display.flip()

        if collected_items >= 10:
            mini_game_running = False

        pygame.time.Clock().tick(60)

    return collected_items


# Основной игровой цикл
def game_loop(screen, settings, level):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

    move_sound.set_volume(settings['effects_volume'])
    bonus_sound.set_volume(settings['effects_volume'])
    upgrade_sound.set_volume(settings['effects_volume'])
    item_sound.set_volume(settings['effects_volume'])

    running = True
    clock = pygame.time.Clock()

    player_pos = find_spawn_position(level)
    player = Player("assets/images/player.png", player_pos[0], player_pos[1], 5)

    enemies = [Enemy("assets/images/enemy.png", x * TILE_SIZE, y * TILE_SIZE, 2) for y, row in enumerate(level) for
               x, tile in enumerate(row) if tile == 'E']
    bonuses = [Bonus("assets/images/bonus.png", x * TILE_SIZE, y * TILE_SIZE) for y, row in enumerate(level) for x, tile
               in enumerate(row) if tile == 'B']
    upgrades = [Bonus("assets/images/upgrade.png", x * TILE_SIZE, y * TILE_SIZE) for y, row in enumerate(level) for
                x, tile in enumerate(row) if tile == 'U']

    step_sound_delay = 300
    last_step_time = pygame.time.get_ticks()

    score = 0
    lives = 3
    font = pygame.font.Font(None, 36)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_F11:  # Обработка нажатия F11 для переключения полноэкранного режима
                settings['fullscreen'] = not settings['fullscreen']
                if settings['fullscreen']:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
            elif event.type == pygame.VIDEORESIZE:  # Обработка изменения размера окна
                screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)

        keys = pygame.key.get_pressed()
        move_played = False
        if keys[settings['move_left']]:
            player.rect.x -= player.speed
            if check_collision(player.rect, level):
                player.rect.x += player.speed
            else:
                move_played = True
        if keys[settings['move_right']]:
            player.rect.x += player.speed
            if check_collision(player.rect, level):
                player.rect.x -= player.speed
            else:
                move_played = True
        if keys[settings['move_up']]:
            player.rect.y -= player.speed
            if check_collision(player.rect, level):
                player.rect.y += player.speed
            else:
                move_played = True
        if keys[settings['move_down']]:
            player.rect.y += player.speed
            if check_collision(player.rect, level):
                player.rect.y -= player.speed
            else:
                move_played = True

        if move_played:
            current_time = pygame.time.get_ticks()
            if current_time - last_step_time > step_sound_delay:
                move_sound.play()
                last_step_time = current_time

        # Отрисовка фона
        screen.blit(pygame.transform.scale(game_background_image, (screen.get_width(), screen.get_height())), (0, 0))

        for y, row in enumerate(level):
            for x, tile in enumerate(row):
                if tile == '1':
                    pygame.draw.rect(screen, (255, 255, 255), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        for enemy in enemies:
            enemy.move_towards_player(player.rect.topleft)
            enemy.draw(screen)
            if player.rect.colliderect(enemy.rect):
                collected_items = item_collecting_mini_game(screen, font, player, settings)
                if collected_items < 10:
                    lives -= 1
                    if lives <= 0:
                        running = False

        for bonus in bonuses:
            bonus.draw(screen)
            if player.rect.colliderect(bonus.rect):
                bonuses.remove(bonus)
                score += 10
                bonus_sound.play()

        for upgrade in upgrades:
            upgrade.draw(screen)
            if player.rect.colliderect(upgrade.rect):
                upgrades.remove(upgrade)
                player.speed += 1
                upgrade_sound.play()

        player.draw(screen)

        draw_text(screen, f"Score: {score}", font, (255, 255, 255), 10, 10)
        draw_text(screen, f"Lives: {lives}", font, (255, 255, 255), 10, 50)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()


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
        'language': 'en'  # Установите 'ru' для русского языка
    }

    while True:
        main_menu(screen, game_loop, settings_menu, select_sound, settings)