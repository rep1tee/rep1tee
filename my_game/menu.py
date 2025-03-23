import pygame
import sys
from levels.level1 import level as level1
from levels.level2 import level as level2
from levels.level3 import level as level3

# Загрузка фона для главного меню
menu_background_image = pygame.image.load("assets/images/menu_background.png")

# Языковые настройки (русский и английский)
LANGUAGES = {
    'en': {
        'main_menu': 'Main Menu',
        'start_game': 'Start Game',
        'settings': 'Settings',
        'exit': 'Exit',
        'control_settings': 'Control Settings',
        'audio_settings': 'Audio Settings',
        'video_settings': 'Video Settings',
        'back_to_menu': 'Back to Menu',
        'move_up': 'Move Up',
        'move_down': 'Move Down',
        'move_left': 'Move Left',
        'move_right': 'Move Right',
        'back_to_settings': 'Back to Settings',
        'audio_settings': 'Audio Settings',
        'music_volume': 'Music Volume',
        'effects_volume': 'Effects Volume',
        'video_settings': 'Video Settings',
        'fullscreen': 'Fullscreen',
        'language': 'Language',
        'english': 'English',
        'russian': 'Russian',
        'select_level': 'Select Level',
    },
    'ru': {
        'main_menu': 'Главное Меню',
        'start_game': 'Начать Игру',
        'settings': 'Настройки',
        'exit': 'Выйти',
        'control_settings': 'Настройки Управления',
        'audio_settings': 'Настройки Аудио',
        'video_settings': 'Настройки Видео',
        'back_to_menu': 'Назад в Меню',
        'move_up': 'Вверх',
        'move_down': 'Вниз',
        'move_left': 'Влево',
        'move_right': 'Вправо',
        'back_to_settings': 'Назад к Настройкам',
        'audio_settings': 'Настройки Аудио',
        'music_volume': 'Громкость Музыки',
        'effects_volume': 'Громкость Эффектов',
        'video_settings': 'Настройки Видео',
        'fullscreen': 'Полноэкранный Режим',
        'language': 'Язык',
        'english': 'Английский',
        'russian': 'Русский',
        'select_level': 'Выберите Уровень',
    }
}

def main_menu(screen, game_loop, settings_menu, select_sound, settings):
    lang = LANGUAGES[settings['language']]
    font = pygame.font.Font(None, 74)
    title_text = font.render(lang['main_menu'], True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 150))

    start_game_text = font.render(lang['start_game'], True, (255, 255, 255))
    start_game_rect = start_game_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))

    settings_text = font.render(lang['settings'], True, (255, 255, 255))
    settings_rect = settings_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    exit_text = font.render(lang['exit'], True, (255, 255, 255))
    exit_rect = exit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    settings['fullscreen'] = not settings['fullscreen']
                    if settings['fullscreen']:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Выход из главного меню
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if start_game_rect.collidepoint(event.pos):
                        select_sound.play()
                        level_menu(screen, game_loop, select_sound, settings)  # Переход в меню выбора уровня
                    elif settings_rect.collidepoint(event.pos):
                        select_sound.play()
                        settings_menu(screen, select_sound, settings)  # Открытие настроек
                    elif exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())), (0, 0))  # Отображение фона
        screen.blit(title_text, title_rect)
        screen.blit(start_game_text, start_game_rect)
        screen.blit(settings_text, settings_rect)
        screen.blit(exit_text, exit_rect)

        pygame.display.flip()

def level_menu(screen, start_game, select_sound, settings):
    lang = LANGUAGES[settings['language']]
    font = pygame.font.Font(None, 74)
    title_text = font.render(lang['select_level'], True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 150))

    level1_text = font.render("Level 1", True, (255, 255, 255))
    level1_rect = level1_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))

    level2_text = font.render("Level 2", True, (255, 255, 255))
    level2_rect = level2_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    level3_text = font.render("Level 3", True, (255, 255, 255))
    level3_rect = level3_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))

    maze_level_text = font.render("Maze Level", True, (255, 255, 255))
    maze_level_rect = maze_level_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 250))

    back_text = font.render(lang['back_to_menu'], True, (255, 255, 255))
    back_rect = back_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 350))

    selected_level = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    settings['fullscreen'] = not settings['fullscreen']
                    if settings['fullscreen']:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                elif event.key == pygame.K_ESCAPE:
                    selected_level = None
                    running = False  # Возврат в главное меню
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if level1_rect.collidepoint(event.pos):
                        select_sound.play()
                        selected_level = "level1"
                    elif level2_rect.collidepoint(event.pos):
                        select_sound.play()
                        selected_level = "level2"
                    elif level3_rect.collidepoint(event.pos):
                        select_sound.play()
                        selected_level = "level3"
                    elif maze_level_rect.collidepoint(event.pos):
                        select_sound.play()
                        selected_level = "maze_level"
                    elif back_rect.collidepoint(event.pos):
                        select_sound.play()
                        selected_level = None
                        running = False  # Возврат в главное меню

        if selected_level:
            start_game(screen, settings, selected_level)  # Запуск игры с выбранным уровнем
            running = False

        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())), (0, 0))  # Отображаем фон с адаптацией размера
        screen.blit(title_text, title_rect)
        screen.blit(level1_text, level1_rect)
        screen.blit(level2_text, level2_rect)
        screen.blit(level3_text, level3_rect)
        screen.blit(maze_level_text, maze_level_rect)
        screen.blit(back_text, back_rect)

        pygame.display.flip()

def settings_menu(screen, select_sound, settings):
    lang = LANGUAGES[settings['language']]
    font = pygame.font.Font(None, 74)
    title_text = font.render(lang['settings'], True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 150))

    control_text = font.render(lang['control_settings'], True, (255, 255, 255))
    control_rect = control_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))

    audio_text = font.render(lang['audio_settings'], True, (255, 255, 255))
    audio_rect = audio_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    video_text = font.render(lang['video_settings'], True, (255, 255, 255))
    video_rect = video_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))

    back_text = font.render(lang['back_to_menu'], True, (255, 255, 255))
    back_rect = back_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 250))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    settings['fullscreen'] = not settings['fullscreen']
                    if settings['fullscreen']:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Возврат в главное меню
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if control_rect.collidepoint(event.pos):
                        select_sound.play()
                        control_settings(screen, select_sound, settings)  # Открытие настроек управления
                    elif audio_rect.collidepoint(event.pos):
                        select_sound.play()
                        audio_settings(screen, select_sound, settings)  # Открытие настроек аудио
                    elif video_rect.collidepoint(event.pos):
                        select_sound.play()
                        video_settings(screen, select_sound, settings)  # Открытие настроек видео
                    elif back_rect.collidepoint(event.pos):
                        select_sound.play()
                        running = False  # Возврат в главное меню

        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())), (0, 0))  # Отображаем фон
        screen.blit(title_text, title_rect)
        screen.blit(control_text, control_rect)
        screen.blit(audio_text, audio_rect)
        screen.blit(video_text, video_rect)
        screen.blit(back_text, back_rect)

        pygame.display.flip()

def control_settings(screen, select_sound, settings):
    lang = LANGUAGES[settings['language']]
    font = pygame.font.Font(None, 74)
    title_text = font.render(lang['control_settings'], True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 150))

    move_up_text = font.render(lang['move_up'], True, (255, 255, 255))
    move_up_rect = move_up_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))

    move_down_text = font.render(lang['move_down'], True, (255, 255, 255))
    move_down_rect = move_down_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    move_left_text = font.render(lang['move_left'], True, (255, 255, 255))
    move_left_rect = move_left_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))

    move_right_text = font.render(lang['move_right'], True, (255, 255, 255))
    move_right_rect = move_right_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 250))

    back_text = font.render(lang['back_to_settings'], True, (255, 255, 255))
    back_rect = back_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 350))

    changing_key = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    settings['fullscreen'] = not settings['fullscreen']
                    if settings['fullscreen']:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Возврат в настройки
                elif changing_key:
                    settings[changing_key] = event.key
                    changing_key = None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if move_up_rect.collidepoint(event.pos):
                        select_sound.play()
                        changing_key = 'move_up'
                    elif move_down_rect.collidepoint(event.pos):
                        select_sound.play()
                        changing_key = 'move_down'
                    elif move_left_rect.collidepoint(event.pos):
                        select_sound.play()
                        changing_key = 'move_left'
                    elif move_right_rect.collidepoint(event.pos):
                        select_sound.play()
                        changing_key = 'move_right'
                    elif back_rect.collidepoint(event.pos):
                        select_sound.play()
                        running = False  # Возврат в настройки

        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())), (0, 0))  # Отображаем фон
        screen.blit(title_text, title_rect)
        screen.blit(move_up_text, move_up_rect)
        screen.blit(move_down_text, move_down_rect)
        screen.blit(move_left_text, move_left_rect)
        screen.blit(move_right_text, move_right_rect)
        screen.blit(back_text, back_rect)

        pygame.display.flip()


def draw_slider(screen, text, value, min_value, max_value, x, y, width, height):
    font = pygame.font.Font(None, 36)
    label = font.render(text, True, (255, 255, 255))
    screen.blit(label, (x, y))

    slider_rect = pygame.Rect(x, y + 40, width, height)
    pygame.draw.rect(screen, (200, 200, 200), slider_rect)
    handle_pos = ((value - min_value) / (max_value - min_value)) * width
    handle_rect = pygame.Rect(x + handle_pos - 10, y + 30, 20, 20)
    pygame.draw.rect(screen, (100, 100, 100), handle_rect)

    return slider_rect, handle_rect


def audio_settings(screen, select_sound, settings):
    lang = LANGUAGES[settings['language']]
    font = pygame.font.Font(None, 74)
    title_text = font.render(lang['audio_settings'], True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 150))

    back_text = font.render(lang['back_to_settings'], True, (255, 255, 255))
    back_rect = back_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))

    music_volume = settings['music_volume']
    effects_volume = settings['effects_volume']

    dragging_music = False
    dragging_effects = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    settings['fullscreen'] = not settings['fullscreen']
                    if settings['fullscreen']:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Возврат в настройки
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if back_rect.collidepoint(event.pos):
                        select_sound.play()
                        running = False  # Возврат в настройки
                    elif music_slider.collidepoint(event.pos):
                        dragging_music = True
                    elif effects_slider.collidepoint(event.pos):
                        dragging_effects = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # ЛКМ
                    dragging_music = False
                    dragging_effects = False
            elif event.type == pygame.MOUSEMOTION:
                if dragging_music:
                    music_volume = min(max((event.pos[0] - music_slider.x) / music_slider.width, 0), 1)
                    settings['music_volume'] = music_volume
                elif dragging_effects:
                    effects_volume = min(max((event.pos[0] - effects_slider.x) / effects_slider.width, 0), 1)
                    settings['effects_volume'] = effects_volume

        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())),
                    (0, 0))  # Отображаем фон
        screen.blit(title_text, title_rect)
        music_slider, music_handle = draw_slider(screen, lang['music_volume'], music_volume, 0, 1,
                                                 screen.get_width() // 2 - 150, screen.get_height() // 2 - 50, 300, 20)
        effects_slider, effects_handle = draw_slider(screen, lang['effects_volume'], effects_volume, 0, 1,
                                                     screen.get_width() // 2 - 150, screen.get_height() // 2 + 50, 300,
                                                     20)
        screen.blit(back_text, back_rect)

        pygame.display.flip()


def video_settings(screen, select_sound, settings):
    lang = LANGUAGES[settings['language']]
    font = pygame.font.Font(None, 74)
    title_text = font.render(lang['video_settings'], True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 150))

    fullscreen_text = font.render(lang['fullscreen'], True, (255, 255, 255))
    fullscreen_rect = fullscreen_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))

    language_text = font.render(lang['language'], True, (255, 255, 255))
    language_rect = language_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    back_text = font.render(lang['back_to_settings'], True, (255, 255, 255))
    back_rect = back_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    settings['fullscreen'] = not settings['fullscreen']
                    if settings['fullscreen']:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Возврат в настройки
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if fullscreen_rect.collidepoint(event.pos):
                        select_sound.play()
                        settings['fullscreen'] = not settings['fullscreen']  # Переключаем полноэкранный режим
                        if settings['fullscreen']:
                            screen = pygame.display.set_mode((screen.get_width(), screen.get_height()),
                                                             pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode((screen.get_width(), screen.get_height()),
                                                             pygame.RESIZABLE)
                    elif language_rect.collidepoint(event.pos):
                        select_sound.play()
                        language_settings(screen, select_sound, settings)  # Открытие настроек языка
                    elif back_rect.collidepoint(event.pos):
                        select_sound.play()
                        running = False  # Возврат в настройки

        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())),
                    (0, 0))  # Отображаем фон
        screen.blit(title_text, title_rect)
        screen.blit(fullscreen_text, fullscreen_rect)
        screen.blit(language_text, language_rect)
        screen.blit(back_text, back_rect)

        pygame.display.flip()


def language_settings(screen, select_sound, settings):
    lang = LANGUAGES[settings['language']]
    font = pygame.font.Font(None, 74)
    title_text = font.render(lang['language'], True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 150))

    english_text = font.render(lang['english'], True, (255, 255, 255))
    english_rect = english_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))

    russian_text = font.render(lang['russian'], True, (255, 255, 255))
    russian_rect = russian_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

    back_text = font.render(lang['back_to_settings'], True, (255, 255, 255))
    back_rect = back_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 150))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    settings['fullscreen'] = not settings['fullscreen']
                    if settings['fullscreen']:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Возврат в настройки
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if english_rect.collidepoint(event.pos):
                        select_sound.play()
                        settings['language'] = 'en'  # Устанавливаем английский язык
                    elif russian_rect.collidepoint(event.pos):
                        select_sound.play()
                        settings['language'] = 'ru'  # Устанавливаем русский язык
                    elif back_rect.collidepoint(event.pos):
                        select_sound.play()
                        running = False  # Возврат в настройки

        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())),
                    (0, 0))  # Отображаем фон
        screen.blit(title_text, title_rect)
        screen.blit(english_text, english_rect)
        screen.blit(russian_text, russian_rect)
        screen.blit(back_text, back_rect)

        pygame.display.flip()