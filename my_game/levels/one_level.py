import pygame
import sys
from objects import Player, Enemy, Bonus, Obstacle  # Импортируем классы

class one:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        # Создаём игрока
        self.player = Player("assets/images/player.png", 50, 50, 5)

        # Создаём выход (можно заменить на картинку)
        self.exit = pygame.Rect(screen.get_width() - 100, screen.get_height() - 100, 50, 50)

        # Создаём стены как препятствия
        self.walls = [
            Obstacle("assets/images/wall.png", 100, 100),
            Obstacle("assets/images/wall.png", 300, 100),
            Obstacle("assets/images/wall.png", 100, 200),
        ]

        # Бонусы
        self.bonuses = [
            Bonus("assets/images/bonus.png", 150, 150),
            Bonus("assets/images/bonus.png", 350, 250),
        ]

        # Враги (с анимацией движения)
        self.enemies = [
            Enemy("assets/images/enemy.png", 250, 250, 2),
        ]

    def run_level(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_F11:
                        self.settings['fullscreen'] = not self.settings['fullscreen']
                        if self.settings['fullscreen']:
                            self.screen = pygame.display.set_mode((self.screen.get_width(), self.screen.get_height()), pygame.FULLSCREEN)
                        else:
                            self.screen = pygame.display.set_mode((self.screen.get_width(), self.screen.get_height()), pygame.RESIZABLE)

            # Управление персонажем
            keys = pygame.key.get_pressed()
            if keys[self.settings['move_left']]:
                self.player.rect.x -= self.player.speed
            if keys[self.settings['move_right']]:
                self.player.rect.x += self.player.speed
            if keys[self.settings['move_up']]:
                self.player.rect.y -= self.player.speed
            if keys[self.settings['move_down']]:
                self.player.rect.y += self.player.speed

            # Столкновение со стенами
            for wall in self.walls:
                if self.player.rect.colliderect(wall.rect):
                    if keys[self.settings['move_left']]:
                        self.player.rect.x += self.player.speed
                    if keys[self.settings['move_right']]:
                        self.player.rect.x -= self.player.speed
                    if keys[self.settings['move_up']]:
                        self.player.rect.y += self.player.speed
                    if keys[self.settings['move_down']]:
                        self.player.rect.y -= self.player.speed

            # Подбор бонусов
            for bonus in self.bonuses[:]:
                if self.player.rect.colliderect(bonus.rect):
                    self.bonuses.remove(bonus)
                    # Можно добавить звук или эффект

            # Движение врагов к игроку
            for enemy in self.enemies:
                enemy.move_towards_player(self.player.rect.topleft)
                if self.player.rect.colliderect(enemy.rect):
                    running = False  # Игрок проиграл

            # Проверка выхода
            if self.player.rect.colliderect(self.exit):
                running = False  # Игрок прошёл уровень

            # Отрисовка сцены
            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)

            for wall in self.walls:
                wall.draw(self.screen)

            for bonus in self.bonuses:
                bonus.draw(self.screen)

            for enemy in self.enemies:
                enemy.draw(self.screen)

            pygame.draw.rect(self.screen, (255, 0, 0), self.exit)  # Временно квадрат выхода


            pygame.display.flip()
            clock.tick(60)
