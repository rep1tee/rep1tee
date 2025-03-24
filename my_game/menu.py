import pygame
import sys
from levels.one_level import one
from levels.level2 import two
from levels.level3 import fre
from levels.maze_level import MazeLevel

LANGUAGES = {
    'en': {
        'main_menu': 'Main Menu',
        'start_game': 'Start Game',
        'settings': 'Settings',
        'exit': 'Exit',
        'select_level': 'Select Level',
        'back_to_menu': 'Back to Menu',
        'control_settings': 'Control Settings',
        'audio_settings': 'Audio Settings',
        'video_settings': 'Video Settings',
        'language': 'Language',  # <-- Он должен быть здесь!
        'back_to_settings': 'Back to Settings',
        'move_up': 'Move Up',
        'move_down': 'Move Down',
        'move_left': 'Move Left',
        'move_right': 'Move Right',
    },
    'ru': {
        'main_menu': 'Главное Меню',
        'start_game': 'Начать Игру',
        'settings': 'Настройки',
        'exit': 'Выход',
        'select_level': 'Выбрать Уровень',
        'back_to_menu': 'Назад в Меню',
        'control_settings': 'Настройки Управления',
        'audio_settings': 'Настройки Аудио',
        'video_settings': 'Настройки Видео',
        'language': 'Язык',  # <-- И здесь!
        'back_to_settings': 'Назад к Настройкам',
        'move_up': 'Движение Вверх',
        'move_down': 'Движение Вниз',
        'move_left': 'Движение Влево',
        'move_right': 'Движение Вправо',
    }
}

# Загрузка изображения фона
menu_background_image = pygame.image.load("assets/images/menu_background.png")

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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if level1_rect.collidepoint(event.pos):
                        select_sound.play()
                        one(screen, settings).run_level()
                    elif level2_rect.collidepoint(event.pos):
                        select_sound.play()
                        two(screen, settings).run_level()
                    elif level3_rect.collidepoint(event.pos):
                        select_sound.play()
                        fre(screen, settings).run_level()
                    elif maze_level_rect.collidepoint(event.pos):
                        select_sound.play()
                        MazeLevel(screen, settings).run_level()
                    elif back_rect.collidepoint(event.pos):
                        select_sound.play()
                        running = False  # Возврат в главное меню

        screen.fill((0, 0, 0))
        screen.blit(title_text, title_rect)
        screen.blit(level1_text, level1_rect)
        screen.blit(level2_text, level2_rect)
        screen.blit(level3_text, level3_rect)
        screen.blit(maze_level_text, maze_level_rect)
        screen.blit(back_text, back_rect)

        pygame.display.flip()



def settings_menu(screen, select_sound, settings):
    lang = LANGUAGES[settings['language']]
    font = pygame.font.Font(None, 60)  # Уменьшаем размер шрифта


    menu_items = [
        ("Control Settings", -150),
        ("Audio Settings", -50),
        ("Video Settings", 50),
        ("Language", 150),
        ("Back to Menu", 250)
    ]



    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())), (0, 0))

        rects = []
        for text, y_offset in menu_items:
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + y_offset))
            screen.blit(text_surface, text_rect)
            rects.append((text_rect, text))  # Запоминаем, какие кнопки где находятся

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    settings['fullscreen'] = not settings['fullscreen']
                    pygame.display.set_mode((screen.get_width(), screen.get_height()),
                                            pygame.FULLSCREEN if settings['fullscreen'] else pygame.RESIZABLE)
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Выход из настроек
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for rect, name in rects:
                    if rect.collidepoint(event.pos):
                        select_sound.play()
                        if name == lang['control_settings']:
                            control_settings(screen, select_sound, settings)
                        elif name == lang['audio_settings']:
                            audio_settings(screen, select_sound, settings)
                        elif name == lang['video_settings']:
                            video_settings(screen, select_sound, settings)
                        elif name == "Language":
                            language_settings(screen, select_sound, settings)  # Меню языка
                        elif name == lang['back_to_menu']:
                            running = False  # Выход в главное меню



class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 40)  # Уменьшим шрифт
        self.options = ["Level 1", "Level 2", "Level 3", "Maze Level", "Exit"]
        self.selected = 0

    def run_menu(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))

            width, height = self.screen.get_size()
            spacing = height // (len(self.options) + 2)  # Уменьшим отступы
            start_y = height // 4  # Сдвигаем выше

            for i, option in enumerate(self.options):
                color = (255, 255, 255) if i != self.selected else (255, 255, 0)
                text_surface = self.font.render(option, True, color)
                text_rect = text_surface.get_rect(center=(width // 2, start_y + i * spacing))
                self.screen.blit(text_surface, text_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected == len(self.options) - 1:
                            pygame.quit()
                            sys.exit()  # Выход из игры
                        return self.selected
                    elif event.key == pygame.K_ESCAPE:
                        return

def control_settings(screen, select_sound, settings):
    font = pygame.font.Font(None, 60)
    lang = LANGUAGES[settings['language']]

    if 'controls' not in settings:
        settings['controls'] = {
            'left': pygame.K_a,
            'right': pygame.K_d,
            'up': pygame.K_w,
            'down': pygame.K_s
        }

    controls = settings['controls']
    keys = ['left', 'right', 'up', 'down']
    key_labels = {"left": "Left", "right": "Right", "up": "Up", "down": "Down"}

    selected_key = None  # Какая клавиша сейчас изменяется?
    waiting_for_input = False  # Ждем ли новую клавишу?

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())), (0, 0))

        menu_items = []
        for i, key in enumerate(keys):
            text = f"{key_labels[key]}: {pygame.key.name(controls[key]).upper()}"
            color = (255, 0, 0) if selected_key == key else (255, 255, 255)
            surface = font.render(text, True, color)
            rect = surface.get_rect(center=(screen.get_width() // 2, 200 + i * 80))
            menu_items.append((key, surface, rect))
            screen.blit(surface, rect)

        # Текст при ожидании новой клавиши
        if waiting_for_input:
            input_text = font.render("Press any key...", True, (255, 255, 0))
            screen.blit(input_text, (screen.get_width() // 2 - 100, screen.get_height() - 100))

        # Кнопка выхода
        back_surface = font.render(lang['back_to_menu'], True, (255, 255, 255))
        back_rect = back_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() - 50))
        screen.blit(back_surface, back_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if waiting_for_input and selected_key:  # Ждем клавишу?
                    controls[selected_key] = event.key  # Записываем новую клавишу
                    waiting_for_input = False
                    selected_key = None
                elif event.key == pygame.K_ESCAPE:
                    running = False  # Выход из меню
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for key, _, rect in menu_items:
                    if rect.collidepoint(event.pos):
                        if selected_key == key:  # Двойной клик?
                            waiting_for_input = True
                        selected_key = key  # Помечаем ключ для изменения
                if back_rect.collidepoint(event.pos):  # Кнопка выхода
                    running = False


def get_new_key(current_key):
    waiting_for_key = True
    while waiting_for_key:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return event.key

def audio_settings(screen, select_sound, settings):
    lang = LANGUAGES[settings['language']]
    font = pygame.font.Font(None, 74)
    title_text = font.render(lang['audio_settings'], True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 150))

    music_volume_text = font.render(f"Music Volume: {int(settings['music_volume'] * 100)}%", True, (255, 255, 255))
    music_volume_rect = music_volume_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))

    effects_volume_text = font.render(f"Effects Volume: {int(settings['effects_volume'] * 100)}%", True, (255, 255, 255))
    effects_volume_rect = effects_volume_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

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
                    running = False  # Возврат в главное меню
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    if music_volume_rect.collidepoint(event.pos):
                        select_sound.play()
                        settings['music_volume'] = adjust_volume(settings['music_volume'])
                        music_volume_text = font.render(f"Music Volume: {int(settings['music_volume'] * 100)}%", True, (255, 255, 255))
                        music_volume_rect = music_volume_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
                    elif effects_volume_rect.collidepoint(event.pos):
                        select_sound.play()
                        settings['effects_volume'] = adjust_volume(settings['effects_volume'])
                        effects_volume_text = font.render(f"Effects Volume: {int(settings['effects_volume'] * 100)}%", True, (255, 255, 255))
                        effects_volume_rect = effects_volume_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
                    elif back_rect.collidepoint(event.pos):
                        select_sound.play()
                        running = False  # Возврат в главное меню

        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())), (0, 0))  # Отображаем фон
        screen.blit(title_text, title_rect)
        screen.blit(music_volume_text, music_volume_rect)
        screen.blit(effects_volume_text, effects_volume_rect)
        screen.blit(back_text, back_rect)

        pygame.display.flip()

def adjust_volume(current_volume):
    return min(1.0, max(0.0, current_volume + 0.1 * (1 if current_volume < 1.0 else -1.0)))

def video_settings(screen, select_sound, settings):
    font = pygame.font.Font(None, 60)  # Размер шрифта
    lang = LANGUAGES[settings['language']]

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())), (0, 0))

        # Создаем текстовые элементы
        fullscreen_text = f"Fullscreen: {'ON' if settings['fullscreen'] else 'OFF'}"
        fullscreen_surface = font.render(fullscreen_text, True, (255, 255, 255))
        fullscreen_rect = fullscreen_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))

        back_text = lang['back_to_menu']
        back_surface = font.render(back_text, True, (255, 255, 255))
        back_rect = back_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))

        screen.blit(fullscreen_surface, fullscreen_rect)
        screen.blit(back_surface, back_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if fullscreen_rect.collidepoint(event.pos):
                    settings['fullscreen'] = not settings['fullscreen']
                    select_sound.play()
                    if settings['fullscreen']:
                        screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
                elif back_rect.collidepoint(event.pos):
                    select_sound.play()
                    running = False

def language_settings(screen, select_sound, settings):
    font = pygame.font.Font(None, 60)  # Уменьшаем шрифт
    lang = LANGUAGES[settings['language']]

    menu_items = [
        ("English", -50),
        ("Русский", 50),
        (lang['back_to_menu'], 150)
    ]

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(pygame.transform.scale(menu_background_image, (screen.get_width(), screen.get_height())), (0, 0))

        rects = []
        for text, y_offset in menu_items:
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + y_offset))
            screen.blit(text_surface, text_rect)
            rects.append((text_rect, text))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Закрываем меню
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for rect, name in rects:
                    if rect.collidepoint(event.pos):
                        select_sound.play()
                        if name == "English":
                            settings['language'] = 'en'
                        elif name == "Русский":
                            settings['language'] = 'ru'
                        elif name == lang['back_to_menu']:  # Теперь точно работает
                            running = False  # Закрываем меню
